---
layout: default
title: Pages Configuration
nav_order: 3
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
# Controls the sort order of the page in the sidebar navigation. Lower numbers appear first.
# Default: Unset (pages without nav_order appear after ordered pages, sorted alphabetically)
nav_order: 4

# When set to true, the page is hidden from the sidebar navigation.
# The page still exists and can be linked to directly.
# Default: false
nav_exclude: false

# When set to true, the page is excluded from the site's search index.
# Default: false
search_exclude: false

# Page description used in <meta name="description"> and social media previews.
# Takes priority over `excerpt`. Falls back to `description` from _config.yml if neither is set.
# Default: Unset
description: Short description used in meta tags and social previews.

# Fallback description for <meta name="description"> and social previews when
# `description` is not set. Truncated to 200 characters.
# Default: Unset
excerpt: Fallback description if description is not set.

# Sets a <link rel="canonical"> tag. Useful when the same content is accessible
# via multiple URLs.
# Default: Unset
canonical_url: https://www.example.com/canonical-page

# When set to true, adds <meta name="robots" content="noindex, nofollow"> to the page.
# Useful for draft, debug, or internal pages that should not appear in search results.
# Default: false
noindex: false

# Page-specific social card image shown when this page is shared on social platforms
# (Twitter/X, LinkedIn, Discord, Slack, etc.). Recommended size: 1200×630px.
# Overrides social_image from _config.yml for this page.
# Default: Unset
social_image: /assets/img/my-social-card.jpg

# Alt text for the social_image above. Defaults to the page title if not set.
# Default: page title
social_image_alt: "A description of the social card image"

# Article author name. Used in <meta name="author"> and article:author for posts.
# Defaults to site_author from _config.yml.
# Default: Unset
author: Author Name

# Author Twitter/X handle (without @). Used in twitter:creator for posts.
# Defaults to twitter from _config.yml.
# Default: Unset
twitter: handle

# Date the post was last modified, used in the article:modified_time meta tag.
# Only applies to the post layout.
# Default: Unset
date_last_modified: 2025-01-01
---
```
