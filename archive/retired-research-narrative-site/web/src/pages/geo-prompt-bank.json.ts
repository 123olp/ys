import type {APIRoute} from "astro";
import promptBank from "../data/geo-monitoring-prompt-bank.json";
import {publicUrl} from "../lib/site";

export const prerender = true;

export const GET: APIRoute = () =>
  new Response(
    JSON.stringify(
      {
        ...promptBank,
        canonicalUrl: publicUrl("/geo-prompt-bank.json")
      },
      null,
      2
    ),
    {headers: {"Content-Type": "application/json; charset=utf-8"}}
  );
