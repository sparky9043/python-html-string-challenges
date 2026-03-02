# Python HTML String Manipulation Challenges

5 Python challenges to build and modify a minimal HTML page using string methods
and concatenation only. No parsers, no libraries — pure string primitives.

## Rules
- Only string methods (.replace, .find, .rfind, .split, .index, .count, etc.) are allowed
- String concatenation with + and += is allowed
- f-strings may be used to build values before insertion
- Converting the string to a list to index elements is NOT allowed
- No imports or external libraries of any kind

## Challenges

| # | Challenge | Branch | Status |
|---|-----------|--------|--------|
| 1 | Update Page Metadata | `challenge/01-metadata` | ✅ Done |
| 2 | Update Stylesheet and Script Sources | `challenge/02-assets` | ✅ Done |
| 3 | Inject Heading Tags | `challenge/03-headings` | ✅ Done |
| 4 | Add Paragraph and Image Tags | `challenge/04-content` | ⏳ Pending |
| 5 | Full Page Builder | `challenge/05-full-page` | ⏳ Pending |

## Outputs

### Challenge 1 — Update Page Metadata

**Concepts:** `.replace()`, f-strings, string concatenation

**Solution file:** `challenge_01_metadata.py`

**HTML output file:** `html_outputs/challenge_01_output.html`

**Terminal output:**

![Challenge 1 Terminal](screenshots/challenge_01_terminal.png)

**Browser preview:** Open `html_outputs/challenge_01_output.html` in a browser to verify
the updated `lang` attribute and `<title>` tag render correctly.

### Challenge 2 — Update Stylesheet and Script Sources

**Concepts:** `.find()`, `.index()`, string slicing with computed positions, concatenation

**Solution file:** `challenge_02_stylesheets_and_scripts.py`

**HTML output file:** `html_outputs/challenge_02_output.html`

**Terminal output:**

![Challenge 2 Terminal](screenshots/challenge_02_terminal.png)

**Browser preview:** After opening the HTML file in a browser, use **View Page Source** to confirm the `href` and `src` values were updated correctly. Your terminal screenshot must show the printed `<link>` and `<script>` lines clearly enough to read the new filenames.


### Challenge 3 — Inject Heading Tags

**Concepts:** `.find()`, `.split()` on a specific separator, string concatenation, multi-line string building

**Solution file:** `challenge_03_headings.py`

**HTML output file:** `html_outputs/challenge_03_output.html`

**Terminal output:**

![Challenge 3 Terminal](screenshots/challenge_03_terminal.png)

**Browser preview:**  Open the HTML output in a browser — the `<h1>`, `<h2>`, and `<h3>` headings must be visible on the page with correct visual hierarchy. A blank page usually means the heading tags ended up outside `<body>` or contain a syntax error — check the source.

