# Ruby version used by GH Pages: https://pages.github.com/versions.json
FROM ruby:3.3

WORKDIR /srv/jekyll

# Pre-install gems for caching (these layers survive volume mounts
# since gems are stored in /usr/local/bundle, not /srv/jekyll)
COPY Gemfile jekyll-theme-rtd.gemspec ./
RUN bundle install

EXPOSE 4000 35729

# Re-run bundle install at startup in case dependencies have changed,
# this will be near-instant if the Gemfile hasn't been modified
CMD ["sh", "-lc", "bundle install && exec bundle exec jekyll serve --host 0.0.0.0 --watch --force_polling --livereload"]
