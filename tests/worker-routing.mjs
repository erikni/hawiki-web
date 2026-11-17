import assert from "node:assert/strict";
import { readFile } from "node:fs/promises";

const source = await readFile(new URL("../worker.js", import.meta.url), "utf8");
const moduleUrl = `data:text/javascript;charset=utf-8,${encodeURIComponent(source)}`;
const { default: worker } = await import(moduleUrl);

const seen = [];
const env = {
  ASSETS: {
    async fetch(request) {
      seen.push(new URL(request.url).pathname);
      return new Response("asset", { status: 200 });
    },
  },
};

async function route(url, headers = {}) {
  seen.length = 0;
  const response = await worker.fetch(new Request(url, { headers }), env);
  return { response, path: seen[0] };
}

let result = await route("https://www.hawiki.cz/navody/");
assert.equal(result.response.status, 200);
assert.equal(result.path, "/__sites/cs/navody/");

result = await route("https://hawiki.eu/getting-started/");
assert.equal(result.response.status, 200);
assert.equal(result.path, "/__sites/eu/getting-started/");

result = await route("https://hawiki.cz/navody/?from=apex");
assert.equal(result.response.status, 308);
assert.equal(result.response.headers.get("location"), "https://www.hawiki.cz/navody/?from=apex");

result = await route("https://www.hawiki.eu/getting-started/");
assert.equal(result.response.status, 308);
assert.equal(result.response.headers.get("location"), "https://hawiki.eu/getting-started/");

result = await route("https://preview.hawiki-web.workers.dev/?site=cs");
assert.equal(result.path, "/__sites/cs/");
assert.match(result.response.headers.get("set-cookie"), /hawiki_preview=cs/);

result = await route("https://preview.hawiki-web.workers.dev/assets/style.css", {
  Cookie: "hawiki_preview=en",
});
assert.equal(result.path, "/__sites/eu/assets/style.css");

result = await route("https://unrelated.example/");
assert.equal(result.response.status, 421);
assert.equal(result.path, undefined);

console.log("Worker hostname and preview routing verified.");
