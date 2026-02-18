---
layout: default
title: Debug Config
nav_order: 3
---

# 🐛 Debug Config

This theme repository includes a **debug utility page** that prints every
Jekyll, Liquid, and GitHub Pages variable available at build time, together
with live demonstrations of all Liquid filters. It is extremely useful for
troubleshooting builds — especially on GitHub Pages, where many variables
(under the `site.github.*` namespace) are populated automatically and may
differ from a local environment.

> **Note:** The debug page lives in the
> [`docs/`](https://github.com/carlosperate/jekyll-theme-rtd/tree/main/docs)
> folder and is **not** bundled with the theme itself. Theme users who want
> to use it must copy the file into their own project.

## Where to find it

The debug page source is at
[`docs/debug.html`](https://github.com/carlosperate/jekyll-theme-rtd/blob/main/docs/debug.html)
in the theme repository.

## How to use it

### 1. Copy the file

Download or copy
[`debug.html`](https://github.com/carlosperate/jekyll-theme-rtd/blob/main/docs/debug.html)
into your site's root (or wherever your Jekyll source files live):

```text
your-project/
├── _config.yml
├── index.md
├── debug.html   ← place it here
└── ...
```

### 2. Enable the page

Open `debug.html` and find this line near the top (after the front matter and
the HTML comment):

```liquid
{% raw %}{% assign debug_enabled = false %}{% endraw %}
```

Change `false` to `true`:

```liquid
{% raw %}{% assign debug_enabled = true %}{% endraw %}
```

That is the **only** change needed. Rebuild your site and navigate to
`/debug.html`.

### 3. Disable or remove when done

> ⚠️ **Do not leave this page enabled on a public site.**

When you are finished debugging, either:

- Set the variable back to `false`, **or**
- Delete `debug.html` from your project entirely.

## What does it show?

The page is divided into the following sections:

| # | Section | Description |
|---|---------|-------------|
| 1 | Global Variables | `content` (layout-only) |
| 2 | Jekyll Variables | `jekyll.version`, `jekyll.environment` |
| 3 | Theme Variables | `theme.*` (gem-based themes) |
| 4 | Site Variables (Built-in) | Core `site.*` values |
| 5 | Site Variables (Theme config) | Theme-specific `_config.yml` settings |
| 6 | `site.github.*` Variables | GitHub Pages metadata — repository info, URLs, org members, etc. |
| 7 | Page Variables | `page.*` for the current page |
| 8 | Layout Variables | `layout.*` for the active layout |
| 9 | Liquid Filters | Live input → output demos for URL, date, string, HTML, array, math, and other filters |
| 10 | Full Site Dump | `site \| inspect` (collapsed) |
| 11 | Environment Info | Markdown engine, highlighter, timezone, host, port |

## Safety features

The page ships with several safeguards:

- **`noindex: true`** — Adds a `<meta name="robots" content="noindex, nofollow">`
  tag so search engines will not index the page.
- **`search_exclude: true`** — Keeps the page out of the site's built-in
  search index.
- **`nav_exclude: true`** — Hides the page from the sidebar navigation.
- **Disabled by default** — The page renders a "disabled" message unless you
  explicitly set the `debug_enabled` variable to `true` inside the file.

## Security considerations

Even with the safeguards above, the page **will expose information you may not
want to share publicly** when enabled:

- **Repository metadata** — `site.github | inspect` includes contributor
  lists, organisation members, and other GitHub API data.
- **Filesystem paths** — `site.source` and `site.destination` reveal server
  directory structures.
- **Full config dump** — `site | inspect` shows every value in `_config.yml`,
  which may include API keys or tokens if misconfigured.

**Always disable or remove the file before deploying to production.**
