# Google Search (google.com) – Test Cases

Scope: public google.com home page and web search, signed out, English (`hl=en`), desktop Chrome unless noted.
"Auto" = covered by the automated suite in `tests/` (test name prefix `test_tcNN_`).

## Home page

| ID | Title | Steps | Expected result | Priority | Auto |
|----|-------|-------|-----------------|----------|------|
| TC01 | Home page loads | Open https://www.google.com | Page loads, title is "Google" | P1 | Yes |
| TC02 | Logo displayed | Open home page | Google logo / Doodle is visible | P2 | Yes |
| TC03 | Search box usable | Click the search box | Box is visible and receives focus | P1 | Yes |
| TC04 | Search buttons present | Open home page | "Google Search" and "I'm Feeling Lucky" buttons exist | P2 | Yes |
| TC05 | Gmail link | Check "Gmail" link in header | Link visible, points to mail.google.com | P3 | Yes |
| TC06 | Images link | Check "Images" link in header | Link visible, opens Google Images | P3 | Yes |
| TC07 | Sign in link | Check "Sign in" button | Visible, points to accounts.google.com | P2 | Yes |
| TC08 | Footer legal links | Check footer | "Privacy" and "Terms" link to policies.google.com | P3 | Yes |
| TC09 | Empty search | Focus empty box, press Enter | Stays on home page, no results page | P2 | Yes |
| TC10 | Mobile layout | Resize to 390×844 | Search box still visible and usable | P2 | Yes |

## Search

| ID | Title | Steps | Expected result | Priority | Auto |
|----|-------|-------|-----------------|----------|------|
| TC11 | Search with Enter | Type "playwright testing", press Enter | URL has `/search?q=playwright+testing`, organic results listed | P1 | Yes |
| TC12 | Query retained | Search "selenium vs playwright" | Results page search box shows the same query | P2 | Yes |
| TC13 | Results title | Search "pytest fixtures" | Tab title contains the query | P3 | Yes |
| TC14 | Special characters | Search `c++ & c# <tags>` | Results page loads, no error / no script injection | P1 | Yes |
| TC15 | Long query | Search a ~250-char query | Page loads gracefully (results or message) | P2 | Yes |
| TC16 | Gibberish query | Search a random gibberish string | Results page loads without error (fuzzy results or a "did not match any documents" message) | P2 | Yes |
| TC17 | Calculator | Search `12*12` | Calculator answer `144` is shown | P3 | Yes |
| TC18 | Autocomplete | Type "weather in" slowly | Suggestion dropdown with options appears | P2 | Yes |
| TC19 | Images tab | Search "golden retriever", click Images | Image results shown (`udm=2` / `tbm=isch`) | P2 | Yes |
| TC20 | Pagination | Search "python unittest", click Next | Page 2 loads (`start=10`) | P3 | Yes |

## Manual-only cases

| ID | Title | Steps | Expected result | Priority |
|----|-------|-------|-----------------|----------|
| TC21 | Voice search | Click microphone icon, allow mic, speak a query | Spoken query is searched | P3 |
| TC22 | Search by image (Lens) | Click camera icon, upload an image | Lens results for the image | P3 |
| TC23 | I'm Feeling Lucky | Type "wikipedia", click "I'm Feeling Lucky" | Redirects straight to the top result | P3 |
| TC24 | Keyboard navigation | Use Tab / arrow keys through header, box, suggestions | All controls reachable, visible focus ring | P2 |
| TC25 | Screen reader | Use NVDA/VoiceOver on home page | Search box announced as "Search" combobox | P2 |
| TC26 | Signed-in state | Sign in, open home page | Avatar shown instead of "Sign in" | P2 |
| TC27 | Language switch | Open `/?hl=fr` | UI text displayed in French | P3 |
| TC28 | Cross-browser | Repeat TC01–TC11 in Firefox, Safari, Edge | Same behaviour | P2 |
| TC29 | Performance | Load home page with DevTools/Lighthouse | LCP < 2.5s on broadband | P3 |
| TC30 | Consent banner (EU) | Open from an EU IP in a fresh profile | Consent dialog shown; Accept/Reject both work | P2 |
