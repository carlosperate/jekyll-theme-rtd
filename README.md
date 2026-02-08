# Read The Docs Theme for Jekyll and GitHub Pages

Port of the Read the Docs theme to Jekyll that can be used with GitHub Pages.

You can preview it in the
[user documentation](https://carlosperate.github.io/jekyll-theme-rtd):

![theme screenshot](docs/assets/img/screenshot.png)

The original [Read The Docs](https://sphinx-rtd-theme.readthedocs.io)
theme was created for [Sphinx](https://www.sphinx-doc.org/), and so it is
designed specifically for documentation.

Combined with [GitHub Pages](https://pages.github.com) it's a great and easy
way to document your projects!

Check out the [quick start guide]() to see how easy it is to 

### 🚧 Warning!

This theme is currently a **Work-In-Progress** but, while some things might be
broken, it should be already usable.

Missing features are listed in the GitHub issues with the
[to-do label](https://github.com/carlosperate/jekyll-theme-rtd/issues?q=is%3Aissue+is%3Aopen+label%3Ato-do),
and any known issues are listed with the
[bug label](https://github.com/carlosperate/jekyll-theme-rtd/issues?q=is%3Aissue+is%3Aopen+label%3Abug).

Contributions are very welcomed!


## 🗂️ Readme Contents

This README contains mostly the developer documentation to edit this theme.

To learn how to use this theme for your own website or docs check out the
[user documentation](https://carlosperate.github.io/jekyll-theme-rtd).

- [🚀 Using this theme with GitHub Pages](#-using-this-theme-with-github-pages)
- [👩‍💻 Developer Documentation](#-developer-documentation)
    - [Run with Docker](#run-with-docker)
    - [Build the docs using the remote theme](#build-the-docs-using-the-remote-theme)
    - [Build the docs with MkDocs for comparison](#build-the-docs-with-mkdocs-for-comparison)
- [👨‍👩‍👧‍👦 Contributing](#-contributing)
- [⚖️ License](#%EF%B8%8F-license)


## 🚀 Using this theme with GitHub Pages

The fastest way to use this theme is with GitHub Pages, check out the
[Quick Start Guide from the user documentation](https://carlosperate.github.io/jekyll-theme-rtd/quickstart.html).

## 👩‍💻 Developer Documentation

These instructions describe different ways to to set up your environment to
develop or edit this theme.

The theme is developed like a normal Jekyll site, and it uses the theme
documentation as the site content.

### Run with Docker

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

### Build the docs with MkDocs for comparison

As this theme has been ported from the MkDocs port, it can be useful to run
MkDocs on the documentation markdown file and compare its output to the Jekyll
output. A `mkdocs.yml` file is included to configure the project.

Pipenv has been used to manage Python dependencies:

```bash
$ pip install pipenv
$ pipenv install
$ pipenv run mkdocs build
$ cd _site_mkdocs
$ pipenv run python -m http.server 8080
```


## 👨‍👩‍👧‍👦 Contributing

Bug reports and pull requests are welcome on GitHub at
https://github.com/carlosperate/jekyll-theme-rtd.

This project is intended to be a safe, welcoming space for collaboration, and
contributors are expected to adhere to the
[Contributor Covenant](http://contributor-covenant.org) code of conduct.


## ⚖️ License

The original theme is from
[Read The Docs](https://github.com/readthedocs/sphinx_rtd_theme). Copyright ©
2013-2018 Dave Snider, Read the Docs, Inc. & contributors, and released under
the [MIT License](LICENSE-rtd).

This theme is based on the [MkDocs](https://github.com/mkdocs/mkdocs)
[`readthedocs` port](https://github.com/mkdocs/mkdocs/tree/1.0.4/mkdocs/themes/readthedocs).
Copyright © 2014, Tom Christie, all rights reserved, and released under the
[BSD 2-Clause "Simplified" License](LICENSE-mkdocs).

The theme modifications to port it Jekyll can be seen
[here](https://github.com/carlosperate/jekyll-theme-rtd/compare/dddce9f13fde24c03aee4533158c43091120d47e...master).
This and all new features are released under the
[BSD 2-Clause "Simplified" License](LICENSE).
