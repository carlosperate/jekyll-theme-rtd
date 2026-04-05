# frozen_string_literal: true

Gem::Specification.new do |spec|
  spec.name       = "jekyll-theme-rtd"
  spec.version    = "1.3.0"
  spec.authors    = ["carlosperate"]
  spec.email      = ["carlosperate@embeddedlog.com"]

  spec.summary    = "Port of the Read the Docs theme to Jekyll to use with GitHub Pages."
  spec.homepage   = "https://github.com/carlosperate/jekyll-theme-rtd"
  spec.license    = "BSD-2-Clause"
  spec.metadata      = {
    "bug_tracker_uri"   => "https://github.com/carlosperate/jekyll-theme-rtd/issues",
    "documentation_uri" => "https://carlosperate.github.io/jekyll-theme-rtd/",
    "source_code_uri"   => "https://github.com/carlosperate/jekyll-theme-rtd",
  }

  spec.files       = Dir[
    "_includes/**/*",
    "_layouts/**/*",
    "assets/**/*",
    "LICENSE*",
    "README*"
  ]

  # To match GH Pages as much as possible dependency versions from:
  # https://pages.github.com/versions.json
  spec.add_runtime_dependency "jekyll", "~> 3.10"

  spec.add_development_dependency "github-pages", "~> 232"
  # Needed to change to use version specified in the Gemfile so that we can use local paths with "remote_theme"
  # https://github.com/benbalter/jekyll-remote-theme/pull/120
  # gem "jekyll-remote-theme", github: "benbalter/jekyll-remote-theme", ref: "048c7ec68ac6205aa684a3a72d4f02a5b0b4916d"
  spec.add_development_dependency "jekyll-remote-theme", "~> 0.4.3"

  # Others unrelated to GH pages
  spec.add_development_dependency "jekyll-livereload", "~> 0.2.2"
  spec.add_development_dependency "bundler", "~> 2.0"
  spec.add_development_dependency "rake", "~> 13.0"
end
