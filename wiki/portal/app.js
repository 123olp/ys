const portalConfig = window.HUMAN_INFRA_PORTAL || { wikiPort: "18782" };

function wikiBase(language) {
  if (language.origin) {
    return language.origin.replace(/\/$/, "");
  }
  const host = window.location.hostname || "localhost";
  const port = portalConfig.wikiPort ? `:${portalConfig.wikiPort}` : "";
  return `${window.location.protocol}//${host}${port}${language.path || "/"}`.replace(/\/$/, "");
}

function languageStatus(language) {
  return language.status === "available" ? "已开放" : "筹备中";
}

async function loadPageCount(baseUrl) {
  const params = new URLSearchParams({
    action: "query",
    meta: "siteinfo",
    siprop: "statistics",
    format: "json",
    origin: "*"
  });
  const response = await fetch(`${baseUrl}/api.php?${params}`, { mode: "cors" });
  if (!response.ok) {
    throw new Error(`MediaWiki API returned ${response.status}`);
  }
  const payload = await response.json();
  return payload?.query?.statistics?.articles;
}

function renderLanguage(language, list, select) {
  const available = language.status === "available";
  const baseUrl = available ? wikiBase(language) : "";
  const article = document.createElement(available ? "a" : "div");
  article.className = `language-card language-card--${language.status}`;
  if (available) {
    article.href = `${baseUrl}/`;
  } else {
    article.setAttribute("aria-disabled", "true");
  }

  const title = document.createElement("strong");
  title.textContent = language.localName;
  const description = document.createElement("span");
  description.textContent = language.description;
  const meta = document.createElement("small");
  meta.textContent = languageStatus(language);

  article.append(title, description, meta);
  list.append(article);

  if (available) {
    const option = document.createElement("option");
    option.value = language.code;
    option.dataset.baseUrl = baseUrl;
    option.textContent = language.localName;
    select.append(option);

    loadPageCount(baseUrl)
      .then((count) => {
        if (Number.isFinite(count)) {
          meta.textContent = `${count.toLocaleString("zh-CN")} 篇内容词条`;
        }
      })
      .catch(() => {
        meta.textContent = "已开放";
      });
  }
}

async function initializePortal() {
  const response = await fetch("languages.json");
  if (!response.ok) {
    throw new Error("Language registry unavailable");
  }
  const registry = await response.json();
  const list = document.querySelector("#language-list");
  const select = document.querySelector("#search-language");

  registry.languages.forEach((language) => renderLanguage(language, list, select));

  const zh = registry.languages.find((language) => language.code === "zh" && language.status === "available");
  if (zh) {
    document.querySelector("#about-link").href =
      `${wikiBase(zh)}/index.php?title=${encodeURIComponent("Human Infra:关于")}`;
  }
}

document.querySelector("#search-form").addEventListener("submit", (event) => {
  event.preventDefault();
  const query = document.querySelector("#search-input").value.trim();
  const selected = document.querySelector("#search-language").selectedOptions[0];
  if (!query || !selected) {
    return;
  }
  const url = new URL(`${selected.dataset.baseUrl}/index.php`);
  url.searchParams.set("title", "Special:Search");
  url.searchParams.set("search", query);
  window.location.assign(url);
});

initializePortal().catch(() => {
  document.querySelector("#language-list").textContent = "语言注册表暂时不可用。";
});
