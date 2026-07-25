const stabilizePage = require("./onReady");

const contentFixture = `
  <div class="mp-2012-text">
  <h2>标准栏目内容</h2>
  <p><b><a href="#">标准链接</a></b>用于验证首页模板的字体、间距、颜色与边界。</p>
  <ul>
    <li>第一条标准内容用于固定排版高度。</li>
    <li>第二条标准内容用于验证列表缩进。</li>
  </ul>
  <div class="mp-2012-block-nav-footer hlist"><a href="#">更多内容</a></div>
  </div>
`;

const captureSelectors = [
  "#mp-2012-banner",
  "#mp-2012-column-feature-block",
  "#mp-2012-column-dyk-block",
  "#mp-2012-column-good-block",
  "#mp-2012-column-featurepic-block",
  "#mp-2012-column-right-block-a",
  "#mp-2012-column-right-block-b",
  "#mp-2012-column-right-block-c",
  "#mp-2012-links",
  "#mp-2012-sisters",
];

module.exports = async (page) => {
  await stabilizePage(page);
  await page.keyboard.press("Escape");
  await page.evaluate(
    ({ fixture, selectors }) => {
      const root = document.querySelector("#mp-2012");
      if (root) {
        const rect = root.getBoundingClientRect();
        const offsetX = rect.x - Math.round(rect.x);
        const offsetY = rect.y - Math.round(rect.y);
        root.style.transform = `translate(${-offsetX}px, ${-offsetY}px)`;
      }

      /*
       * 组件截图不得包含 Vector 页面壳或按实验桶出现的浮层。除明确类名外，
       * 统一移除模板根节点之外的 dialog、menu、fixed 与 sticky 元素。
       */
      document.querySelectorAll("body *").forEach((element) => {
        if (!root || root.contains(element)) {
          return;
        }
        const style = window.getComputedStyle(element);
        const isOverlay =
          element.matches(
            '[role="dialog"], [role="menu"], [aria-modal="true"], ' +
              ".oo-ui-windowManager, .oo-ui-window, .uls-language-list, " +
              ".uls-settings-ui",
          ) || ["fixed", "sticky"].includes(style.position);
        if (isOverlay) {
          element.style.setProperty("display", "none", "important");
        }
      });

      const hide = (selector) => {
        const element = document.querySelector(selector);
        if (element) {
          element.style.visibility = "hidden";
        }
      };
      const replace = (selector, html) => {
        const element = document.querySelector(selector);
        if (element) {
          element.innerHTML = html;
        }
      };

      hide("#mp-2012-banner-logo");
      hide("#mp-2012-banner-title");
      hide("#mp-2012-banner-intro");

      [
        "#mp-2012-column-featurepic-block",
        "#mp-2012-column-feature-block",
        "#mp-2012-column-dyk-block",
        "#mp-2012-column-good-block",
        "#mp-2012-column-itn-block",
        "#mp-2012-column-otd-block",
        "#mp-2012-column-uptrends-block",
        "#mp-2012-column-participate-block",
        "#mp-2012-column-tips-block",
      ].forEach((selector) =>
        replace(selector, `<h2>标准栏目</h2>${fixture}`),
      );

      replace("#mp-2012-links", fixture);
      replace("#mp-2012-sisters", fixture);

      /*
       * BackstopJS 按选择器裁切截图。相同组件若因不同 Vector 页面壳落在
       * 不同小数像素坐标，Chromium 会生成不同的文本抗锯齿像素。逐个把
       * 截图边界对齐到整数像素，只消除壳层坐标噪音，不改变组件尺寸或布局。
       */
      selectors.forEach((selector) => {
        const element = document.querySelector(selector);
        if (!element) {
          return;
        }
        const rect = element.getBoundingClientRect();
        const offsetX = rect.x - Math.round(rect.x);
        const offsetY = rect.y - Math.round(rect.y);
        element.style.transform = `translate(${-offsetX}px, ${-offsetY}px)`;
      });
    },
    { fixture: contentFixture, selectors: captureSelectors },
  );
  await page.evaluate(() => document.fonts.ready);
};
