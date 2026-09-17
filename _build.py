# Generates the static pages. Run: python3 _build.py
# The output is plain HTML with no dependencies. This file is a convenience,
# not a build step you need in order to deploy.
import os, html

SITE = "Goth Skin"
DESC = "A visual exploration of the beauty we find in darkness. In skin, in nature, in art and in ourselves."
URL  = "https://gothskin.com"
EMAIL = "hello@gothskin.com"

FONTS = ('<link rel="preconnect" href="https://fonts.googleapis.com">'
 '<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>'
 '<link rel="stylesheet" href="https://fonts.googleapis.com/css2?'
 'family=Bodoni+Moda:ital,opsz,wght@0,6..96,400;0,6..96,500;1,6..96,400&'
 'family=Archivo:wght@400;500;600&display=swap">')

NAV = [("Portraits","portraits.html"),("The Idea","about.html"),
       ("Be Featured","be-featured.html")]

def head(title, desc, path, depth=0):
    up = "../"*depth
    return f"""<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>{html.escape(title)}</title>
<meta name="description" content="{html.escape(desc)}">
<link rel="canonical" href="{URL}/{path}">
<meta property="og:type" content="website">
<meta property="og:title" content="{html.escape(title)}">
<meta property="og:description" content="{html.escape(desc)}">
<meta property="og:image" content="{URL}/assets/og.png">
<meta property="og:url" content="{URL}/{path}">
<meta name="twitter:card" content="summary_large_image">
<meta name="robots" content="index,follow,noai,noimageai">
<link rel="icon" href="{up}assets/favicon-32.png" sizes="32x32">
<link rel="icon" href="{up}assets/favicon-512.png" sizes="512x512">
<link rel="apple-touch-icon" href="{up}assets/apple-touch-icon.png">
{FONTS}
<link rel="stylesheet" href="{up}assets/site.css">
</head>
<body>
<a class="skip" href="#main">Skip to content</a>
<div class="wrap">
"""

def nav(current, depth=0):
    up = "../"*depth
    parts = []
    for n, h in NAV:
        cur = ' aria-current="page"' if h == current else ''
        parts.append('<li><a href="%s%s"%s>%s</a></li>' % (up, h, cur, html.escape(n)))
    items = "".join(parts)
    return f"""<nav class="nav">
  <a class="mark" href="{up}index.html">GOTH SKIN</a>
  <ul>{items}</ul>
</nav>
<main id="main">
"""

def join(depth=0):
    up = "../"*depth
    return f"""</main>
<div class="join">
  <div>
    <h2>Join Goth Skin</h2>
    <p>New portraits, new writing and studio dates, before they go anywhere else.</p>
  </div>
  <div class="btns">
    <a class="btn" href="mailto:{EMAIL}?subject=Join%20Goth%20Skin">Join by email</a>
  </div>
</div>
"""

def foot(depth=0):
    up = "../"*depth
    return f"""<footer>
  <span class="bod" style="font-size:13px;letter-spacing:.22em;text-transform:none;color:var(--ink)">GOTH SKIN</span>
  <span class="links">
    <a href="{up}consent.html">Consent and your rights</a>
    <a href="mailto:{EMAIL}?subject=Removal%20request">Request removal</a>
    <a href="mailto:{EMAIL}">Contact</a>
  </span>
</footer>
</div>
</body>
</html>
"""

def page(fn, title, desc, current, body, depth=0):
    out = head(title, desc, fn, depth) + nav(current, depth) + body + join(depth) + foot(depth)
    path = fn if depth==0 else fn
    os.makedirs(os.path.dirname(path) or ".", exist_ok=True)
    open(path,"w",encoding="utf-8").write(out)
    print("wrote", path)

MANIFESTO = """  <div class="manifesto">
    <p>Darkness is celebrated when it is chosen and feared when it is inherent.</p>
    <p>Goths adopt it and are called elegant, mysterious, powerful, and they are.</p>
    <p>People born with it get the opposite reading from the same vocabulary.</p>
  </div>
"""

EMPTY_PORTRAIT = """    <article class="portrait empty">
      <div class="frame"></div><div class="rule"></div>
      <p class="nm bod">Not photographed yet</p>
      <p class="meta">Casting now</p>
    </article>
"""

# ---------------------------------------------------------------- home
page("index.html", "Goth Skin — Dark by Nature", DESC, "index.html", f"""
{MANIFESTO}

<section class="plain" style="border-top:1px solid var(--rule)">
  <div class="grid">
    <p class="lab">What this is</p>
    <div class="body">
      <p class="lead">Goth Skin is a visual exploration of the beauty we find in darkness. In skin, in nature, in art and in ourselves.</p>
      <p>It is not an argument. It is a body of photographs, made carefully, of people who agreed to be in them.</p>
      <p><a href="about.html" style="border-bottom:1px solid var(--ink);padding-bottom:2px;font-size:11.5px;font-weight:600;letter-spacing:.17em;text-transform:uppercase">Read the idea</a></p>
    </div>
  </div>
</section>

<section>
  <div style="display:flex;align-items:baseline;justify-content:space-between;gap:20px;flex-wrap:wrap;margin-bottom:34px">
    <p class="lab">The portraits</p>
    <a href="portraits.html" style="font-size:11px;font-weight:600;letter-spacing:.17em;text-transform:uppercase;border-bottom:1px solid var(--ink);padding-bottom:2px">See all</a>
  </div>
  <div class="portraits">
{EMPTY_PORTRAIT}{EMPTY_PORTRAIT}{EMPTY_PORTRAIT}{EMPTY_PORTRAIT}  </div>
  <p style="margin-top:34px;color:var(--muted);font-size:15px">
    The first shoot has not happened yet. These four frames are the first four
    people, and we have not met them.
  </p>
</section>

<div class="cta">
  <h1 class="bod">This could be you.</h1>
  <p>You do not need to be a model, an influencer, goth or known to anyone at all. Interesting people and honest stories are the whole requirement.</p>
  <div class="btns" style="justify-content:center">
    <a class="btn" href="be-featured.html">Apply to be featured</a>
  </div>
</div>
""")

# ---------------------------------------------------------------- about
page("about.html", "The Idea — Goth Skin", DESC, "about.html", f"""
<div style="text-align:center;padding-block:56px 0">
  <h1 class="bod" style="letter-spacing:.06em">GOTH SKIN</h1>
  <p class="lab" style="letter-spacing:.46em;margin-top:20px;max-width:none">Dark by Nature</p>
</div>

{MANIFESTO}

<section>
  <div class="grid">
    <p class="lab">What this is</p>
    <div class="body">
      <p class="lead">Goth Skin is a visual exploration of the beauty we find in darkness. In skin, in nature, in art and in ourselves.</p>
      <p>It is not an argument. It is a body of photographs, made carefully, of people who agreed to be in them.</p>
    </div>
  </div>
</section>

<section>
  <div class="grid">
    <p class="lab">Dark by nature</p>
    <div class="body">
      <p>Nature means two things here, and this work lives where they meet.</p>
      <div class="pair">
        <div><h3>Inherent</h3><p>Dark skin. Dark fur and feathers. Night, obsidian, deep water, black flowers. Darkness nobody decided on.</p></div>
        <div><h3>Chosen</h3><p>Darkness made into a language by artists, designers, writers and musicians across a century of work.</p></div>
      </div>
      <p><strong>Both are beautiful. Only one of them has ever had to prove it.</strong></p>
    </div>
  </div>
</section>

<section>
  <div class="grid">
    <p class="lab">How we work</p>
    <div class="body">
      <ul class="marks">
        <li><b>Everyone has a name.</b> Every person we photograph is named and tells their own story in their own words. Nobody here is a composition.</li>
        <li><b>You do not have to be goth.</b> Goth gives us part of the visual vocabulary and none of the entry requirements. A woman in a white dress beside a raven can say this better than head to toe black.</li>
        <li><b>The person in the frame sets the terms.</b> What we publish, what stays out, what city we name and what we never mention. Decided by them, before the shutter.</li>
        <li><b>We do not explain the pictures.</b> If an image needs a caption to make its case, it is the wrong image.</li>
      </ul>
    </div>
  </div>
</section>

<section>
  <div class="grid">
    <p class="lab">What we will never do</p>
    <div class="body">
      <div class="panel">
        <ul class="marks">
          <li>Price the people in these pictures out of anything we make.</li>
          <li>Take a sponsor who gets a say in who is photographed.</li>
          <li>Let what we sell decide what we publish.</li>
          <li>Keep a portrait up after the person asks us to take it down. No reason required, no questions asked.</li>
        </ul>
        <p class="note">These are easy promises to make now and close to impossible to make later, once there is money arguing the other way. That is exactly why they are written down here, in public, before there is any.</p>
      </div>
    </div>
  </div>
</section>

<div class="cta">
  <h1 class="bod">This could be you.</h1>
  <p>You do not need to be a model, an influencer, goth or known to anyone at all.</p>
  <div class="btns" style="justify-content:center">
    <a class="btn" href="be-featured.html">Apply to be featured</a>
    <a class="btn ghost" href="portraits.html">See the portraits</a>
  </div>
</div>
""")

# ---------------------------------------------------------------- portraits
page("portraits.html", "Portraits — Goth Skin",
     "Every person Goth Skin has photographed, in the order we met them.",
     "portraits.html", f"""
<section class="plain" style="padding-block:clamp(48px,7vw,76px) clamp(30px,4vw,44px)">
  <h1 class="bod">The Portraits</h1>
  <p style="margin-top:20px">Everyone we have photographed and sat down with, in the order we met them. The archive grows by two a month once it starts.</p>
</section>

<section>
  <div class="portraits">
{EMPTY_PORTRAIT}{EMPTY_PORTRAIT}{EMPTY_PORTRAIT}{EMPTY_PORTRAIT}{EMPTY_PORTRAIT}{EMPTY_PORTRAIT}  </div>
</section>

<section>
  <div class="panel">
    <h2 style="font-size:clamp(1.3rem,3vw,1.8rem)">Nothing here yet, and that is the honest version.</h2>
    <p style="margin-top:14px">The first shoot has not happened. Rather than fill this page with stock photography or
    somebody else's work, it stays empty until there is something real to put in it. Every frame above
    is a person we have not met.</p>
    <p class="note">If you want to be one of them, the door is below and it is open.</p>
  </div>
</section>

<div class="cta">
  <h1 class="bod">Your portrait belongs here.</h1>
  <p>We are casting the first batch now.</p>
  <div class="btns" style="justify-content:center">
    <a class="btn" href="be-featured.html">Apply to be featured</a>
  </div>
</div>
""")

# ---------------------------------------------------------------- be featured
page("be-featured.html", "Be Featured — Goth Skin",
     "Apply to be photographed by Goth Skin. You do not need to be a model, an influencer or known to anyone.",
     "be-featured.html", f"""
<section class="plain" style="padding-block:clamp(48px,7vw,76px) clamp(30px,4vw,44px)">
  <h1 class="bod">Be Featured</h1>
  <p class="lead" style="margin-top:22px">You do not need to be a model, an influencer, goth or known to anyone at all. Interesting people and honest stories are the whole requirement.</p>
</section>

<section>
  <div class="grid">
    <p class="lab">How it works</p>
    <div class="body">
      <ul class="marks">
        <li><b>You email us.</b> Use the form below, which opens your mail app with everything laid out. We read every one.</li>
        <li><b>We talk first.</b> Before any camera comes out, we agree what gets published, what stays private and what we never mention.</li>
        <li><b>Then we shoot.</b> Your own clothes. Your own face. An afternoon, not a full day.</li>
        <li><b>You can change your mind.</b> At any point, including after it is published. No reason required.</li>
      </ul>
      <p style="margin-top:22px"><strong>Do not send photographs in your first email.</strong> Send links or a few words instead. We will ask for images once we have spoken, so that nothing of yours is sitting in an inbox before you have decided anything.</p>
      <p>Eighteen and over only, for now.</p>
    </div>
  </div>
</section>

<section>
  <div class="grid">
    <p class="lab">Apply</p>
    <div class="body">
      <form id="apply">
        <div class="field">
          <label for="name">Name, or the name you use publicly</label>
          <input type="text" id="name" name="name" autocomplete="name" required>
        </div>
        <div class="field">
          <label for="where">Where you are</label>
          <input type="text" id="where" name="where" placeholder="City and state, or just the region">
          <p class="hint">We only publish what you tell us to publish. You can give a region and nothing more.</p>
        </div>
        <div class="field">
          <label for="links">A link or two, if you have them</label>
          <input type="text" id="links" name="links" placeholder="Instagram, a portfolio, anything at all">
          <p class="hint">Optional. Plenty of the most interesting people have no links.</p>
        </div>
        <div class="field">
          <label for="style">How you would describe how you look and dress</label>
          <textarea id="style" name="style"></textarea>
        </div>
        <div class="field">
          <label for="story">Something about you</label>
          <textarea id="story" name="story" placeholder="What you listen to, what you make, what you have worn for ten years, what people get wrong about you. Anything true."></textarea>
        </div>
        <div class="check">
          <input type="checkbox" id="age" name="age" required>
          <label for="age">I am eighteen or over.</label>
        </div>
        <div class="check">
          <input type="checkbox" id="consent" name="consent" required>
          <label for="consent">I understand Goth Skin will contact me by email about this, and that nothing is agreed and nothing is published until I say so in writing.</label>
        </div>
        <button class="btn" type="submit">Send application</button>
        <p class="hint" style="margin-top:16px">This opens your email app with your answers filled in. Nothing is stored on this website.</p>
      </form>
    </div>
  </div>
</section>

<script>
document.getElementById('apply').addEventListener('submit', function (e) {{
  e.preventDefault();
  var f = e.target;
  var get = function (id) {{ return (f.querySelector('#' + id) || {{}}).value || ''; }};
  var body = [
    'Name: ' + get('name'),
    'Where: ' + get('where'),
    'Links: ' + get('links'),
    '',
    'Style:',
    get('style'),
    '',
    'About me:',
    get('story'),
    '',
    'I confirm I am 18 or over.'
  ].join('\\n');
  window.location.href = 'mailto:{EMAIL}'
    + '?subject=' + encodeURIComponent('Be Featured: ' + get('name'))
    + '&body=' + encodeURIComponent(body);
}});
</script>
""")

# ---------------------------------------------------------------- consent
page("consent.html", "Consent and your rights — Goth Skin",
     "What Goth Skin does with your photographs, what it never does, and how to have a portrait taken down.",
     "consent.html", f"""
<section class="plain" style="padding-block:clamp(48px,7vw,76px) clamp(30px,4vw,44px)">
  <h1 class="bod">Consent and your rights</h1>
  <p class="lead" style="margin-top:22px">Written in plain English, because a release nobody can read is not consent.</p>
</section>

<section>
  <div class="grid">
    <p class="lab">What we may do</p>
    <div class="body">
      <ul class="marks">
        <li>Publish your portrait and your words on this website.</li>
        <li>Publish them on Goth Skin's own social accounts.</li>
        <li>Include them in Goth Skin's own printed work, such as a book or an exhibition.</li>
      </ul>
    </div>
  </div>
</section>

<section>
  <div class="grid">
    <p class="lab">What we may not do</p>
    <div class="body">
      <ul class="marks">
        <li>License your image to anyone else, sell it as stock or hand it to a third party.</li>
        <li>Use it in advertising, whether ours or anybody else's.</li>
        <li>Put it on anything we sell. That needs a separate, paid agreement that you sign later and can refuse.</li>
        <li>Publish your employer, ever, under any circumstances.</li>
        <li>Publish your city, your full name or anything else you asked us to leave out.</li>
      </ul>
    </div>
  </div>
</section>

<section>
  <div class="grid">
    <p class="lab">Taking it down</p>
    <div class="body">
      <p><strong>You can have your portrait removed at any time, for any reason, or for no reason.</strong>
      Email us and it comes down within seven days. You do not have to explain, and we will not ask.</p>
      <p>This applies forever and it applies to work already published. It is the one promise this
      project is built on, and if we ever break it, nothing else here is worth anything.</p>
      <p class="btns" style="margin-top:8px">
        <a class="btn" href="mailto:{EMAIL}?subject=Removal%20request">Request removal</a>
      </p>
    </div>
  </div>
</section>

<section>
  <div class="grid">
    <p class="lab">Reposting</p>
    <div class="body">
      <p>Press and community reposting help this project and we welcome both, with credit to
      Goth Skin and to the person in the photograph. Cropping out the person's name is the one
      thing we ask you not to do.</p>
      <p>Commercial reuse of any kind needs written permission from us and from the person pictured.</p>
    </div>
  </div>
</section>

<section>
  <div class="grid">
    <p class="lab">Machines</p>
    <div class="body">
      <p>Every page here carries noai and noimageai directives, and images are served at web
      resolution only. That stops casual scraping and nothing more. We are not going to pretend
      it stops a determined actor, because it does not.</p>
    </div>
  </div>
</section>

<section>
  <div class="grid">
    <p class="lab">The legal part</p>
    <div class="body">
      <p>Before any shoot you will receive a short written release that says all of the above in
      the language lawyers prefer. Nothing on this page is a substitute for it and nothing in it
      will contradict this page. If it ever does, this page is what we meant.</p>
      <p>Questions: <a href="mailto:{EMAIL}" style="border-bottom:1px solid var(--ink)">{EMAIL}</a></p>
    </div>
  </div>
</section>
""")

# ---------------------------------------------------------------- profile template
PROFILE = f"""
<section class="plain" style="padding-block:clamp(40px,6vw,64px) 0">
  <p class="lab">No. 01 &middot; Photographed in [CITY], [MONTH YEAR]</p>
  <h1 class="bod" style="margin-top:22px">[NAME]</h1>
  <div style="display:flex;gap:0;margin-top:30px;border-top:1px solid var(--ink);flex-wrap:wrap">
    <div style="flex:1 1 140px;padding:16px 22px 16px 0;border-right:1px solid var(--rule)">
      <p class="lab">Lives</p><p style="margin-top:6px;font-size:15px">[CITY]</p>
    </div>
    <div style="flex:1 1 140px;padding:16px 22px;border-right:1px solid var(--rule)">
      <p class="lab">Listens to</p><p style="margin-top:6px;font-size:15px">[ARTISTS]</p>
    </div>
    <div style="flex:1 1 140px;padding:16px 0 16px 22px">
      <p class="lab">Does</p><p style="margin-top:6px;font-size:15px">[WHAT THEY DO]</p>
    </div>
  </div>
</section>

<section class="plain" style="padding-block:clamp(30px,4vw,44px)">
  <figure style="margin:0">
    <!-- Replace this placeholder with the real portrait:
         <img src="images/01-lead.jpg" alt="Portrait of [NAME], photographed in [CITY]"> -->
    <div style="aspect-ratio:4/3;background:var(--bone-2);border:1px dashed #C8C2B9;display:flex;align-items:center;justify-content:center">
      <p class="lab" style="max-width:none">Lead portrait &middot; images/01-lead.jpg</p>
    </div>
    <figcaption class="lab" style="margin-top:14px">[CITY], [MONTH YEAR]</figcaption>
  </figure>
</section>

<section>
  <p class="bod" style="font-size:clamp(1.5rem,4.4vw,2.6rem);line-height:1.18;max-width:22ch;margin:0 auto;text-align:center">
    &ldquo;[THE ONE LINE THAT MADE YOU WANT TO PUBLISH THIS.]&rdquo;
  </p>
</section>

<section>
  <div class="grid">
    <p class="lab">The story</p>
    <div class="body">
      <p>[Three to five short paragraphs, in their voice as much as possible. Music goes in
      somewhere, because it is how people in this world find each other. Exclusion may appear,
      in passing, among everything else. It is never the whole profile.]</p>
      <p>[Paragraph two.]</p>
      <p>[Paragraph three.]</p>
    </div>
  </div>
</section>

<section>
  <div class="panel">
    <p style="margin:0;font-size:14.5px">[NAME] asked us not to publish [WHATEVER THEY ASKED US TO WITHHOLD].
    Everyone in this archive sets their own terms and can ask us to take their portrait down at any
    time, without giving a reason. <a href="../consent.html" style="border-bottom:1px solid var(--ink)">Your rights</a>.</p>
  </div>
</section>

<section>
  <div style="display:flex;align-items:center;justify-content:space-between;gap:20px;flex-wrap:wrap">
    <p class="lab">Next in the archive</p>
    <a class="bod" style="font-size:clamp(1.4rem,3.4vw,2.2rem)" href="#">[NEXT NAME] &rarr;</a>
  </div>
</section>
"""
page("portraits/_template.html", "[NAME] — Goth Skin",
     "[One line from their story, used as the link preview description.]",
     "portraits.html", PROFILE, depth=1)
