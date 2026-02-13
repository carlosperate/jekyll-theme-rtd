---
layout: default
title: Install Theme In A Jekyll Project
nav_order: 2
---

# Install Theme In A Jekyll Project

This theme is not published as a Gem. Instead, you can use it in your Jekyll
project via the `jekyll-remote-theme` plugin, which allows you to use any
GitHub-hosted theme.

## Install using jekyll-remote-theme

Add this line to your Jekyll site's `Gemfile`:

```ruby
gem "jekyll-remote-theme"
```

Add these lines to your Jekyll site's `_config.yml`:

```yaml
plugins:
  - jekyll-remote-theme

remote_theme: carlosperate/jekyll-theme-rtd
```

And then execute:

```bash
$ bundle
```

## Pin to a specific version

The latest version of `jekyll-remote-theme` also lets you select a specific
version, tag, or branch. To pin your site to a specific release:

```yaml
remote_theme: carlosperate/jekyll-theme-rtd@v1.0.0
```

This ensures your site continues to use a known version even when the theme
is updated.

## Local Jekyll to test GH Pages

If you are hosting your website in GH Pages, but testing locally with Jekyll
you might want to have a look at the official documentation for
[Testing your GitHub Pages site locally with Jekyll](https://help.github.com/en/github/working-with-github-pages/testing-your-github-pages-site-locally-with-jekyll).
