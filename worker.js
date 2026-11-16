const HOSTS = new Map([
  ["www.hawiki.cz", "cs"],
  ["hawiki.cz", "cs"],
  ["hawiki.eu", "eu"],
  ["www.hawiki.eu", "eu"],
]);

function previewSite(request, url) {
  if (!url.hostname.endsWith(".workers.dev")) return null;
  const selected = url.searchParams.get("site");
  if (selected === "cs" || selected === "en") return selected === "cs" ? "cs" : "eu";
  const cookie = request.headers.get("Cookie") || "";
  const match = cookie.match(/(?:^|;\s*)hawiki_preview=(cs|en)(?:;|$)/);
  return match?.[1] === "cs" ? "cs" : "eu";
}

export default {
  async fetch(request, env) {
    const url = new URL(request.url);
    if (url.hostname === "hawiki.cz") {
      url.hostname = "www.hawiki.cz";
      return Response.redirect(url, 308);
    }
    if (url.hostname === "www.hawiki.eu") {
      url.hostname = "hawiki.eu";
      return Response.redirect(url, 308);
    }
    const preview = previewSite(request, url);
    const site = HOSTS.get(url.hostname) || preview;
    if (!site) {
      return new Response("Unknown HAwiki hostname", { status: 421 });
    }

    const selected = url.searchParams.get("site");
    url.searchParams.delete("site");
    url.pathname = `/__sites/${site}${url.pathname}`;
    const assetRequest = new Request(url, request);
    const response = await env.ASSETS.fetch(assetRequest);

    if (preview && (selected === "cs" || selected === "en")) {
      const headers = new Headers(response.headers);
      headers.append("Set-Cookie", `hawiki_preview=${selected}; Path=/; Max-Age=86400; SameSite=Lax; Secure`);
      return new Response(response.body, { status: response.status, statusText: response.statusText, headers });
    }
    return response;
  },
};
