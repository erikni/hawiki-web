# Projektová konfigurace AI agenta

Tento repozitář používá metodiku
[SDLC-AI v1.2.1](https://github.com/erikni/sdlc-ai/releases/tag/v1.2.1).
Pravidla jsou odkazovaná v pevně připnuté verzi; dokumenty z větve `main`
repozitáře SDLC-AI nejsou pro tento projekt autoritativní.

## Konfigurace

```env
SDLC_AI_VERSION=v1.2.1
GITHUB_OWNER=erikni
REPOSITORY_NAME=hawiki-web
LANG=cs
SITE_URL=https://www.hawiki.cz
DEPLOY_PROVIDER=cloudflare
PREVIEW_URL_PATTERN=*-hawiki-web.gemini77.workers.dev
CLOUDFLARE_CONFIG_PATH=wrangler.jsonc
CLOUDFLARE_TYPE=WORKERS
```

`PREVIEW_URL_PATTERN` je pouze validační vzor. Před schválením mergu vždy
zjistěte a ověřte skutečnou URL konkrétního preview. Secrets, tokeny, ID účtů
a jiné přihlašovací údaje do tohoto souboru nepatří.

## Povinný postup

1. Od první odpovědi používejte češtinu.
2. Určete typ issue podle
   [SDLC-AI v1.2.1](https://github.com/erikni/sdlc-ai/blob/v1.2.1/README.md).
3. Pro `TASK`, `CHORE`, `SPIKE` nebo `BUG` načtěte pouze
   [TASK.md v1.2.1](https://github.com/erikni/sdlc-ai/blob/v1.2.1/TASK.md)
   a postupujte podle něj, dokud nenastane spouštěč zvýšení.
4. Pro `STORY` nebo `EPIC` pokračujte podle
   [ISSUE.md v1.2.1](https://github.com/erikni/sdlc-ai/blob/v1.2.1/ISSUE.md)
   a načtěte jen dokumenty, které tento postup vyžaduje.
5. Git workflow řiďte
   [GIT.md v1.2.1](https://github.com/erikni/sdlc-ai/blob/v1.2.1/GIT.md),
   testování
   [TEST.md v1.2.1](https://github.com/erikni/sdlc-ai/blob/v1.2.1/TEST.md)
   a bezpečnost
   [SECURITY.md v1.2.1](https://github.com/erikni/sdlc-ai/blob/v1.2.1/SECURITY.md).
6. Nasazení řiďte
   [DEPLOY.md v1.2.1](https://github.com/erikni/sdlc-ai/blob/v1.2.1/DEPLOY.md)
   a adaptérem
   [DEPLOY-CF.md v1.2.1](https://github.com/erikni/sdlc-ai/blob/v1.2.1/DEPLOY-CF.md).
7. Do výchozí větve nezapisujte přímo. Issue, feature větev, push a PR
   vytvořte bez dotazu; člověk schvaluje merge konkrétního HEAD SHA.
8. Za pravdu považujte jen ověřený stav GitHubu, CI, preview a produkce.

## Konvence projektu

- Zdrojové články jsou v `content/`; vygenerovaný adresář `dist/` se do
  repozitáře neukládá.
- Sestavení a kontroly spouští `sh build-cloudflare.sh`.
- Preview workflow je `.github/workflows/preview-cloudflare-workers.yml`;
  produkční workflow je `.github/workflows/deploy-cloudflare-workers.yml`.
- Produkční canonical URL je `https://www.hawiki.cz`. Preview URL nesmí být
  použita jako canonical URL ani v sitemapě.
- Obsah článků pište česky, jednoduše a pro netechnické čtenáře. Ověření podle
  dokumentace nerozšiřujte na tvrzení o praktickém testování.

## Změna verze metodiky

Verzi SDLC-AI měňte pouze samostatným issue a pull requestem. V jednom commitu
aktualizujte všechny odkazy na tag v `AGENTS.md` a `README.md`, projděte
release notes nové verze a doložte kontrolu odkazů.
