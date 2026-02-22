---
layout: default
title: Theme Configuration
nav_order: 1
---

# Theme Configuration

This theme is configured via your Jekyll or GitHub Pages' `_config.yml` file.
Below are the standard Jekyll options and the theme-specific settings
you can use to customise the look and behaviour of your site.

## Generic _config.yml configuration

These are standard Jekyll configuration options that the theme uses:

```yml
title: This is the title for your site
description: And this is a short description that goes with it.
```

## Theme Specific Configuration

The following options are specific to this theme and can be added to your
`_config.yml` to control features like the sidebar logo, navigation,
search, analytics, and more:

```yml
# Name shown in the footer copyright and in the page author meta tag.
site_author: Carlos Pereira Atencio

# Repository URL used for GitHub links (Edit on GitHub, footer revision link, bottom-left GitHub link).
repo_url: 'https://github.com/carlosperate/jekyll-theme-rtd'

# Show/hide the "Edit on GitHub" link in page breadcrumbs.
edit_on_github: true

# Set it to true if the site is build with GitHub Pages from the "docs" folder.
# This takes in consideration the "docs/" path the "Edit on GitHub" link.
github_docs_folder: true

# Logo image URL shown at the top of the left sidebar.
# If not set, the site title is shown instead.
logo: 'https://your.url/image.png'

# Custom favicon URL.
# If not set, defaults to assets/img/favicon.ico from the theme.
site_favicon: 'https://your.url/here.ico'

# Enables sticky navigation behavior for the left sidebar.
sticky_navigation: true

# Where to show previous/next navigation buttons.
# Options: none, top, bottom, both
prev_next_buttons_location: both

# Enables the search box in the sidebar.
search_enabled: true

# Google Analytics measurement ID (or legacy UA ID).
# When set, the analytics snippet is included.
google_analytics: UA-XXXXX-Y

# Adds anonymize_ip to the analytics config.
# Only applies when google_analytics is set.
google_analytics_anonymize_ip: true

# highlight.js style name loaded from cdnjs.
# Default: github-gist
hljs_style: github-gist

# List of highlight.js languages to load from cdnjs.
hljs_languages:
  - ruby
  - python
  - javascript
  - bash
  - yaml

# List of additional CSS files to load for all pages, path relative to the site base URL.
extra_css:
  - assets/css/my_custom_file.css
```
