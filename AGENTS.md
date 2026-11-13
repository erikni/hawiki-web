# Pokyny pro agenty

## Kontext repozitáře pro GIT.md

Při práci podle `GIT.md` používejte následující projektové hodnoty. Jde o veřejný kontext projektu, nikoli o přihlašovací údaje nebo secrets.

```env
GITHUB_USERNAME=erikni
REPOSITORY_NAME=hawiki-web
SITE_URL=https://www.hawiki.cz
PREVIEW_URL=*-hawiki-web.gemini77.workers.dev
CF_WORKER_URI=hawiki-web
```

`PREVIEW_URL` je vzor adresy. Před předložením změny ke schválení vždy zjistěte a ověřte skutečnou URL konkrétního preview; wildcard není odkaz na nasazený náhled.
