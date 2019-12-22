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
    - [Run in a virtual machine with Vagrant](#run-in-a-virtual-machine-with-vagrant)
    - [Run locally with Ruby](#run-locally-with-ruby)
    - [Build the docs using the remote theme](#build-the-docs-using-the-remote-theme)
    - [Build the docs with MkDocs for comparison](#build-the-docs-with-mkdocs-for-comparison)
- [👨‍👩‍👧‍👦 Contributing](#-contributing)
- [⚖️ License](#%EF%B8%8F-license)


## 🚀 Using this theme with GitHub Pages

The fastest way to use this theme is with GitHub Pages, check out the
[Quick Start Guide from the user documentation](https://carlosperate.github.io/jekyll-theme-rtd/quickstart.html).

## 👩‍💻 Developer Documentation

These instructions describe two different ways to to set up your environment to
develop or edit this theme.

The theme is developed like a normal Jekyll site, and it can serve the
documentation using the theme source code located here.

### Run in a virtual machine with Vagrant

[Vagrant](https://www.vagrantup.com) provides an easy way to set up and manage
a Virtual Machine with [VirtualBox](https://www.virtualbox.org). With a single
command you can automatically create the VM with all the dependencies required
to build and sever this project.

There is a [Vagrantfile](Vagrantfile) included to run an Ubuntu VM with Ruby
and Jekyll. To set-up everything and serve the website run:

```bash
$ vagrant up
```

The first time you run this command it will take a bit longer, as it downloads
and installs everything. Subsequent runs will be much quicker.

This will serve the website at [http://localhost:4000](http://localhost:4000)
with a hot-reload enabled, so any changes made on these files will trigger a
rebuild.

#### Other Vagrant commands

To stop the virtual machine first press `Ctrl+C` to end the Jekyll process and
execute in your terminal:

```
$ vagrant halt
```

You can also SSH into the virtual machine with:

```
$ vagrant ssh
```

### Run locally with Ruby

This website has been developed using Ruby v2.5. You can install the
dependencies with:

```bash
$ gem install bundler
$ bundle install
```

### Build the docs using the remote theme

The Jekyll project here is configured with the root of this repository as the
root of the website, so when it is built locally it will see all pages as being
inside a "docs" folder, and therefore in the "docs" category in the left
navigation bar and page URLs.

On the other hand the root of the website built and served with
[GitHub Pages](https://carlosperate.github.io/jekyll-theme-rtd) is the
"docs" folder, so the left navigation bar will show the child folder as
categories and the URLs will be different.

For updating the theme documentation it can be useful to build and sever the
docs folder with the same configuration as GitHub Pages. Of course, this would
mean that the theme used will be the current snapshot of `master` on GitHub
instead of the local files, but that is not important to just preview the docs.

To do this, add the following lines to the `docs/_config.yml` file:

```yml
plugins:
  - jekyll-remote-theme
```

Then execute Jekyll from the docs folder:

```
$ vagrant up --no-provision
$ vagrant ssh
(ssh session) $ cd /vagrant/docs
(ssh session) $ bundle exec jekyll serve --host 0.0.0.0 --watch --force_polling
```

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
