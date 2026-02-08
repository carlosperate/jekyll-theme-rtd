# frozen_string_literal: true

Gem::Specification.new do |spec|
  spec.name       = "jekyll-theme-rtd"
  spec.version    = "0.1.0"
  spec.authors    = ["carlosperate"]
  spec.email      = ["carlosperate@embeddedlog.com"]

  spec.summary    = "Port of the Read the Docs theme to Jekyll to use with GitHub Pages."
  spec.homepage   = "https://github.com/carlosperate/jekyll-theme-rtd"
  spec.license    = "MIT"

  spec.files       = Dir[
    "_includes/**/*",
    "_layouts/**/*",
    "_sass/**/*",
    "assets/**/*",
    "LICENSE*",
    "README*"
  ]

  # To match GH Pages as much as possible dependency versions from:
  # https://pages.github.com/versions.json
  spec.add_runtime_dependency "jekyll", "~> 3.10"

  spec.add_development_dependency "github-pages", "~> 232"
  spec.add_development_dependency "jekyll-remote-theme", "~> 0.4.3"

  # Others unrelated to GH pages
  spec.add_development_dependency "jekyll-livereload", "~> 0.2.2"
  spec.add_development_dependency "bundler", "~> 2.0"
  spec.add_development_dependency "rake", "~> 13.0"
end
