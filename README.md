# jekyll-theme-rtd

Port of the Read the Docs theme to Jekyll to use with GitHub Pages.

```
vagrant up
vagrant ssh
(in ssh session) > cd /vagrant && bundle exec jekyll serve --host 0.0.0.0 --watch --force_polling
```

This is still a **Work-In-Progress** theme and things will **not** work well.

This theme is ported from the MkDocs port of the Read The Docs Sphinx theme.
License and copyright for the theme can be found in the
[LICENSE-mkdocs](LICENSE-mkdocs) file.

To compare the output from MkDocs:

```
mkdocs build
```

-----

Welcome to your new Jekyll theme! In this directory, you'll find the files you need to be able to package up your theme into a gem. Put your layouts in `_layouts`, your includes in `_includes`, your sass files in `_sass` and any other assets in `assets`.

To experiment with this code, add some sample content and run `bundle exec jekyll serve` – this directory is setup just like a Jekyll site!

TODO: Delete this and the text above, and describe your gem


## Installation

Add this line to your Jekyll site's `Gemfile`:

```ruby
gem "jekyll-theme-rtd"
```

And add this line to your Jekyll site's `_config.yml`:

```yaml
theme: jekyll-theme-rtd
```

And then execute:

    $ bundle

Or install it yourself as:

    $ gem install jekyll-theme-rtd

## Usage

TODO: Write usage instructions here. Describe your available layouts, includes, sass and/or assets.

## Contributing

Bug reports and pull requests are welcome on GitHub at https://github.com/carlosperate/jekyll-theme-rtd. This project is intended to be a safe, welcoming space for collaboration, and contributors are expected to adhere to the [Contributor Covenant](http://contributor-covenant.org) code of conduct.

## Development

To set up your environment to develop this theme, run `bundle install`.

Your theme is setup just like a normal Jekyll site! To test your theme, run `bundle exec jekyll serve` and open your browser at `http://localhost:4000`. This starts a Jekyll server using your theme. Add pages, documents, data, etc. like normal to test your theme's contents. As you make modifications to your theme and to your content, your site will regenerate and you should see the changes in the browser after a refresh, just like normal.

When your theme is released, only the files in `_layouts`, `_includes`, `_sass` and `assets` tracked with Git will be bundled.
To add a custom directory to your theme-gem, please edit the regexp in `rtd.gemspec` accordingly.

## License

The theme is available as open source under the terms of the [MIT License](LICENSE).
