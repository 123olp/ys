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

module.exports = async (page) => {
  await stabilizePage(page);
  await page.evaluate((fixture) => {
    const root = document.querySelector("#mp-2012");
    if (root) {
      const rect = root.getBoundingClientRect();
      const offsetX = rect.x - Math.round(rect.x);
      const offsetY = rect.y - Math.round(rect.y);
      root.style.transform = `translate(${-offsetX}px, ${-offsetY}px)`;
    }

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
    ].forEach((selector) => replace(selector, `<h2>标准栏目</h2>${fixture}`));

    replace("#mp-2012-links", fixture);
    replace("#mp-2012-sisters", fixture);
  }, contentFixture);
};
