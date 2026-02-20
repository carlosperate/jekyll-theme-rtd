---
layout: default
title: Developer Docs
nav_order: 3
---

# Developer Documentation

This page is meant for developers who want to contribute to the development
of this theme or build their own customisations.

The theme is developed like a normal Jekyll site, and it uses the
[docs folder in the GitHub repository](https://github.com/carlosperate/jekyll-theme-rtd/tree/main/docs)
as the markdown content to generate this website.

And the repository with all the theme source code is at:
[https://github.com/carlosperate/jekyll-theme-rtd](https://github.com/carlosperate/jekyll-theme-rtd)

## 🚀 Run with Docker

[Docker](https://www.docker.com) provides an easy way to set up the
development environment without installing Ruby or any other dependencies
on your machine. With two simple commands you can build and serve this project.

A [Dockerfile](Dockerfile) is included to run an environment with Ruby and
Jekyll. First, build the Docker image:

```bash
$ docker build -t jekyll-theme-rtd .
```

And then serve the website:

```bash
$ docker run --rm -p 4000:4000 -p 35729:35729 -v $(pwd):/srv/jekyll jekyll-theme-rtd
```

This will serve the website at [http://localhost:4000](http://localhost:4000)
with live-reload enabled, so any changes made on these files will trigger a
rebuild and automatically refresh the browser.

Building the docker image pre-installs the required Ruby Gems, but the built
image still goes triggers a gem installation step every time it is launched,
in case there has been changes. It's recommended to rebuild the image if there
are any changes made to the `Gemfile` or gemspec dependencies.

### Build the docs using the remote theme

This method is meant to replicate how GitHub Pages builds the "docs" folder for
[https://carlosperate.github.io/jekyll-theme-rtd](https://carlosperate.github.io/jekyll-theme-rtd).

There are two main differences with this method:

1. The root directory is the "docs" folder instead of the project root
  directory, so the navigation hierarchy is different.
2. This method uses the `remote_theme` Jekyll plugin, so it uses the files
  currently pushed and available in the GitHub repository `main` branch,
  not the local files from your machine.

To do this, we add the `-w /srv/jekyll/docs` to the docker command:

```bash
$ docker run --rm -p 4000:4000 -p 35729:35729 -v $(pwd):/srv/jekyll -w /srv/jekyll/docs jekyll-theme-rtd
```

And, as before, the website is served at [http://localhost:4000](http://localhost:4000).

## 🐛 Debug Config

A debug utility page is included in the `docs/` folder that prints all
Jekyll, Liquid, and GitHub Pages variables at build time. It is very useful
for inspecting `site.github.*` metadata and troubleshooting configuration
issues during development.

See the
[Debug Config](https://carlosperate.github.io/jekyll-theme-rtd/configuration/debug.html)
docs page for full details, usage instructions, and security considerations.

The source file is at repository [`docs/debug.html`](debug.html) file.

## 🆚 Build the docs with MkDocs for comparison

As this theme is a port from the MkDocs port, it can be useful to run
MkDocs to build the docs and compare the original MkDocs theme vs
this Jekyll port. A `mkdocs.yml` file is included to configure the project.

We recommend using a virtual environment to run the following steps:

```bash
$ pip install mkdocs==1.0.4 Jinja2==2.11.3 MarkupSafe==1.1.1 Markdown==3.1.1 "setuptools<82"
$ mkdocs serve
```

This currently needs Python 3.9, but as we update the theme to include the
latest changes from MkDocs version it'll be able to work with newer versions.

## 👨‍👩‍👧‍👦 Contributing

Bug reports and pull requests are welcome on GitHub at
https://github.com/carlosperate/jekyll-theme-rtd.

This project is intended to be a safe, welcoming space for collaboration, and
contributors are expected to adhere to the
[Contributor Covenant](http://contributor-covenant.org) code of conduct.

## ⚖️ License

Information about the license can be found in the
[repository README file](https://github.com/carlosperate/jekyll-theme-rtd/tree/main?tab=readme-ov-file#%EF%B8%8F-license).
