# Read The Docs Theme for Jekyll and GitHub Pages

Port of the Read the Docs theme to Jekyll to use with GitHub Pages.

![screenshot](assets/img/screenshot.png)

This theme is currently a **Work-In-Progress** but, while some things might be
broken, it should be already usable.

This theme is ported from the MkDocs port of the Read The Docs Sphinx theme.
Full license and copyright information can be found in the
[License](#license) section.


## Using with GitHub Pages

Add a `_config.yml` file to your GitHub pages repository (`master`/`gh-pages`
branch or inside a `docs` folder, depending on your GitHub repository settings)
with this line:

```yml
remote_theme: carlosperate/jekyll-theme-rtd
```

There are more configuration options explain in the docs, or you can have a
look at the [_config.yml file from this repo](docs/_config.yml).


## Add this theme to your Jekyll project

Add this line to your Jekyll site's `Gemfile`:

```ruby
gem "jekyll-theme-rtd"
```

And add this line to your Jekyll site's `_config.yml`:

```yaml
theme: jekyll-theme-rtd
```

And then execute:

```bash
$ bundle
```

Or install it yourself as:

```bash
$ gem install jekyll-theme-rtd
```


## Development Instructions

These instructions describe two different ways to to set up your environment to
develop or edit this theme.

The theme is developed like a normal Jekyll site, and it can serve the
documentation using the theme source code located here.


### Run with Vagrant and a Virtual Machine

[Vagrant](https://www.vagrantup.com) provides an easy way to set up and manage
a Virtual Machine with [VirtualBox](https://www.virtualbox.org). With a single
command you can automatically create the VM with all the dependencies required
to build and sever this project.

There is [Vagrantfile](Vagrantfile) included to run an Ubuntu VM with Ruby and
Jekyll. To set-up everything and serve the website run:

```bash
$ vagrant up
```

The first time you run this command it will take a bit longer, as it downloads
and installs everything. Subsequents runs will be much quicker.

This will serve the website at [http://localhost:4000](http://localhost:4000)
with a hot-reload enabled, so any changes made on this files will trigger a
rebuild.

#### Other Vagrant commands

To stop the virtual machine first press `Ctrl+C` to end the Jekyll process and
execute in your terminal:

```
vagrant halt
```

You can also SSH into the virtual machine with:

```
vagrant ssh
```

### Run locally with Ruby

This website has been developed using Ruby v2.5.
You can install the dependencies with:

```bash
$ gem install bundler
$ bundle install
```

### Build with MkDocs for comparison

As this theme has been ported from the MkDocs port, it can be useful to run
MkDocs on the same markdown files and compare its output to the Jekyll
output. A `mkdocs.yml` file is included to configure the project.

Pipenv has been used in this case to manage Python dependencies:

```bash
$ pip install pipenv
$ pipenv install
$ pipenv run mkdocs build
$ cd _site_mkdocs
$ pipenv run python -m http.server 8080
```


## Contributing

Bug reports and pull requests are welcome on GitHub at https://github.com/carlosperate/jekyll-theme-rtd.

This project is intended to be a safe, welcoming space for collaboration, and contributors are expected to adhere to the [Contributor Covenant](http://contributor-covenant.org) code of conduct.


## License

The original theme is from
[Read The Docs](https://github.com/readthedocs/sphinx_rtd_theme). Copyright (c)
2013-2018 Dave Snider, Read the Docs, Inc. & contributors and released under
the [MIT License](https://github.com/readthedocs/sphinx_rtd_theme/blob/0.4.2/LICENSE).

This theme is based on the [MkDocs](https://github.com/mkdocs/mkdocs)
[`readthedocs` port](https://github.com/mkdocs/mkdocs/tree/1.0.4/mkdocs/themes/readthedocs).
Copyright © 2014, Tom Christie, all rights reserved, and released under the
[BSD 2-Clause "Simplified" License](https://github.com/mkdocs/mkdocs/blob/1.0.4/LICENSE).

The theme is available as open source under the terms of the [MIT License](LICENSE).
