const { chromium } = require(
    "/usr/local/lib/node_modules/backstopjs/node_modules/playwright"
);

const baseUrl = process.env.WIKI_TEST_URL || "http://127.0.0.1:18790/";
function assert(condition, message) {
    if (!condition) {
        throw new Error(message);
    }
}

async function snapshot(page) {
    return page.evaluate(() => {
        const root = document.documentElement;
        const appearance = document.querySelector("#vector-appearance");
        const header = appearance?.querySelector(".vector-pinnable-header");
        const main = document.querySelector("#mp-2012");
        const pin = appearance?.querySelector(
            ".vector-pinnable-header-pin-button"
        );
        const unpin = appearance?.querySelector(
            ".vector-pinnable-header-unpin-button"
        );
        return {
            rootClass: root.className,
            parentId: appearance?.parentElement?.id || null,
            headerClass: header?.className || null,
            savedPinnedState: header?.dataset.savedPinnedState || null,
            pinDisplay: pin ? getComputedStyle(pin).display : null,
            unpinDisplay: unpin ? getComputedStyle(unpin).display : null,
            mainWidth: main?.getBoundingClientRect().width || 0,
            scrollWidth: root.scrollWidth,
            clientWidth: root.clientWidth,
        };
    });
}

async function main() {
    const browser = await chromium.launch({ headless: true });
    const page = await browser.newPage({
        viewport: { width: 2048, height: 1152 },
        colorScheme: "dark",
    });
    const consoleErrors = [];
    page.on("console", (message) => {
        if (message.type() === "error") consoleErrors.push(message.text());
    });
    page.on("pageerror", (error) => consoleErrors.push(error.message));
    try {
        await page.goto(baseUrl, {
            waitUntil: "domcontentloaded",
            timeout: 30_000,
        });

        assert(
            await page.locator("#vector-appearance input[type='radio']").count()
                === 8,
            "Vector 外观偏好控件不是 8 个"
        );

        let state = await snapshot(page);
        assert(
            state.parentId === "vector-appearance-pinned-container",
            `桌面初始容器错误: ${state.parentId}`
        );
        assert(
            state.rootClass.includes(
                "vector-feature-appearance-pinned-clientpref-1"
            ),
            "桌面初始状态缺少 pinned-clientpref-1"
        );
        assert(
            state.unpinDisplay === "inline-block",
            `“隐藏”按钮不可见: display=${state.unpinDisplay}`
        );
        assert(
            await page.locator(
                "#vector-appearance .vector-pinnable-header-unpin-button"
            ).getAttribute("aria-label") === "隐藏外观",
            "“隐藏”按钮缺少官方 ARIA 标签"
        );
        const pinnedWidth = state.mainWidth;

        await page.locator(
            "#vector-appearance .vector-pinnable-header-unpin-button"
        ).click();
        await page.waitForFunction(() =>
            document.querySelector("#vector-appearance")?.parentElement?.id
                === "vector-appearance-unpinned-container"
        );
        state = await snapshot(page);
        assert(
            state.rootClass.includes(
                "vector-feature-appearance-pinned-clientpref-0"
            ),
            "隐藏后缺少 pinned-clientpref-0"
        );
        assert(
            state.savedPinnedState === "false",
            `隐藏状态未记录: ${state.savedPinnedState}`
        );
        assert(
            state.mainWidth > pinnedWidth + 100,
            `隐藏后正文未扩宽: before=${pinnedWidth}, after=${state.mainWidth}`
        );

        await page.reload({ waitUntil: "domcontentloaded" });
        state = await snapshot(page);
        assert(
            state.parentId === "vector-appearance-unpinned-container",
            "刷新后没有保持隐藏状态"
        );

        await page.locator("#vector-appearance-dropdown-checkbox").click({
            force: true,
        });
        const pinButton = page.locator(
            "#vector-appearance .vector-pinnable-header-pin-button"
        );
        await pinButton.waitFor({ state: "visible" });
        assert(
            await pinButton.getAttribute("aria-label") ===
                "将外观移至侧栏",
            "“移至侧栏”按钮缺少官方 ARIA 标签"
        );
        await pinButton.click();
        await page.waitForFunction(() =>
            document.querySelector("#vector-appearance")?.parentElement?.id
                === "vector-appearance-pinned-container"
        );

        await page.reload({ waitUntil: "domcontentloaded" });
        state = await snapshot(page);
        assert(
            state.parentId === "vector-appearance-pinned-container",
            "刷新后没有保持固定状态"
        );

        await page.setViewportSize({ width: 1024, height: 1152 });
        await page.waitForFunction(() =>
            document.querySelector("#vector-appearance")?.parentElement?.id
                === "vector-appearance-unpinned-container"
        );
        state = await snapshot(page);
        assert(
            state.rootClass.includes(
                "vector-feature-appearance-pinned-clientpref-0"
            ),
            "窄屏没有进入 unpinned 状态"
        );
        assert(
            state.scrollWidth === state.clientWidth,
            `窄屏出现横向溢出: scroll=${state.scrollWidth}, ` +
                `client=${state.clientWidth}`
        );

        await page.setViewportSize({ width: 2048, height: 1152 });
        await page.waitForFunction(() =>
            document.querySelector("#vector-appearance")?.parentElement?.id
                === "vector-appearance-pinned-container"
        );
        assert(consoleErrors.length === 0, `浏览器错误: ${consoleErrors}`);
        await page.screenshot({
            path: "/work/vector-appearance-pinning.png",
            fullPage: true,
        });
        console.log("vector appearance contract ok");
    } finally {
        await browser.close();
    }
}

main().catch((error) => {
    console.error(error);
    process.exit(1);
});
