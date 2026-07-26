const WIKI_ORIGIN = "https://human-infra-wiki.pages.dev";

let snapshotPromise;
let shellPromise;

function normalizeTitle(value) {
	return decodeURIComponent(value)
		.replaceAll("_", " ")
		.replaceAll("+", " ")
		.trim()
		.toLocaleLowerCase("zh-CN");
}

function escapeHtml(value) {
	return String(value)
		.replaceAll("&", "&amp;")
		.replaceAll("<", "&lt;")
		.replaceAll(">", "&gt;")
		.replaceAll('"', "&quot;")
		.replaceAll("'", "&#039;");
}

async function loadSnapshot(env, requestUrl) {
	if (!snapshotPromise) {
		const url = new URL("/snapshot/index.json", requestUrl);
		snapshotPromise = env.ASSETS.fetch(url).then(async (response) => {
			if (!response.ok) {
				throw new Error(`快照索引不可用: ${response.status}`);
			}
			const index = await response.json();
			index.byTitle = new Map();
			for (const page of index.pages) {
				index.byTitle.set(page.normalized, page);
				for (const alias of page.aliases || []) {
					index.byTitle.set(normalizeTitle(alias), page);
				}
			}
			return index;
		});
	}
	return snapshotPromise;
}

async function loadShell(env, requestUrl) {
	if (!shellPromise) {
		shellPromise = env.ASSETS
			.fetch(new URL("/snapshot/shell.html", requestUrl))
			.then(async (response) => {
				if (!response.ok) {
					throw new Error(`Wiki 快照模板不可用: ${response.status}`);
				}
				return response.text();
			});
	}
	return shellPromise;
}

function requestedTitle(url, mainPage) {
	if (url.pathname === "/" || url.pathname === "/index.php") {
		return url.searchParams.get("title") || mainPage;
	}
	for (const prefix of ["/index.php/", "/wiki/"]) {
		if (url.pathname.startsWith(prefix)) {
			return url.pathname.slice(prefix.length);
		}
	}
	return null;
}

function renderShell(shell, page, canonicalUrl) {
	const revision = page.revision
		? `只读公开快照，源修订 ID：${page.revision}。`
		: "只读公开快照。";
	return shell
		.replaceAll("__HI_DOCUMENT_TITLE__", `${escapeHtml(page.title)} - Human Infra Wiki`)
		.replaceAll("__HI_DISPLAY_TITLE__", page.displayTitle)
		.replaceAll("__HI_CONTENT__", page.body)
		.replaceAll("__HI_CATEGORIES__", page.categories || "")
		.replaceAll("__HI_REVISION__", revision)
		.replaceAll("__HI_CANONICAL__", canonicalUrl);
}

function searchBody(query, pages) {
	const normalized = normalizeTitle(query);
	const matches = normalized
		? pages.filter((page) => page.normalized.includes(normalized)).slice(0, 50)
		: [];
	const items = matches
		.map((page) => {
			const href = `/index.php/${encodeURIComponent(page.title.replaceAll(" ", "_"))}`;
			return `<li><a href="${href}">${escapeHtml(page.title)}</a></li>`;
		})
		.join("");
	const result = matches.length
		? `<ul class="mw-search-results">${items}</ul>`
		: "<p>没有找到匹配的快照词条。</p>";
	return {
		title: `搜索：${query}`,
		displayTitle: `搜索：${escapeHtml(query)}`,
		body: `<div class="mw-parser-output"><p>只读快照中的标题搜索结果：</p>${result}</div>`,
		categories: "",
		revision: null,
	};
}

async function renderPage(request, env) {
	const url = new URL(request.url);
	const index = await loadSnapshot(env, request.url);
	const shell = await loadShell(env, request.url);
	const title = requestedTitle(url, index.mainPage);
	if (title === null) {
		return env.ASSETS.fetch(request);
	}

	const normalized = normalizeTitle(title);
	if (normalized === normalizeTitle("Special:Search")) {
		const query = url.searchParams.get("search") || "";
		const page = searchBody(query, index.pages);
		return new Response(
			renderShell(shell, page, `${WIKI_ORIGIN}/index.php?title=Special:Search&search=${encodeURIComponent(query)}`),
			{ headers: { "content-type": "text/html; charset=UTF-8" } }
		);
	}
	if (normalized === normalizeTitle("Special:Random")) {
		const page = index.pages[Math.floor(Math.random() * index.pages.length)];
		return Response.redirect(
			`${WIKI_ORIGIN}/index.php/${encodeURIComponent(page.title.replaceAll(" ", "_"))}`,
			302
		);
	}

	const entry = index.byTitle.get(normalized);
	if (!entry) {
		const body = {
			title: "页面不存在",
			displayTitle: "页面不存在",
			body: `<div class="mw-parser-output"><p>该页面不在当前公开快照中。</p><p><a href="/">返回首页</a></p></div>`,
			categories: "",
			revision: null,
		};
		return new Response(renderShell(shell, body, url.href), {
			status: 404,
			headers: { "content-type": "text/html; charset=UTF-8" },
		});
	}

	const pageResponse = await env.ASSETS.fetch(
		new URL(`/snapshot/pages/${entry.file}`, request.url)
	);
	if (!pageResponse.ok) {
		return new Response("Wiki 页面快照不可用", { status: 503 });
	}
	const page = await pageResponse.json();
	const canonical = `${WIKI_ORIGIN}/index.php/${encodeURIComponent(page.title.replaceAll(" ", "_"))}`;
	return new Response(renderShell(shell, page, canonical), {
		headers: {
			"content-type": "text/html; charset=UTF-8",
			"cache-control": "public, max-age=300",
			"x-robots-tag": "index, follow",
		},
	});
}

export default {
	async fetch(request, env) {
		const url = new URL(request.url);
		if (url.pathname === "/api.php" || url.pathname === "/rest.php") {
			return Response.json(
				{ error: "公开站是只读快照，编辑与 API 仅在本地 MediaWiki 可用。" },
				{ status: 410 }
			);
		}
		try {
			return await renderPage(request, env);
		} catch (error) {
			return new Response(`Wiki 快照读取失败: ${error.message}`, { status: 500 });
		}
	},
};
