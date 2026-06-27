import {defineConfig} from "astro/config";
import mdx from "@astrojs/mdx";

export default defineConfig({
  integrations: [mdx()],
  site: "https://tradecatlabs.github.io/human_infra",
  devToolbar: {
    enabled: false
  },
  output: "static"
});
