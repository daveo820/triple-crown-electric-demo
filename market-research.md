# Market research: electrician sites, for the Triple Crown Electric concept

## How this was done (and what I could not get)
- Researched 7 October 2026. Ten electrician sites: two national franchises that set the conversion playbook (Mister Sparky, Mr. Electric) and eight Triangle electricians that show up on searches for "best electrician Garner NC" and "electrician Raleigh NC".
- Lighthouse 12, mobile, one run per homepage from this box. Single runs are noisy, so treat the numbers as rough.
- **No traffic numbers.** Similarweb and Semrush need logins or block automated requests, so "top performing" here means the sites that rank on the local searches, the national brands that set the pattern, and how fast they load.
- Homepage screenshots (desktop and iPhone 13) are in `research/`, compressed.

## Lighthouse, mobile homepage
| Site | Who | Perf | A11y | Best pr. | SEO | LCP | Page weight |
|---|---|---|---|---|---|---|---|
| bushcrowelectric.com | Raleigh, residential only | 81 | 100 | 93 | 100 | 3.8 s | 0.6 MB |
| trippelectric.com | Triangle, since 1996, ranks for "Garner electrician" | 76 | 86 | 75 | 92 | 4.2 s | 1.4 MB |
| electricallpro.com | Raleigh, 175+ Google reviews, ranks for Garner | 74 | 100 | 82 | 100 | 6.3 s | 1.1 MB |
| arcelectric.com | Raleigh, family owned since 2011 | 69 | 76 | 100 | 100 | 7.0 s | 0.9 MB |
| theplugelectrician.com | Garner, 5.0 from 123 reviews on its own widget | 61 | 92 | 100 | 100 | 12.5 s | 2.8 MB |
| rduelectricians.com | Royal Electric, Raleigh | 60 | 96 | 96 | 92 | 22.3 s | 5.7 MB |
| mrelectric.com | National franchise | 43 | 65 | 57 | 85 | 4.8 s | 4.2 MB |
| powermasterelectric.com | Triangle, generator focused | 43 | 85 | 75 | 100 | 79.6 s | 23.7 MB |
| mistersparky.com | National franchise | 38 | 90 | 75 | 85 | 12.4 s | 8.4 MB |
| pointelectricnc.com | Raleigh area | 35 | 92 | 79 | 92 | 12.1 s | 5.1 MB |
| **triplecrownelectric.com** | **Client, Garner** | **55** | **46** | **50** | 92 | **17.3 s** | **3.2 MB** |

Triple Crown has the worst accessibility score in the set (46) and the second slowest main paint among the local shops. Only Bushcrow gets its main content up in under 4 seconds on mobile. A static site that loads in under 2.5 seconds would beat every competitor here.

## Patterns the strongest sites share
1. **The phone number is the main button.** Electric All Pro, ARC, The Plug, PowerMaster and Royal all put a tap to call button in the header and again in the hero. Mr. Electric pins "Call Now" to the bottom of the mobile screen. People calling an electrician usually have a problem now.
2. **A number with a source, right under the headline.** ARC: "4.9 stars across 620+ reviews on Google, Yelp and Nextdoor, NC Electrical License #29565". Electric All Pro: "5.0 on Google, 175+ Reviews" and "NC Electrical License: L.32531". Bushcrow puts its license number in a trust strip. The license number shows up on nearly every Triangle site, so leaving it off (as Triple Crown does today) reads as missing.
3. **Price honesty as the pitch.** ARC leads with "no trip charge" and "free in home quotes", Electric All Pro with "clear recommendations and upfront pricing", Royal with "upfront pricing, no surprise charges". Triple Crown's reviews already say this ("no surprises, no pressure", "gave time and cost estimates along the way"), but its site never does.
4. **Owner story in first person.** Electric All Pro's founder note ("I started Electric All Pro in 2018 after more than 20 years in the trade") and ARC's origin story ("we kept seeing the same gaps in customer service") do the work Triple Crown's broken sentence "a team of years of experience as well" tries to do.
5. **Separate paths for homes and businesses.** ARC, Tripp, Point and Royal all split Residential and Commercial in the nav. Big sites (Mister Sparky, ARC, Tripp) also add one page per service and per town for search.
6. **The look is converging.** Five of the ten (Electric All Pro, Bushcrow, PowerMaster, The Plug, Royal) use a dark navy or black hero with a bright yellow, lime or cyan accent, and most add a lightning bolt. Several look like the same template family. That is a chance to look different.
7. **Common weak spots:** cookie banners covering the first mobile screen (Mister Sparky, Point, Royal), stock photos of smiling technicians, mascots (PowerMaster), and heavy pages (PowerMaster sends 23.7 MB).

## What none of them show
No site in the set shows its permit record. Permit history is public, and Triple Crown's is unusually strong for a small shop: about 100 permitted projects from 2023 through September 2026, 26 of them on projects valued over $100,000, including additions and new townhomes in Raleigh (BuildZoom, from NC permit records). That is the one thing this concept can say that no competitor says.

## Local competition (Garner)
For "best electrician Garner NC" the Google listings index shows The Plug Electrician (5.0, 59 ratings on Google), LivElectric Services (4.9, 76), Triple Crown (4.9, 44), Michael Westmoreland Electric (5.0, 4) and Gregory Electric (4.6, 5). Triple Crown is third by review count among Garner based shops. The Plug and Electric All Pro both target "Garner" directly with landing pages; Tripp Electric has a dedicated /garner page. Triple Crown's site title already says "Electrician in Garner NC", so the name is in place, but the page behind it is slow and has no h1.

## What this means for Triple Crown (and what I built)
| Winning pattern | What I built |
|---|---|
| Phone first | Tap to call in the header on every page ("Call Eric" on phones), in the hero, and as the footer headline. |
| Number with a source | A meter band under the hero: 4.9 from 44 Google reviews, 100 permitted projects, 37 in 2025, license L.32141. Each one is sourced on the page. |
| Price honesty | Pulled from the reviews instead of claimed: "explained the process and costs, no surprises, no pressure". |
| Homes and businesses | The panel schedule hero: odd circuits are home services, even circuits are business services, the way a panel door is labeled. |
| Something nobody else shows | A permit record page with projects per year, value ranges and three anonymized jobs. |
| Look different | Light paper background with navy and gold from the Triple Crown logo, instead of the dark lightning bolt look most competitors use. |
