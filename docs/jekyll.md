---
layout: default
title: Install Theme In A Jekyll Project
nav_order: 2
---

# Install Theme In A Jekyll Project

**WARNING!** This theme hasn't been published as a Gem yet, so while these
instructions should be correct once it has been published, currently it won't
work.

---

You can add this port of the Read The Docs theme to your Jekyll project as
you would normally do with any other
[gem-based Jekyll theme](https://jekyllrb.com/docs/themes/).

There are two simple methods to do this:

1. Editing your project Gemfile
2. Manually installing the gem

## Edit your project Gemfile

Add this line to your Jekyll site's `Gemfile`:

```ruby
gem "jekyll-theme-rtd"
```

Add this line to your Jekyll site's `_config.yml`:

```yaml
theme: jekyll-theme-rtd
```

And then execute:

```bash
$ bundle
```

## Manually install gem

Or install the gem yourself with:

```bash
$ gem install jekyll-theme-rtd
```

And add this line to your Jekyll site's `_config.yml`:

```yaml
theme: jekyll-theme-rtd
```
