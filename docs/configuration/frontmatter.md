---
layout: default
title: Pages Configuration
nav_order: 2
---

# Pages Configuration

Each page in your site can be configured via
[front matter](https://jekyllrb.com/docs/front-matter/), the YAML block
at the top of a Markdown file enclosed by `---` lines.

## Generic Front Matter

These are standard Jekyll front matter options used by the theme:

```yml
---
layout: default
title: Page Title Goes Here
---
```

- **`layout`**: The layout template to use for the page. This theme provides
  `default`, `page`, and `post` layouts (all render identically).
- **`title`**: The page title. It appears in the browser tab, the sidebar
  navigation, and the breadcrumbs.

## Theme Specific Front Matter

These additional front matter options are specific to this theme:

```yml
---
excerpt: Short description to include as an opening and SEO metatags.
nav_order: 4
nav_exclude: false
canonical_url: https://www.google.com
search_exclude: false
noindex: false
---
```

- **`excerpt`**: Sets the `<meta name="description">` tag for the page, which
  is used by search engines and social media previews. If not set on the site's
  index page, the `description` from `_config.yml` is used as a fallback.
- **`nav_order`**: A numeric value that controls the sort order of pages in the
  sidebar navigation. Lower numbers appear first.
- **`nav_exclude`**: When set to `true`, the page is hidden from the sidebar
  navigation. The page still exists and can be linked to directly.
- **`canonical_url`**: Sets a `<link rel="canonical">` tag in the page's
  `<head>`. Useful for SEO when the same content is accessible via multiple
  URLs.
- **`search_exclude`**: When set to `true`, the page is excluded from the
  site's search index and will not appear in search results.
- **`noindex`**: When set to `true`, a
  `<meta name="robots" content="noindex, nofollow">` tag is added to the
  page's `<head>`. This tells search engines not to index the page or follow
  its links. Useful for draft, debug, or internal pages that should not appear
  in search engine results.
