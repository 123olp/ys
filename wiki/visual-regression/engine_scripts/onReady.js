module.exports = async (page) => {
  await page.evaluate(async () => {
    await document.fonts.ready;
    const pendingImages = Array.from(document.images)
      .filter((image) => !image.complete)
      .map(
        (image) =>
          new Promise((resolve) => {
            image.addEventListener("load", resolve, { once: true });
            image.addEventListener("error", resolve, { once: true });
          }),
      );
    await Promise.race([
      Promise.all(pendingImages),
      new Promise((resolve) => window.setTimeout(resolve, 5000)),
    ]);

    const style = document.createElement("style");
    style.textContent = [
      "*, *::before, *::after {",
      "  animation: none !important;",
      "  caret-color: transparent !important;",
      "  transition: none !important;",
      "}",
      /*
       * 中文维基百科会按地域、会话和实验桶异步显示 ULS、CentralNotice
       * 等页面壳浮层。它们不属于首页模板，必须从模板截图中稳定排除。
       */
      "#centralNotice,",
      ".centralNotice,",
      ".uls-menu,",
      ".uls-dialog,",
      ".mwe-popups,",
      ".mw-notification-area,",
      ".vector-sticky-header,",
      "#scrollUpButton-zhwiki,",
      "#scrollDownButton-zhwiki {",
      "  display: none !important;",
      "}",
    ].join("\n");
    document.head.appendChild(style);
    window.scrollTo(0, 0);
  });
};
