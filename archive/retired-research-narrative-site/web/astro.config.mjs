import {defineConfig} from "astro/config";
import mdx from "@astrojs/mdx";
import sitemap from "@astrojs/sitemap";

const base = process.env.SITE_BASE_PATH || "/";
const site =
  process.env.PUBLIC_SITE_ORIGIN ||
  process.env.CF_PAGES_URL ||
  "https://human-infra.pages.dev";

export default defineConfig({
  integrations: [
    mdx(),
    sitemap({
      filter: (page) => !/\.(json|txt)$/.test(new URL(page).pathname)
    })
  ],
  site,
  base,
  devToolbar: {
    enabled: false
  },
  trailingSlash: "always",
  output: "static"
});
