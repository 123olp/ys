const { chromium } = require(
    "/usr/local/lib/node_modules/backstopjs/node_modules/playwright"
);

const baseUrl = process.env.WIKI_TEST_URL || "http://127.0.0.1:18782/";
const expectedLanguageCount = 347;

async function main() {
    const browser = await chromium.launch({ headless: true });
    const page = await browser.newPage({
        viewport: { width: 1440, height: 1200 },
        colorScheme: "dark",
    });

    try {
        await page.goto(baseUrl, {
            waitUntil: "domcontentloaded",
            timeout: 30_000,
        });

        const trigger = page.locator("#p-lang-btn-checkbox");
        await trigger.waitFor({ state: "attached", timeout: 15_000 });
        await page.waitForFunction(
            () => window.mw &&
                mw.loader.getState("ext.uls.interface") === "ready",
            null,
            { timeout: 15_000 }
        );

        const sourceLinkCount = await page.locator(
            "#p-lang-btn a.interlanguage-link-target"
        ).count();
        if (sourceLinkCount !== expectedLanguageCount) {
            throw new Error(
                `Vector 语言入口数量错误: expected=${expectedLanguageCount}, ` +
                `actual=${sourceLinkCount}`
            );
        }

        await trigger.click({ force: true });

        const selector = page.locator(".uls-rewrite");
        await selector.waitFor({ state: "visible", timeout: 15_000 });

        const renderedLanguages = page.locator(
            ".uls-rewrite__language-item"
        );
        const renderedLanguageCount = await renderedLanguages.count();
        const uniqueRenderedLanguageCount = await renderedLanguages.evaluateAll(
            (items) => new Set(
                items.map((item) => item.querySelector("a")?.href)
            ).size
        );
        if (uniqueRenderedLanguageCount !== expectedLanguageCount) {
            throw new Error(
                `ULS V2 唯一语言数量错误: expected=${expectedLanguageCount}, ` +
                `actual=${uniqueRenderedLanguageCount}, ` +
                `rendered=${renderedLanguageCount}`
            );
        }

        await selector.screenshot({
            path: "/work/language-selector-open.png",
        });

        await trigger.click({ force: true });
        await selector.waitFor({ state: "hidden", timeout: 5_000 });

        console.log(
            `language selector ok: source=${sourceLinkCount}, ` +
            `unique=${uniqueRenderedLanguageCount}, ` +
            `rendered=${renderedLanguageCount}`
        );
    } finally {
        await browser.close();
    }
}

main().catch((error) => {
    console.error(error);
    process.exit(1);
});
