# Static page builder for the Triple Crown Electric concept. Run: python3 build.py
import json, os
BASE = 'https://daveo820.github.io/triple-crown-electric-demo/'  # temporary GitHub Pages link; swap for Vercel later
TEL, TEL_H = '+19198032023', '(919) 803&#8209;2023'
GMAPS = 'https://www.google.com/maps/search/?api=1&query=Triple+Crown+Electric+LLC+313+US+70+Hwy+E+Garner+NC'
TOWNS = ['Garner','Raleigh','Cary','Morrisville','Knightdale','Clayton','Fuquay Varina','Durham','Chapel Hill','Wake Forest']
ORG = {"@context":"https://schema.org","@type":"Electrician","name":"Triple Crown Electric LLC",
 "url":"https://www.triplecrownelectric.com","telephone":"+1-919-803-2023","email":"triplecrownelectric@gmail.com",
 "founder":{"@type":"Person","name":"Eric Josey"},
 "address":{"@type":"PostalAddress","streetAddress":"313-C US Highway 70 East","addressLocality":"Garner","addressRegion":"NC","postalCode":"27529","addressCountry":"US"},
 "geo":{"@type":"GeoCoordinates","latitude":35.702794,"longitude":-78.597804},
 "openingHours":"Mo-Fr 08:00-18:00","areaServed":TOWNS,"paymentAccepted":"Cash, Check, Credit Card, PayPal",
 "aggregateRating":{"@type":"AggregateRating","ratingValue":"4.9","reviewCount":"44"},
 "image":BASE+"img/storefront-313c.webp"}
FONTS = 'https://fonts.googleapis.com/css2?family=Archivo:wdth,wght@112..125,600..900&family=Martian+Mono:wght@400;500&family=Public+Sans:ital,wght@0,400;0,600;0,700;1,400&display=swap'
def TAG(n, txt=''): return f'<span class="ckt"><i class="tog" aria-hidden="true"></i>CKT {n:02d}</span>' + (f'<span class="ckt-t">{txt}</span>' if txt else '')
STARS = '<span class="stars" aria-hidden="true">&#9733;&#9733;&#9733;&#9733;&#9733;</span>'

def img(src, alt, sizes='100vw', eager=False, w=None, h=None, cls=''):
    small = src.replace('.webp','-800.webp')
    srcset = f' srcset="img/{small} 800w, img/{src} 1080w" sizes="{sizes}"' if os.path.exists('img/'+small) else ''
    dims = f' width="{w}" height="{h}"' if w else ''
    load = ' fetchpriority="high"' if eager else ' loading="lazy" decoding="async"'
    return f'<img src="img/{src}"{srcset} alt="{alt}"{dims}{load}' + (f' class="{cls}"' if cls else '') + '>'

HEAD = '''<!doctype html><html lang="en" class="no-js"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>{t}</title><meta name="description" content="{d}"><link rel="canonical" href="{url}">
<meta property="og:type" content="website"><meta property="og:site_name" content="Triple Crown Electric (concept)"><meta property="og:title" content="{t}"><meta property="og:description" content="{d}"><meta property="og:url" content="{url}"><meta property="og:image" content="{base}og.png">
<meta name="twitter:card" content="summary_large_image"><meta name="twitter:title" content="{t}"><meta name="twitter:description" content="{d}"><meta name="twitter:image" content="{base}og.png">
<meta name="robots" content="noindex, nofollow"><!-- concept demo, not for indexing -->
<meta name="theme-color" content="#1c2a63">
<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link rel="preload" as="style" href="{fonts}"><link rel="stylesheet" href="{fonts}" media="print" onload="this.media='all'"><noscript><link rel="stylesheet" href="{fonts}"></noscript>
<link rel="stylesheet" href="css/design-system.css"><link rel="stylesheet" href="css/components.css"><link rel="stylesheet" href="css/pages.css">
<link rel="icon" href="data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 26 26'%3E%3Crect width='26' height='26' rx='4' fill='%231c2a63'/%3E%3Cpath d='M15 3 L8 15 H13 L11 23 L18 11 H13 Z' fill='%23d9ae3c'/%3E%3C/svg%3E">
<script>document.documentElement.classList.replace('no-js','js-ready')</script><script type="application/ld+json">{ld}</script></head><body>
<a class="skip" href="#main">Skip to content</a>
<div class="demo-bar">Concept by <a href="https://luminarch.pro">LuminArch</a>. Not the official Triple Crown Electric site. Facts come from public records and Google reviews; placeholders are labeled.</div>
<header class="top"><div class="wrap nav"><a class="mark" href="index.html"><span class="bolt" aria-hidden="true"><svg viewBox="0 0 20 26"><path d="M12 1 L3 15 H9 L7 25 L17 10 H11 Z"/></svg></span><span class="mk"><b>Triple Crown</b><small>Electric LLC &middot; Garner NC</small></span></a>
<button class="menu-btn" aria-expanded="false" aria-controls="menu">Menu</button><ul id="menu">{nav}</ul><a class="btn btn--call" href="tel:{tel}"><span class="dot" aria-hidden="true"></span><span class="cl-full">{telh}</span><span class="cl-short">Call Eric</span></a></div></header><main id="main">'''

FOOT = f'''</main><footer class="site-foot"><div class="wrap">
<div class="door">
 <div class="door-l"><p class="kicker kicker--gold">{TAG(20,'Main breaker')}</p><p class="foot-call">One call.<br><a href="tel:{TEL}">{TEL_H}</a></p><p class="foot-sub">Monday to Friday, 8am to 6pm. Free estimates. Cash, check, credit card and PayPal.</p></div>
 <div class="door-r"><div class="label-card"><p class="lc-h">Panel directory</p><dl>
  <div><dt>Owner</dt><dd>Eric Josey</dd></div><div><dt>Shop</dt><dd>313-C US Hwy 70 East, Garner NC 27529</dd></div>
  <div><dt>NC electrical</dt><dd>License L.32141</dd></div><div><dt>Email</dt><dd><a href="mailto:triplecrownelectric@gmail.com">triplecrownelectric@gmail.com</a></dd></div>
  <div><dt>Google</dt><dd>4.9 from 44 reviews</dd></div></dl></div></div>
</div>
<div class="foot-grid">
 <div><h2>Work</h2><ul><li><a href="services.html#residential">Residential</a></li><li><a href="services.html#commercial">Commercial</a></li><li><a href="record.html">Permit record</a></li><li><a href="reviews.html">Reviews</a></li></ul></div>
 <div><h2>Talk to Eric</h2><ul><li><a href="contact.html">Free estimate</a></li><li><a href="contact.html#hiring">We are hiring</a></li><li><a href="{GMAPS}" rel="noopener">Directions</a></li></ul></div>
 <div class="ft-towns"><h2>Service area</h2><p>{" &middot; ".join(TOWNS)}</p></div>
</div>
<div class="foot-row"><span>Triple Crown Electric LLC, Garner, North Carolina</span><span>Concept by <a href="https://luminarch.pro">LuminArch</a></span></div></div></footer>
<script src="js/main.js"></script></body></html>'''

NAV = [('services.html','Services'),('record.html','Permit record'),('reviews.html','Reviews'),('contact.html','Free estimate')]
def bc(*n): return {"@context":"https://schema.org","@type":"BreadcrumbList","itemListElement":[{"@type":"ListItem","position":i+1,"name":a,"item":BASE+b} for i,(a,b) in enumerate(n)]}
def page(fn, t, d, body, ld=None):
    assert 50 <= len(t) <= 62, (fn, len(t), t)
    assert 130 <= len(d) <= 165, (fn, len(d), d)
    nav = ''.join(f'<li><a href="{h}"' + (' aria-current="page"' if h == fn else '') + f'>{n}</a></li>' for h, n in NAV)
    url = BASE + ('' if fn == 'index.html' else fn)
    open(fn,'w').write(HEAD.format(t=t,d=d,url=url,base=BASE,nav=nav,ld=json.dumps(ld or ORG),fonts=FONTS,tel=TEL,telh=TEL_H) + body + FOOT)

# ---------- real Google reviews, as shown on the Exa place page (Google review data). "..." = truncated at the source ----------
EXA = 'https://exa.ai/library/place/qjqsyr1j1t1'
REV = [
 ('2026-02-05','Feb 2026','I cannot recommend Triple Crown Electric highly enough. They were professional, punctual, and incredibly knowledgeable. Everything was explained clearly, the work was done efficiently, and the results were flawless. Eric did an outstanding job from start to finish. He arrived on time, diagnosed the issue quickly, and completed the work with care and precision. What really stood out was how clearly he explained the process and costs, no surprises, no pressure. The work area was left spotless, and everything works perfectly...'),
 ('2026-01-05','Jan 2026','The technician fixed our problem, evaluated some other issues and helped us investigate and explain some other issues we were having.'),
 ('2025-03-20','Mar 2025','We were especially pleased with: speaking to someone (Eric) and not having to leave a voicemail for a return call.. Prompt response to our request for service. Fortunately, as it worked out, we received service call on the same day. Eric arrived on time and able to address our needs. Thank You Eric for satisfying our request in such a timely manner.'),
 ('2024-09-24','Sep 2024','Eric was exceptional in every way possible. He took on a complex job that required a lot of schedule coordination and got it done quickly and efficiently. He took the time to explain everything and went above and beyond by helping out with a couple of small electrical issues. More than that, he&rsquo;s a genuinely kind, trustworthy, and reliable person.'),
 ('2023-09-04','Sep 2023','I had an issue with my outlets in my kitchen. Eric from Triple crown was able to come out the same day and handle everything. I was also able to get a new outlet installed under my sink. Eric was awesome, he gave a great diagnostic on what happened, explained everything he needed to do and gave time and cost estimates along the way. I&rsquo;ll definitely be using triple crown for my needs in the future.'),
 ('2022-10-06','Oct 2022','Let me start by saying I called 9 electricians over the course of 2 months and Eric was #9. He was timely, responsive, and honest. He sent an invoice electronically so we were able to put down a deposit and schedule an appointment. From initial call to completed work, it took 2 weeks. He is fairly priced and where another electrician told me we would have to upgrade our entire panel, after a couple photos, Eric basically said it was no big deal and he would take care of installing our EV charger...'),
 ('2022-03-23','Mar 2022','Great company! We hired Triple Crown Electric to rewire our kitchen electrical outlets and to install recessed lights and pendant lights as part of our kitchen renovation. Eric is a very smart electrician, he&rsquo;s super efficient yet demonstrates an impressive attention to detail at the same time, his job quality is incomparable. My wife and I are very pleased with his work, we love our new kitchen lighting. We highly recommend Triple Crown Electric.'),
 ('2022-03-08','Mar 2022','My wife and I recently hired Triple Crown Electric for two different jobs at our home. Eric and his team from Triple Crown are extremely professional. They showed up on time and explained to us what their plan of action was to accomplish the jobs at hand. Their pricing was excellent, and beat a lot of the other competitors that had bid for the jobs. Eric even advised and helped us to pick out the correct and best lighting fixtures that would fit our needs for one of the jobs...'),
]
def rq(i, cls=''):
    iso, d, q = REV[i]
    return f'<blockquote class="rq rv {cls}"><div class="rq-top">{STARS}<time datetime="{iso}">{d}</time></div><p>&ldquo;{q}&rdquo;</p><footer><span class="src">Google review, 5 of 5</span></footer></blockquote>'

RES = ['Troubleshooting and circuit tracing','Service upgrades and meter upgrades','Panel connections','Generators and transfer switches','EV charger installs','Recessed lights','Ceiling fans and exhaust fans','Outlets and ground faults','Remodeling and new additions','Home office wiring','TV mounting and TV and telephone wiring','Hot tub and spa hookups','Fluorescent ballast repair']
COM = ['Panel changes, single and 3 phase','Lighting upgrades','Parking lot lighting','Office wiring','Computer cabling and wire toning','Telecommunication','Surge protection','GFI certification','Circuitry load testing','Remodeling and new additions','Troubleshooting and circuit tracing']
YEARS = [('2023',25),('2024',30),('2025',37),('2026',8)]
VALS = [('Under $5k',12),('$5k to $20k',20),('$20k to $50k',13),('$50k to $100k',10),('$100k to $250k',11),('$250k to $500k',8),('$500k to $1M',6),('Over $1M',1)]
JOBS = [('Aug 2025','North Raleigh, 27617','Renovation of a 4,167 sq ft two story home plus a 740 sq ft heated first floor addition.','$544,284','Residential electrical sub permit'),
 ('Aug 2025','Downtown Raleigh, 27601','Three new three story condo style townhomes with a stair tower, about 3,560 sq ft each.','$501,178 to $503,291 each','Sub permits on all three'),
 ('Oct 2025','Downtown Raleigh, 27601','Second floor addition with an attic renovation, first floor renovation and a new carport.','$320,292','Residential electrical sub permit')]

# ---------- HOME ----------
panel = ''.join(f'<li><span class="pn">{2*i+1:02d}</span><span class="pl">{a}</span><i class="tog" aria-hidden="true"></i></li><li><span class="pn">{2*i+2:02d}</span><span class="pl">{b}</span><i class="tog" aria-hidden="true"></i></li>' for i,(a,b) in enumerate([
 ('Troubleshooting','Panel changes, 1 and 3 phase'),('Service and meter upgrades','Lighting upgrades'),('Generators, transfer switches','Parking lot lighting'),
 ('EV chargers','Office and data wiring'),('Recessed lights and fans','Surge protection'),('Remodels and additions','GFI certification')]))
page('index.html','Electrician in Garner NC | Triple Crown Electric, Eric Josey',
 'Licensed Garner electrician Eric Josey: service calls, panel and generator work, and wiring on 100 permitted Triangle projects. 4.9 on Google. Call (919) 803-2023.', f'''
<section class="hero"><div class="wrap hero-grid">
 <div class="hero-copy rv"><p class="kicker">{TAG(1,'NC electrical license L.32141')}</p>
  <h1>From one dead outlet to the <span class="hl">whole addition.</span></h1>
  <p class="lede">Triple Crown Electric is Eric Josey&rsquo;s shop on US 70 in Garner. Service calls for Triangle homes, and the wiring behind about 100 permitted projects since 2023, from kitchen circuits to new townhomes.</p>
  <div class="cta"><a class="btn" href="tel:{TEL}">Call {TEL_H}</a><a class="btn btn--line" href="contact.html">Free estimate <span aria-hidden="true">&rarr;</span></a></div>
  <p class="hours"><span class="live" aria-hidden="true"></span>Mon to Fri, 8am to 6pm &middot; 313-C US Hwy 70 East, Garner</p></div>
 <div class="panel rv" aria-labelledby="panel-h"><div class="panel-head"><p id="panel-h">Panel schedule</p><span>Triple Crown Electric &middot; Garner NC</span></div>
  <ol class="panel-list">{panel}</ol>
  <div class="panel-foot"><span>Left: homes</span><span>Right: businesses</span><a href="services.html">Full list &rarr;</a></div></div>
</div></section>

<section class="meter" aria-label="Triple Crown Electric by the numbers"><div class="wrap meter-grid">
 <a class="m rv" href="reviews.html"><span class="mv"><span data-count="4.9" data-dec="1">4.9</span></span><span class="ml">Google rating, <b>44 reviews</b></span></a>
 <a class="m rv" href="record.html"><span class="mv"><span data-count="100">100</span></span><span class="ml">permitted projects, <b>2023 to 2026</b></span></a>
 <a class="m rv" href="record.html#years"><span class="mv"><span data-count="37">37</span></span><span class="ml">projects in <b>2025 alone</b></span></a>
 <div class="m rv"><span class="mv mv--sm">L.32141</span><span class="ml">NC electrical license, <b>active</b></span></div>
</div><p class="wrap src-note">Permit counts and license: BuildZoom, from North Carolina permit and license board records, updated Sep 2026. Rating: Google.</p></section>

<section class="voices" aria-labelledby="v-h"><div class="wrap voices-grid">
 <div class="v-head rv"><p class="kicker">{TAG(3,'What people say first')}</p><h2 id="v-h">&ldquo;Speaking to someone (Eric) and not having to leave a voicemail.&rdquo;</h2><p>Reviewers keep naming the same things: Eric picks up, shows up the same day, and explains the cost before he starts.</p><a class="btn btn--line" href="reviews.html">Read 8 Google reviews</a></div>
 <div class="v-quotes">{rq(0,'rq--big')}{rq(5)}</div>
</div></section>

<section class="record-teaser" aria-labelledby="r-h"><div class="wrap rt-grid">
 <div class="rv"><p class="kicker kicker--gold">{TAG(5,'The permit record')}</p><h2 id="r-h">The small jobs pay the bills. <em>The permits tell you the rest.</em></h2>
 <p>Public permit records list Triple Crown on additions, whole home renovations and new townhomes across Raleigh. Twenty six of the projects with a public value were valued over $100,000.</p>
 <a class="btn btn--gold" href="record.html">See the record <span aria-hidden="true">&rarr;</span></a></div>
 <ol class="years rv" id="years-mini">{''.join(f'<li><span class="y">{y}</span><span class="bar" style="--v:{n/37:.3f}"><b>{n}</b></span></li>' for y,n in YEARS)}</ol>
 <p class="fine rv">Projects per year from BuildZoom. 2026 is January through September. Values are the permit valuation for the whole project, not the electrical contract.</p>
</div></section>

<section class="split" aria-labelledby="s-h"><div class="wrap split-grid">
 <figure class="split-photo rv">{img('fleet-truck-van.webp','Triple Crown Electric pickup and lettered work van on a job site',sizes='(max-width:900px) 100vw, 50vw',w=1000,h=541)}<figcaption>{TAG(7)} The Triple Crown van, from triplecrownelectric.com</figcaption></figure>
 <div class="rv"><p class="kicker">{TAG(9,'Homes and businesses')}</p><h2 id="s-h">Two sides of the panel.</h2>
 <p><b>Homes:</b> troubleshooting, service upgrades, generators, EV chargers, recessed lighting, hot tubs and remodels.</p>
 <p><b>Businesses:</b> single and 3 phase panel changes, parking lot and lighting upgrades, office and data wiring, surge protection and GFI certification.</p>
 <a class="btn btn--line" href="services.html">Every service</a></div>
</div></section>

<section class="area" aria-labelledby="a-h"><div class="wrap rv"><p class="kicker">{TAG(11,'Service area')}</p><h2 id="a-h">Garner first. <em>Then nine more towns down the line.</em></h2>
<ol class="line">{''.join(f'<li><span>{t}</span></li>' for t in TOWNS)}</ol></div></section>''', ld=[ORG,bc(('Home',''))])

# ---------- SERVICES ----------
def svc(lst, side): return ''.join(f'<li class="rv"><span class="pn">{(2*i+1) if side=="L" else (2*i+2):02d}</span>{s}</li>' for i,s in enumerate(lst))
page('services.html','Residential and Commercial Electrical Services | Triple Crown',
 'Panel and service upgrades, generators, EV chargers, lighting, troubleshooting and 3 phase commercial work from Triple Crown Electric in Garner NC. Call Eric today.', f'''
<section class="page-head"><div class="wrap rv"><p class="crumbs"><a href="index.html">Home</a> / Services</p><p class="kicker">{TAG(2,'Services')}</p><h1>Every circuit <em>Triple Crown</em> works on.</h1>
<p class="lede">The list below comes straight from the current Triple Crown site, plus EV charger installs, which show up in a Google review. Odd numbers are homes. Even numbers are businesses, the way a panel is labeled.</p></div></section>
<div class="wrap svc-grid">
 <section id="residential" class="svc-col" aria-labelledby="res-h"><h2 id="res-h">{TAG(1)} Residential</h2><ul class="svc-list">{svc(RES,'L')}</ul>
  <p class="note">Recent review: &ldquo;where another electrician told me we would have to upgrade our entire panel, after a couple photos, Eric basically said it was no big deal and he would take care of installing our EV charger.&rdquo; <a href="reviews.html">Google, Oct 2022</a></p></section>
 <section id="commercial" class="svc-col svc-col--dark" aria-labelledby="com-h"><h2 id="com-h">{TAG(2)} Commercial</h2><ul class="svc-list">{svc(COM,'R')}</ul>
  <figure class="svc-fig">{img('commercial-cantina-exterior.webp','Taco Bell Cantina storefront, a commercial job shown on the Triple Crown site',sizes='(max-width:900px) 100vw, 40vw',w=600,h=458)}<figcaption>Shown on Triple Crown&rsquo;s commercial page. <strong>Placeholder:</strong> confirm the scope and location with Eric.</figcaption></figure></section>
</div>
<section class="wrap faq" aria-labelledby="f-h"><p class="kicker">{TAG(4,'Before you call')}</p><h2 id="f-h">Straight answers.</h2>
<details class="rv"><summary>Is Triple Crown licensed?</summary><p>Yes. North Carolina electrical contractor license L.32141, verified active by BuildZoom in May 2026. The company also holds NC plumbing license 38077.</p></details>
<details class="rv"><summary>Do you give free estimates?</summary><p>Yes. Estimates are free. Call {TEL_H} or send the form on the estimate page.</p></details>
<details class="rv"><summary>How do I pay?</summary><p>Cash, check, credit card and PayPal.</p></details>
<details class="rv"><summary>Do you pull permits?</summary><p>For permitted work, yes. Public records show about 100 permitted projects from 2023 through September 2026.</p></details>
<details class="rv"><summary>What are your hours?</summary><p>Monday to Friday, 8am to 6pm. Closed Saturday and Sunday.</p></details>
</section>''', ld=[ORG,bc(('Home',''),('Services','services.html')),
 {"@context":"https://schema.org","@type":"FAQPage","mainEntity":[{"@type":"Question","name":q,"acceptedAnswer":{"@type":"Answer","text":a}} for q,a in [("Is Triple Crown licensed?","Yes. North Carolina electrical contractor license L.32141."),("Do you give free estimates?","Yes. Call (919) 803-2023."),("How do I pay?","Cash, check, credit card and PayPal."),("What are your hours?","Monday to Friday, 8am to 6pm.")]]}]+
 [{"@context":"https://schema.org","@type":"Service","name":n,"provider":{"@type":"Electrician","name":"Triple Crown Electric LLC"},"areaServed":"Garner, NC"} for n in ['Residential electrical service','Commercial electrical service']])

# ---------- PERMIT RECORD ----------
page('record.html','Permit Record: 100 Projects Since 2023 | Triple Crown Electric',
 'See Triple Crown Electric permit history: about 100 permitted Triangle projects since 2023, from service upgrades to $500,000 additions. Get a free estimate today.', f'''
<section class="page-head page-head--dark"><div class="wrap rv"><p class="crumbs"><a href="index.html">Home</a> / Permit record</p><p class="kicker kicker--gold">{TAG(5,'Public record')}</p><h1>About 100 permits. <em>Here&rsquo;s what they were for.</em></h1>
<p class="lede">Every permitted electrical job in North Carolina leaves a public record. Here is what the records show for Triple Crown Electric, summarized by BuildZoom.</p></div></section>
<div class="wrap rec">
<section id="years" class="rec-block rv" aria-labelledby="y-h"><h2 id="y-h">Projects per year</h2><ol class="years years--big">{''.join(f'<li><span class="y">{y}</span><span class="bar" style="--v:{n/37:.3f}"><b>{n}</b></span></li>' for y,n in YEARS)}</ol><p class="fine">2026 runs January through September.</p></section>
<section class="rec-block rv" aria-labelledby="v-h"><h2 id="v-h">Project value, when public</h2><ol class="vals">{''.join(f'<li><span class="y">{l}</span><span class="bar" style="--v:{n/20:.3f}"><b>{n}</b></span></li>' for l,n in VALS)}</ol><p class="fine">35 more projects have no public value. A permit&rsquo;s value covers the whole project, not just the electrical work. Typical permit size about $39,500.</p></section>
<section class="rec-jobs" aria-labelledby="j-h"><p class="kicker">{TAG(6,'Sample permits')}</p><h2 id="j-h">Three recent jobs on the record.</h2>
<div class="jobs">{''.join(f'<article class="job rv"><p class="job-d">{d} &middot; {w}</p><h3>{s}</h3><dl><div><dt>Project value</dt><dd>{v}</dd></div><div><dt>Permit</dt><dd>{p}</dd></div></dl></article>' for d,w,s,v,p in JOBS)}</div>
<p class="note rv">Street addresses are left out on purpose. These are private homes. <strong>Placeholder:</strong> photos of these jobs, with the owners&rsquo; OK.</p></section>
<section class="rec-mix rv" aria-labelledby="m-h"><h2 id="m-h">What the permits are for</h2><ul class="mix"><li><b>90</b> electrical projects</li><li><b>21</b> home additions</li><li><b>12</b> new construction</li></ul><p class="fine">Categories overlap. Source: BuildZoom analysis of the last four years of permits.</p></section>
<section class="gallery-ph rv" aria-labelledby="g-h"><h2 id="g-h">{TAG(8)} Job photos</h2><div class="ph-grid"><figure>{img('commercial-cantina-interior.webp','Restaurant dining room with new lighting and menu screens, shown on the Triple Crown site',sizes='(max-width:900px) 100vw, 33vw',w=600,h=291)}<figcaption>From the current site&rsquo;s commercial page</figcaption></figure><div class="ph">Placeholder: panel upgrade, before and after</div><div class="ph">Placeholder: addition rough in</div><div class="ph">Placeholder: EV charger install</div></div>
<p class="note">The gallery page on triplecrownelectric.com is empty today. This grid is ready for Eric&rsquo;s phone photos.</p></section>
<p class="src-note">Source: <a href="https://www.buildzoom.com/contractor/triple-crown-electric" rel="noopener">BuildZoom contractor profile</a>, built from NC permit and license board records, updated Sep 24 2026.</p>
</div>''', ld=[ORG,bc(('Home',''),('Permit record','record.html'))])

# ---------- REVIEWS ----------
page('reviews.html','4.9 Stars from 44 Google Reviews | Triple Crown Electric',
 'Read Google reviews of Eric Josey and Triple Crown Electric: same day service calls, clear pricing, EV chargers and kitchen rewires. Call (919) 803-2023 today.', f'''
<section class="page-head"><div class="wrap ph-grid"><div class="rv"><p class="crumbs"><a href="index.html">Home</a> / Reviews</p><p class="kicker">{TAG(3,'Reviews')}</p><h1>Eight reviews. <em>Seven name Eric.</em></h1><p class="lede">All eight are five stars. The newest is from February 2026.</p></div>
<div class="score rv"><span class="mv" data-count="4.9" data-dec="1">4.9</span><span>{STARS}<b>44 Google reviews</b></span></div></div></section>
<div class="wrap wall">{''.join(rq(i) for i in range(len(REV)))}</div>
<section class="wrap rv-sources rv"><h2>Where these come from</h2><p>Copied word for word from Triple Crown&rsquo;s Google listing, via a September 2026 snapshot of Google review data on the <a href="{EXA}" rel="noopener">Exa place page</a>. Three dots mark where the snapshot cuts a review short. Reviewer names were not included in the snapshot, so none are shown.</p>
<p class="note"><strong>Not used:</strong> the eleven testimonials on the current site, signed with first names and initials, because they can&rsquo;t be traced to a source. <strong>Placeholder:</strong> a live Google reviews feed with names, once Eric approves it.</p></section>''', ld=[ORG,bc(('Home',''),('Reviews','reviews.html'))])

# ---------- CONTACT ----------
page('contact.html','Free Electrical Estimate in Garner and Raleigh | Triple Crown',
 'Ask Eric Josey for a free electrical estimate in Garner, Raleigh, Cary or Clayton. Call (919) 803-2023, Monday to Friday 8 to 6, or send the form. Cards accepted.', f'''
<section class="page-head"><div class="wrap rv"><p class="crumbs"><a href="index.html">Home</a> / Free estimate</p><p class="kicker">{TAG(4,'Free estimate')}</p><h1>Tell Eric <em>what tripped.</em></h1><p class="lede">Free estimates. Calling is fastest: {TEL_H}, Monday to Friday, 8am to 6pm.</p></div></section>
<div class="wrap est-grid">
<form id="qform" class="rv" novalidate>
<fieldset><legend>Home or business?</legend><div class="chips-in">{''.join(f'<label><input type="radio" name="kind" value="{k}"{" checked" if k=="Home" else ""}> {k}</label>' for k in ['Home','Business'])}</div></fieldset>
<fieldset><legend>What do you need?</legend><div class="chips-in">{''.join(f'<label><input type="checkbox" name="need" value="{k}"> {k}</label>' for k in ['Something stopped working','Panel or service upgrade','Generator','EV charger','Lighting or fans','Remodel or addition','Commercial work','Not sure'])}</div></fieldset>
<div class="two"><div class="field"><label for="n">Name</label><input id="n" name="name" autocomplete="name" required></div><div class="field"><label for="p">Phone</label><input id="p" name="tel" type="tel" autocomplete="tel" required></div></div>
<div class="two"><div class="field"><label for="e">Email</label><input id="e" name="email" type="email" autocomplete="email"></div><div class="field"><label for="t">Town</label><select id="t" name="town">{''.join(f'<option>{t}</option>' for t in TOWNS)}<option>Somewhere else</option></select></div></div>
<div class="field"><label for="m">What&rsquo;s going on?</label><textarea id="m" name="msg" rows="5"></textarea></div>
<button class="btn" type="submit">Send to Eric <span aria-hidden="true">&rarr;</span></button>
<p class="note" id="qmsg" role="status">Demo form. Nothing is sent.</p></form>
<aside class="rv"><figure class="store">{img('storefront-313c.webp','Triple Crown Electric shop door at 313C, US Highway 70 East, Garner',sizes='(max-width:900px) 100vw, 35vw',w=1080,h=1143)}<figcaption>{TAG(12)} 313-C US Hwy 70 East, Garner NC 27529</figcaption></figure>
<div class="est-card"><a class="phone" href="tel:{TEL}">{TEL_H}</a><p>Mon to Fri, 8am to 6pm<br><a href="mailto:triplecrownelectric@gmail.com">triplecrownelectric@gmail.com</a><br><a href="{GMAPS}" rel="noopener">Get directions</a></p><p class="fine">Cash, check, credit card and PayPal accepted.</p></div></aside>
</div>
<section id="hiring" class="wrap hiring rv" aria-labelledby="h-h"><p class="kicker">{TAG(14,'Careers')}</p><h2 id="h-h">Triple Crown is hiring.</h2><p>The current site says &ldquo;We Are Hiring!&rdquo; and nothing else. <strong>Placeholder:</strong> roles, license level and pay range from Eric, so electricians can apply here instead of calling.</p></section>''', ld=[ORG,bc(('Home',''),('Free estimate','contact.html'))])

page('404.html','Page Not Found | Triple Crown Electric, Garner North Carolina',
 'That page tripped the breaker. Head back to the Triple Crown Electric home page or call Eric Josey at (919) 803-2023 for a free electrical estimate in Garner.',
 f'<section class="wrap nf"><p class="kicker">{TAG(404 % 100,"Open circuit")}</p><h1>This page tripped <em>the breaker.</em></h1><p style="margin-top:28px"><a class="btn" href="index.html">Back to the home page</a></p></section>')
print('built')
