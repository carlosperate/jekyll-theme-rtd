---
layout: default
title: Quick Start With GitHub Pages
nav_order: 1
---

# Quick Start With GitHub Pages

There are several ways to configure the
[GitHub Pages publishing source](https://help.github.com/en/github/working-with-github-pages/configuring-a-publishing-source-for-your-github-pages-site),
I'd recommend to use the `docs` folder option, as you can keep source code
and documentation together in the master branch.

With that in mind, there are only three steps required to get your docs up an
running with this theme:
- Add your documentation markdown files a docs folder at the root of your
  repository
- Add to the docs folder a `_config.yml` file with the line:
  ```yml
  remote_theme: carlosperate/jekyll-theme-rtd
  ```
- Select your publishing source in the GitHub repository settings as indicated
  in [the official documentation](https://help.github.com/en/github/working-with-github-pages/configuring-a-publishing-source-for-your-github-pages-site).

And that's it!

There are more configuration options explained in the rest of this theme
documentation, or if you prefer it you can have a look at the
[_config.yml file used to generate this website](docs/_config.yml).
