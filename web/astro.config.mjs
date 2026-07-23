import {defineConfig} from "astro/config";
import mdx from "@astrojs/mdx";
import sitemap from "@astrojs/sitemap";

const base = process.env.SITE_BASE_PATH || "/";

export default defineConfig({
  integrations: [
    mdx(),
    sitemap({
      filter: (page) => !/\.(json|txt)$/.test(new URL(page).pathname)
    })
  ],
  site: "https://tradecatlabs.github.io",
  base,
  devToolbar: {
    enabled: false
  },
  trailingSlash: "always",
  output: "static"
});
