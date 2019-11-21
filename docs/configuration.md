---
layout: default
title: Theme Configuration
nav_order: 2
---

# Configuring the theme

The docs should have an index page.

## _config.yml


```yml
title: Read The Docs Jekyll Theme
description: Port of the Read the Docs theme to Jekyll to use with GitHub Pages.

# Specific to this theme
site_author: Carlos Pereira Atencio
repo_url: 'https://github.com/carlosperate/jekyll-theme-rtd'
edit_on_github: true
github_docs_folder: true
logo: 'https://your.url/image.png'
site_favicon: 'https://your.url/here.ico'
sticky_navigation: true
prev_next_buttons_location: None
prev_next_buttons_location: top
prev_next_buttons_location: bottom
prev_next_buttons_location: both
search_enabled: true
google_analytics: UA-XXXXX-Y
google_analytics_anonymize_ip: true
# The highlight.js library provides 79 different colours for their syntax highlighting. The default is github-gist.
hljs_style: github-gist
```

## Front Matter

```yml
---
layout: default
title: Page Title Goes Here
---

```


```yml
---
excerpt: Short description to include as an opening and SEO metatags.
nav_order: 4
nav_exclude: false
canonical_url: https://www.google.com
search_exclude: false
---
```