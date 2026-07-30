const { chromium } = require(
    process.env.PLAYWRIGHT_MODULE ||
    "/usr/local/lib/node_modules/backstopjs/node_modules/playwright"
);

const portalUrl = process.env.PORTAL_TEST_URL ||
    "https://human-infra.pages.dev/";
const wikiUrl = process.env.WIKI_TEST_URL ||
    "https://wiki.tradecatlabs.com/";
const query = "长寿逃逸速度";

async function main() {
    const portalHostname = new URL(portalUrl).hostname;
    const proxyServer = process.env.HTTPS_PROXY ||
        process.env.https_proxy ||
        process.env.HTTP_PROXY ||
        process.env.http_proxy;
    const launchOptions = { headless: true };
    if (proxyServer &&
        portalHostname !== "localhost" &&
        portalHostname !== "127.0.0.1") {
        launchOptions.proxy = { server: proxyServer };
    }
    const browser = await chromium.launch(launchOptions);
    const page = await browser.newPage({
        viewport: { width: 1280, height: 900 },
        extraHTTPHeaders: { DNT: "1" },
    });
    const externalWikipediaRequests = [];
    const browserProblems = [];

    page.on("request", (request) => {
        const hostname = new URL(request.url()).hostname;
        if (hostname === "wikipedia.org" ||
            hostname.endsWith(".wikipedia.org")) {
            externalWikipediaRequests.push(request.url());
        }
    });
    page.on("console", (message) => {
        if (["warning", "error"].includes(message.type())) {
            browserProblems.push(`${message.type()}: ${message.text()}`);
        }
    });
    page.on("pageerror", (error) => {
        browserProblems.push(`pageerror: ${error}`);
    });

    try {
        await page.goto(portalUrl, {
            waitUntil: "domcontentloaded",
            timeout: 30_000,
        });
        await page.locator("#searchInput").fill(query);
        await page.waitForTimeout(800);

        const expectedAction = new URL("/search/", wikiUrl).toString();
        const action = await page.locator("#search-form").getAttribute("action");
        if (action !== expectedAction) {
            throw new Error(
                `门户搜索 action 错误: expected=${expectedAction}, actual=${action}`
            );
        }
        if (externalWikipediaRequests.length) {
            throw new Error(
                "门户搜索向外部 Wikipedia 泄漏查询: " +
                externalWikipediaRequests.join(", ")
            );
        }

        await page.locator("#search-form button[type='submit']").click();
        await page.waitForURL((url) => {
            const expected = new URL(wikiUrl);
            return url.origin === expected.origin &&
                url.pathname === "/search/" &&
                url.searchParams.get("q") === query;
        }, { timeout: 15_000 });
        await page.locator("#hi-search-summary").waitFor({
            state: "visible",
            timeout: 15_000,
        });
        await page.waitForFunction(() => {
            const summary = document.getElementById("hi-search-summary");
            return summary && summary.textContent.includes("找到");
        });
        const results = await page.locator("#hi-search-results li").allTextContents();
        if (!results.includes(query)) {
            throw new Error(`本地 Wiki 搜索未返回目标词条: ${results.join(", ")}`);
        }

        const upstreamPage = await browser.newPage({
            extraHTTPHeaders: { DNT: "1" },
        });
        const upstreamResponse = await upstreamPage.goto(
            new URL("UPSTREAM.md", portalUrl).toString(),
            { waitUntil: "domcontentloaded", timeout: 30_000 }
        );
        if (!upstreamResponse || upstreamResponse.status() !== 200) {
            throw new Error(
                `门户上游说明不可达: status=${upstreamResponse?.status()}`
            );
        }
        await upstreamPage.close();

        if (browserProblems.length) {
            throw new Error(`浏览器问题: ${browserProblems.join(" | ")}`);
        }
        console.log(
            `portal search ok: action=${action}, results=${results.length}, ` +
            "external_wikipedia_requests=0, upstream=200"
        );
    } finally {
        await browser.close();
    }
}

main().catch((error) => {
    console.error(error);
    process.exit(1);
});
