import { spawn } from 'node:child_process';
import { existsSync } from 'node:fs';
import { mkdir, readFile, rm, writeFile } from 'node:fs/promises';
import { tmpdir } from 'node:os';
import path from 'node:path';
import process from 'node:process';

function parseArgs(argv) {
  const result = {};
  for (let index = 2; index < argv.length; index += 2) {
    const key = argv[index]?.replace(/^--/, '');
    const value = argv[index + 1];
    if (!key || value === undefined) throw new Error(`参数不完整：${argv[index] ?? ''}`);
    result[key] = value;
  }
  return result;
}

const args = parseArgs(process.argv);
const mode = args.mode ?? 'discover';
const targetUrl = args.url ?? 'https://www.historicaltechtree.com/';
const outputDir = path.resolve(args.output ?? 'browser-capture');
const chrome = process.env.CHROME_PATH
  ?? 'C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe';
const routes = mode === 'discover'
  ? ['/', '/about', '/changelog', '/image-credits', '/mini-tree']
  : ['/'];

if (!['discover', 'verify'].includes(mode)) throw new Error(`未知模式：${mode}`);
if (!existsSync(chrome)) throw new Error(`未找到 Chrome：${chrome}`);

await mkdir(outputDir, { recursive: true });
const runtimeDir = path.join(
  tmpdir(),
  `historical-tech-tree-chrome-${process.pid}-${Date.now()}`,
);
await rm(runtimeDir, { recursive: true, force: true });
await mkdir(runtimeDir, { recursive: true });

const browser = spawn(chrome, [
  '--headless=new',
  '--disable-extensions',
  '--disable-background-networking',
  '--no-first-run',
  '--no-default-browser-check',
  '--remote-debugging-port=0',
  `--user-data-dir=${runtimeDir}`,
  '--window-size=1600,1100',
  'about:blank',
], { stdio: ['ignore', 'ignore', 'pipe'], windowsHide: true });

let browserStderr = '';
browser.stderr.on('data', (chunk) => { browserStderr += chunk.toString(); });

async function waitForDevTools() {
  const activePort = path.join(runtimeDir, 'DevToolsActivePort');
  for (let index = 0; index < 150; index += 1) {
    if (existsSync(activePort)) {
      const [port] = (await readFile(activePort, 'utf8')).trim().split(/\r?\n/);
      return Number(port);
    }
    await new Promise((resolve) => setTimeout(resolve, 100));
  }
  throw new Error(`Chrome 调试端口启动超时：${browserStderr.slice(-1000)}`);
}

const port = await waitForDevTools();
const targets = await (await fetch(`http://127.0.0.1:${port}/json/list`)).json();
const target = targets.find((item) => item.type === 'page');
if (!target) throw new Error('未找到 Chrome 页面目标。');

const ws = new WebSocket(target.webSocketDebuggerUrl);
await new Promise((resolve, reject) => {
  ws.addEventListener('open', resolve, { once: true });
  ws.addEventListener('error', reject, { once: true });
});

let nextId = 1;
const pending = new Map();
const oneShotEvents = new Map();
const responses = new Map();
const failedRequests = [];
const consoleErrors = [];

ws.addEventListener('message', (event) => {
  const message = JSON.parse(event.data);
  if (message.id) {
    const waiter = pending.get(message.id);
    if (!waiter) return;
    pending.delete(message.id);
    if (message.error) waiter.reject(new Error(message.error.message));
    else waiter.resolve(message.result);
    return;
  }

  if (message.method === 'Network.responseReceived') {
    const response = message.params.response;
    responses.set(response.url, {
      url: response.url,
      status: response.status,
      mimeType: response.mimeType,
      protocol: response.protocol,
      fromDiskCache: response.fromDiskCache,
      fromServiceWorker: response.fromServiceWorker,
      headers: response.headers,
    });
  }
  if (message.method === 'Network.loadingFailed') {
    failedRequests.push(message.params);
  }
  if (message.method === 'Runtime.consoleAPICalled' && message.params.type === 'error') {
    consoleErrors.push(message.params);
  }
  if (message.method === 'Runtime.exceptionThrown') {
    consoleErrors.push(message.params.exceptionDetails);
  }

  const handlers = oneShotEvents.get(message.method) ?? [];
  handlers.splice(0).forEach((handler) => handler(message.params));
});

function send(method, params = {}) {
  const id = nextId++;
  ws.send(JSON.stringify({ id, method, params }));
  return new Promise((resolve, reject) => pending.set(id, { resolve, reject }));
}

function once(method, timeoutMs = 45000) {
  return new Promise((resolve, reject) => {
    const timer = setTimeout(() => reject(new Error(`等待 ${method} 超时。`)), timeoutMs);
    const handler = (params) => {
      clearTimeout(timer);
      resolve(params);
    };
    const handlers = oneShotEvents.get(method) ?? [];
    handlers.push(handler);
    oneShotEvents.set(method, handlers);
  });
}

async function waitForProcessExit(child, timeoutMs = 10000) {
  if (child.exitCode !== null) return;
  await Promise.race([
    new Promise((resolve) => child.once('exit', resolve)),
    new Promise((resolve) => setTimeout(resolve, timeoutMs)),
  ]);
}

async function removeRuntimeDirectory(directory) {
  for (let attempt = 0; attempt < 20; attempt += 1) {
    try {
      await rm(directory, { recursive: true, force: true });
      return true;
    } catch (error) {
      if (!['EBUSY', 'EPERM', 'ENOTEMPTY'].includes(error?.code)) throw error;
      await new Promise((resolve) => setTimeout(resolve, 250));
    }
  }
  return false;
}

async function evaluate(expression) {
  const result = await send('Runtime.evaluate', {
    expression,
    awaitPromise: true,
    returnByValue: true,
  });
  if (result.exceptionDetails) throw new Error(result.exceptionDetails.text);
  return result.result.value;
}

function routeName(route) {
  return route === '/' ? 'index' : route.slice(1).replace(/[^a-z0-9]+/gi, '-');
}

async function inspectPage() {
  return evaluate(`(async () => {
    const bodyText = document.body?.innerText ?? '';
    const buttons = [...document.querySelectorAll('button')];
    const zoomBefore = buttons.map((button) => button.textContent?.trim()).find((text) => /%$/.test(text ?? '')) ?? '';
    const plus = buttons.find((button) => button.textContent?.trim() === '+');
    plus?.click();
    await new Promise((resolve) => setTimeout(resolve, 500));
    const zoomAfter = buttons.map((button) => button.textContent?.trim()).find((text) => /%$/.test(text ?? '')) ?? '';

    const nodeImage = document.querySelector('img[src*="/tech-images/"]');
    const beforeUrl = location.href;
    const beforeDialogs = document.querySelectorAll('[role="dialog"], dialog, [class*="modal"], [class*="detail"]').length;
    let clickable = nodeImage;
    let ancestor = nodeImage;
    for (let depth = 0; ancestor && depth < 8; depth += 1) {
      const style = getComputedStyle(ancestor);
      if (ancestor.matches?.('button, a, [role="button"]') || style.cursor === 'pointer') {
        clickable = ancestor;
        break;
      }
      ancestor = ancestor.parentElement;
    }

    let graph = null;
    try {
      const response = await fetch('/api/inventions');
      const data = await response.json();
      const nodes = data.nodes ?? data.inventions ?? data.technologies ?? [];
      const links = data.links ?? data.connections ?? data.edges ?? [];
      graph = {
        status: response.status,
        nodeCount: Array.isArray(nodes) ? nodes.length : -1,
        linkCount: Array.isArray(links) ? links.length : -1,
        topLevelKeys: Object.keys(data),
      };
    } catch (error) {
      graph = { error: String(error) };
    }

    return {
      title: document.title,
      readyState: document.readyState,
      bodyCharacters: bodyText.length,
      hasBrand: /HISTORICAL TECH TREE/i.test(bodyText),
      nodeImageCount: document.querySelectorAll('img[src*="/tech-images/"]').length,
      allImageCount: document.images.length,
      zoom: {
        plusPresent: Boolean(plus),
        before: zoomBefore,
        after: zoomAfter,
      },
      nodeInteraction: {
        targetPresent: Boolean(clickable),
        beforeUrl,
        beforeDialogs,
      },
      graph,
      html: document.documentElement.outerHTML,
      performanceUrls: performance.getEntriesByType('resource').map((entry) => entry.name),
    };
  })()`);
}

async function clickNodeTarget() {
  try {
    return await evaluate(`(() => {
      const nodeImage = document.querySelector('img[src*="/tech-images/"]');
      let clickable = nodeImage;
      let ancestor = nodeImage;
      for (let depth = 0; ancestor && depth < 8; depth += 1) {
        const style = getComputedStyle(ancestor);
        if (ancestor.matches?.('button, a, [role="button"]') || style.cursor === 'pointer') {
          clickable = ancestor;
          break;
        }
        ancestor = ancestor.parentElement;
      }
      if (!clickable) return false;
      clickable.dispatchEvent(new MouseEvent('click', { bubbles: true, cancelable: true }));
      return true;
    })()`);
  } catch (error) {
    if (/navigated or closed|context was destroyed/i.test(error.message)) return true;
    throw error;
  }
}

async function inspectInteractionResult(before) {
  for (let attempt = 0; attempt < 30; attempt += 1) {
    try {
      return await evaluate(`(() => ({
        url: location.href,
        dialogs: document.querySelectorAll(
          '[role="dialog"], dialog, [class*="modal"], [class*="detail"]'
        ).length,
      }))()`);
    } catch (error) {
      if (!/navigated or closed|context was destroyed/i.test(error.message)) throw error;
      await new Promise((resolve) => setTimeout(resolve, 200));
    }
  }
  return { url: before.beforeUrl, dialogs: before.beforeDialogs };
}

const pageReports = [];
try {
  await Promise.all([
    send('Runtime.enable'),
    send('Page.enable'),
    send('Network.enable', {
      maxTotalBufferSize: 100_000_000,
      maxResourceBufferSize: 20_000_000,
    }),
  ]);

  for (const route of routes) {
    const url = new URL(route, targetUrl).href;
    const loaded = once('Page.loadEventFired');
    await send('Page.navigate', { url });
    await loaded;
    await evaluate(`new Promise((resolve) => {
      const deadline = Date.now() + 30000;
      const poll = () => {
        if (document.readyState === 'complete' || Date.now() >= deadline) resolve();
        else setTimeout(poll, 200);
      };
      poll();
    })`);
    await new Promise((resolve) => setTimeout(resolve, route === '/' ? 7000 : 2500));

    const inspection = await inspectPage();
    const clicked = await clickNodeTarget();
    await new Promise((resolve) => setTimeout(resolve, 1200));
    const interactionResult = await inspectInteractionResult(inspection.nodeInteraction);
    inspection.nodeInteraction = {
      targetPresent: inspection.nodeInteraction.targetPresent,
      clickDispatched: clicked,
      urlChanged: interactionResult.url !== inspection.nodeInteraction.beforeUrl,
      dialogChanged: interactionResult.dialogs > inspection.nodeInteraction.beforeDialogs,
    };
    const name = routeName(route);
    await writeFile(path.join(outputDir, `${name}.rendered.html`), inspection.html, 'utf8');
    delete inspection.html;
    pageReports.push({ route, url, ...inspection });

    if (route === '/') {
      const screenshot = await send('Page.captureScreenshot', {
        format: 'png',
        captureBeyondViewport: false,
      });
      await writeFile(
        path.join(outputDir, `${mode}.png`),
        Buffer.from(screenshot.data, 'base64'),
      );
    }
  }

  const baseOrigin = new URL(targetUrl).origin;
  const remoteRuntimeRequests = [...responses.values()]
    .filter((item) => {
      const protocol = new URL(item.url).protocol;
      return ['http:', 'https:'].includes(protocol)
        && new URL(item.url).origin !== baseOrigin;
    });
  const main = pageReports[0];
  const graphReady = main?.graph?.nodeCount >= 2400 && main?.graph?.linkCount >= 3700;
  const interactionReady = main?.zoom?.plusPresent
    && main?.nodeInteraction?.targetPresent
    && (main.nodeInteraction.urlChanged || main.nodeInteraction.dialogChanged);
  const report = {
    checkedAt: new Date().toISOString(),
    mode,
    targetUrl,
    verdict: graphReady
      && main?.hasBrand
      && main?.bodyCharacters > 1000
      && interactionReady
      && (mode !== 'verify' || remoteRuntimeRequests.length === 0)
      ? 'PASS'
      : 'BLOCK',
    pages: pageReports,
    resources: [...responses.values()].sort((left, right) => left.url.localeCompare(right.url)),
    failedRequests,
    consoleErrors,
    remoteRuntimeRequests,
  };
  await writeFile(
    path.join(outputDir, `${mode}-report.json`),
    `${JSON.stringify(report, null, 2)}\n`,
    'utf8',
  );
  console.log(JSON.stringify({
    verdict: report.verdict,
    mode,
    resources: report.resources.length,
    nodes: main?.graph?.nodeCount,
    links: main?.graph?.linkCount,
    remoteRuntimeRequests: remoteRuntimeRequests.length,
  }));
  if (report.verdict !== 'PASS') process.exitCode = 1;
} finally {
  ws.close();
  if (browser.exitCode === null) browser.kill();
  await waitForProcessExit(browser);
  if (browser.exitCode === null) {
    browser.kill('SIGKILL');
    await waitForProcessExit(browser);
  }
  const removed = await removeRuntimeDirectory(runtimeDir);
  if (!removed) {
    console.error(`警告：Chrome 临时目录仍被系统占用，将由系统临时目录清理：${runtimeDir}`);
  }
}
