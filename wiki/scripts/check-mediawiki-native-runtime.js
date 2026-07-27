const { chromium } = require(
    "/usr/local/lib/node_modules/backstopjs/node_modules/playwright"
);

const baseUrl = process.env.MEDIAWIKI_TEST_URL ||
    "http://127.0.0.1:18782/wiki/Wikipedia:%E9%A6%96%E9%A1%B5";

function assert(condition, message) {
    if (!condition) throw new Error(message);
}

async function main() {
    const browser = await chromium.launch({ headless: true });
    const context = await browser.newContext({
        viewport: { width: 2048, height: 1152 },
        colorScheme: "dark",
    });
    const page = await context.newPage();
    const requests = [];
    const errors = [];
    page.on("request", (request) => requests.push(request.url()));
    page.on("console", (message) => {
        if (message.type() === "error") errors.push(message.text());
    });
    page.on("pageerror", (error) => errors.push(error.message));

    try {
        await page.goto(baseUrl, {
            waitUntil: "domcontentloaded",
            timeout: 30_000,
        });
        await page.locator(
            "#vector-appearance input[type='radio']"
        ).first().waitFor({ state: "attached", timeout: 30_000 });

        assert(
            await page.locator(
                "#vector-appearance input[type='radio']"
            ).count() === 8,
            "MediaWiki 原生 Vector 外观控件不是 8 个"
        );
        assert(
            requests.some((url) =>
                url.includes("/load.php") &&
                (
                    url.includes("skins.vector.js") ||
                    url.includes("skins.vector.clientPreferences")
                )
            ),
            "页面没有通过 ResourceLoader 加载 Vector 原生模块"
        );
        assert(
            !requests.some((url) =>
                url.includes("/assets/vector-client-preferences.js")
            ),
            "页面加载了项目自写 Vector 适配器"
        );

        const largeText = page.locator(
            "#skin-client-pref-vector-feature-custom-font-size-value-2"
        );
        await largeText.check();
        await page.waitForFunction(() =>
            document.documentElement.classList.contains(
                "vector-feature-custom-font-size-clientpref-2"
            )
        );
        await page.reload({ waitUntil: "domcontentloaded" });
        await largeText.waitFor({ state: "attached" });
        assert(await largeText.isChecked(), "MediaWiki 没有持久化字号偏好");

        const appearance = page.locator("#vector-appearance");
        const unpin = appearance.locator(
            ".vector-pinnable-header-unpin-button"
        );
        await unpin.click();
        await page.waitForFunction(() =>
            document.querySelector("#vector-appearance")?.parentElement?.id
                === "vector-appearance-unpinned-container"
        );

        await page.locator("#vector-appearance-dropdown-checkbox").check({
            force: true,
        });
        const pin = appearance.locator(".vector-pinnable-header-pin-button");
        await pin.click();
        await page.waitForFunction(() =>
            document.querySelector("#vector-appearance")?.parentElement?.id
                === "vector-appearance-pinned-container"
        );

        await page.setViewportSize({ width: 1024, height: 1152 });
        await page.waitForFunction(() =>
            document.querySelector("#vector-appearance")?.parentElement?.id
                === "vector-appearance-unpinned-container"
        );
        await page.setViewportSize({ width: 2048, height: 1152 });
        await page.waitForFunction(() =>
            document.querySelector("#vector-appearance")?.parentElement?.id
                === "vector-appearance-pinned-container"
        );

        assert(errors.length === 0, `浏览器错误: ${errors.join(" | ")}`);
        await page.screenshot({
            path: "/work/mediawiki-native-vector.png",
            fullPage: true,
        });
        console.log("MediaWiki/Vector native runtime contract: PASS");
    } finally {
        await browser.close();
    }
}

main().catch((error) => {
    console.error(error);
    process.exit(1);
});
