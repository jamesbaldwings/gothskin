# Goth Skin — gothskin.com

A static site. Plain HTML and CSS, no framework, no build step, no dependencies.
Open `index.html` in a browser and it works. Upload the folder to any host and it works.

## Pages

| File | What it is |
|---|---|
| `index.html` | Home. The manifesto carries it while there is no photography. |
| `about.html` | The Idea. The full argument, the working principles and the public promises. |
| `portraits.html` | The gallery. Honest empty state until the first shoot. |
| `be-featured.html` | Application. Opens the visitor's mail app. Nothing is stored here. |
| `consent.html` | Consent and your rights, in plain English. Linked from every footer. |
| `portraits/_template.html` | Copy this to make a profile page. Fill the `[BRACKETS]`. |
| `assets/site.css` | The whole design system. Two colours, two typefaces, no accent. |
| `robots.txt` | Allows search engines, blocks the known AI training crawlers. |

## Adding a portrait

1. Copy `portraits/_template.html` to `portraits/01-name.html`.
2. Put the images in `portraits/images/`.
3. Replace every `[BRACKET]` and swap the placeholder frame for the real `<img>`.
4. On `portraits.html` and `index.html`, change one `<article class="portrait empty">`
   block into a real one: drop the `empty` class, add the image and link it.
5. Add the page to `sitemap.xml`.

## Before this goes live

- [ ] Set the real contact address. It is `hello@gothskin.com` everywhere right now.
      Search and replace across all `.html` files if that is not the address you want.
- [ ] File the intent-to-use trademark application on GOTH SKIN.
- [ ] Replace `assets/og.png` once there is real photography. Link previews matter more
      than almost anything else on the page.

## Deploying

Any static host. No configuration, no environment variables, no server.

**Cloudflare Pages** — connect this repo, leave the build command empty, set the output
directory to `/`. Point gothskin.com at it in Cloudflare DNS.

**Railway** — add a static site service pointed at this repo.

**Anything else** — upload the folder over FTP. It is that kind of site.

## Notes

- The fonts are Bodoni Moda and Archivo, loaded from Google Fonts. Nothing else is
  loaded from anywhere.
- `_build.py` generated these pages and is kept for convenience. You never have to run
  it. Editing the HTML by hand is fine, and if you do, stop using the script or it will
  overwrite your changes.
- Every page carries `noai` and `noimageai` directives and `robots.txt` blocks the known
  training crawlers. This stops polite scrapers only. Serve images at web resolution and
  assume anything published can be copied.
