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

```yaml
# Name shown in the footer copyright and in the page author meta tag.
# Default: Unset
site_author: Carlos Pereira Atencio

# Language for the site, used in the html lang attribute.
# Should be a single BCP 47 language tag.
# Default: en
lang: en

# Locale for Open Graph tags. Accepts both hyphen and underscore formats
# (e.g. en_US or en-US, fr_FR or fr-FR).
# Default: en_US
locale: en_US

# Repository URL used for GitHub links (like Edit on GitHub,
# footer revision link, bottom-left GitHub link).
# Default Jekyll: Unset, so the links will not appear.
# Default GH Pages: Auto-detected, so links will appear if unset.
# Set to `false` to disable the GitHub links entirely.
repo_url: 'https://github.com/carlosperate/jekyll-theme-rtd'

# Show/hide the "Edit on GitHub" link in page breadcrumbs.
# Default Jekyll: Unset, so the link will not appear.
# Default GH Pages: Auto-detected, so the link will appear if unset.
# Set to `false` to disable the "Edit on GitHub" link specifically.
edit_on_github: true

# GitHub branch to use for the "Edit on GitHub" links.
# Default Jekyll: "main"
# Default GH Pages: Auto-detected, so the default branch will be used.
github_branch: main

# Logo image URL shown at the top of the left sidebar.
# If not set, the site title is shown instead.
# Default: Unset
logo: 'path/to/your_image.png'

# Custom favicon URL.
# Default: assets/img/favicon.ico from the theme if it exist, otherwise unset.
favicon: 'path/to/your_favicon.ico'

# Enables sticky navigation behaviour for the left sidebar.
# Default: false
sticky_navigation: true

# Where to show previous/next navigation buttons.
# Options: none, top, bottom, both
# Default: none
prev_next_buttons_location: both

# Enables the search box in the sidebar.
# Default: true
search_enabled: true

# highlight.js style name loaded from cdnjs.
# Default: github
hljs_style: github

# List of highlight.js languages to load from cdnjs.
# Default: Empty, so no additional languages loaded.
hljs_languages:
  - ruby
  - python
  - javascript
  - bash
  - yaml

# Enables admonitions (GitHub-style blockquote callouts like [!NOTE], [!WARNING], etc).
# Default: true
admonitions: true

# Version string to show in the sidebar.
# Default: Unset
display_version: 1.2.0

# Social media card image shown when the site is shared on social platforms
# (Twitter/X, LinkedIn, Discord, Slack, etc.). Recommended size: 1200×630px.
# Used as the default for all pages; individual pages can override it via
# the `social_image` front matter field.
# Default: site logo if set, otherwise no image (text-only card).
social_image: 'path/to/your_social_card.jpg'

# Alt text for the social card image above.
# Default: site title
social_image_alt: 'A description of the social card image'

# Twitter/X handle for the site (without the @).
# Used in the twitter:site meta tag.
# Default: Unset
twitter: yourtwitterhandle

# Mastodon/Fediverse handle for the site, in the full @user@instance format.
# Used in the fediverse:creator meta tag for Mastodon profile link verification.
# Default: Unset
fediverse: '@you@mastodon.social'

# List of additional CSS & JS files to load for all pages, path relative to the site base URL.
# Default: Empty, so no additional files loaded.
extra_javascript:
  - assets/js/my_custom_file.js
extra_css:
  - assets/css/my_custom_file.css
```
