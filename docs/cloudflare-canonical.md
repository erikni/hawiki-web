# Canonical hostname: změna v Cloudflare

Generátor používá `https://www.hawiki.cz`. Tento údaj nezajišťuje HTTP redirect. Cloudflare Pages deployment je nakonfigurován v GitHub Actions; doménové redirecty nejsou v repozitáři. Stav živých redirectů se nepodařilo ověřit: proxy vrací CONNECT 500. Nejde o doloženou chybu serveru HA wiki.

V Cloudflare zóně **hawiki.cz → Rules → Redirect Rules → Single Redirects** vytvořte pravidlo před obecnými redirecty. Domény musí procházet proxovanou Cloudflare zónou a HTTPS varianta bez www musí mít platný certifikát.

Podmínka:

```text
(http.host eq "hawiki.cz") or
(http.host eq "www.hawiki.cz" and not ssl)
```

Dynamická cílová URL:

```text
concat("https://www.hawiki.cz", http.request.uri.path)
```

Status: **301**. **Preserve query string: zapnout**. Canonical HTTPS/www varianta není podmínkou zachycena, takže pravidlo nevytváří smyčku. Při současném zapnutí Always Use HTTPS může vzniknout další krok; pravidla a jejich pořadí zkontrolujte na celé zóně, aby každá varianta ideálně vedla přímo na HTTPS/www.

Po nastavení zkontrolujte pomocí HTTP klienta bez automatického sledování redirectu:

| Vstup | Status | Location |
| --- | --- | --- |
| http://hawiki.cz/navody/?x=1 | 301 | https://www.hawiki.cz/navody/?x=1 |
| https://hawiki.cz/navody/?x=1 | 301 | https://www.hawiki.cz/navody/?x=1 |
| http://www.hawiki.cz/navody/?x=1 | 301 | https://www.hawiki.cz/navody/?x=1 |
| https://www.hawiki.cz/navody/?x=1 | 200 | bez redirectu |

Potom ověřte i kořen domény, hlubší cestu a více query parametrů. Canonical v HTML nesmí query obsahovat. Tato konfigurace je návrh; nebyla aplikována v účtu Cloudflare.

Zdroj: [Cloudflare: nastavení Single Redirects](https://developers.cloudflare.com/rules/url-forwarding/single-redirects/settings/).
