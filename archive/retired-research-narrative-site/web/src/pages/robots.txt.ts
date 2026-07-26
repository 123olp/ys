import type {APIRoute} from "astro";
import {publicUrl} from "../lib/site";

export const prerender = true;

export const GET: APIRoute = () =>
  new Response(
    [
      "User-agent: *",
      "Allow: /",
      "",
      `Sitemap: ${publicUrl("/sitemap-index.xml")}`,
      `Host: ${new URL(publicUrl()).host}`,
      ""
    ].join("\n"),
    {headers: {"Content-Type": "text/plain; charset=utf-8"}}
  );
