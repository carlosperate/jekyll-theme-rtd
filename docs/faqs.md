---
layout: default
title: What is All This? (FAQs)
nav_order: 3
---

# What is All This? (FAQs)

## What is Jekyll, Read The Docs, GitHub Pages or why do I need to know any of this?

Well, you don't! For a quick walkthrough to get your docs up an running with
this theme see the [Quick Start Guide](quickstart.html).

If you are interested to know more about all this continue reading :)

- [Jekyll](https://jekyllrb.com/) is a static site generator, you give it some
markdown files, select a theme, and it builds a static website.

But you still need to find a way to host it, and that's where GitHub Pages
enters the game.

- [GitHub Pages](https://pages.github.com) is a service from
[GitHub](https://github.com) that allows you to easily build and host a website
from a GitHub repository.

There are a couple of different ways to configure GitHub pages, the easiest
would be to create a `docs` folder, add some markdown files, and with a couple
of clicks
[configure GitHub Pages](https://help.github.com/en/github/working-with-github-pages/configuring-a-publishing-source-for-your-github-pages-site)
to automatically build and publish a website for your project!

GitHub Pages uses Jekyll underneath, so a GitHub Pages theme is a Jekyll theme.

- [Read The Docs](https://readthedocs.org/) is service offering free hosting
for project documentation. It's very flexible, but the easiest way to use
it is with [Sphinx](https://www.sphinx-doc.org/). Similarly to Jekyll, Sphinx
is also a static site generator, but focused on project documentation, and Read
The Docs provides a really nice theme for it.

I love the
[Read The Docs theme for Sphinx](https://sphinx-rtd-theme.readthedocs.io), but
you still have to set up a Sphinx project, a Read The Docs account, and
configure the integration to automatically publish your documentation from
your GitHub repository.

### So...?

For a project that is already in GitHub nothing beats the simplicity of GitHub
Pages, and so this theme is a port of Read The Docs Sphinx theme to Jekyll, so
that it can be easily used with GitHub Pages.

## Other FAQs

We don't have Frequently Asked Questions yet, if you have any please
[open a new issue in the theme GitHub repository](https://github.com/carlosperate/jekyll-theme-rtd/issues/new).
