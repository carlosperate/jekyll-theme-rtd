# Ruby version used by GH Pages: https://pages.github.com/versions.json
FROM ruby:3.3

WORKDIR /srv/jekyll

# Pre-install gems for caching (these layers survive volume mounts
# since gems are stored in /usr/local/bundle, not /srv/jekyll)
COPY Gemfile jekyll-theme-rtd.gemspec ./
RUN bundle install

# Inline entrypoint script
RUN cat > /usr/local/bin/entrypoint.sh <<'EOF' && chmod +x /usr/local/bin/entrypoint.sh
#!/usr/bin/env bash
set -euo pipefail

bundle install

case "${1:-serve}" in
  build)
    exec bundle exec jekyll build
    ;;
  serve)
    shift || true
    exec bundle exec jekyll serve --host 0.0.0.0 --watch --force_polling --livereload "$@"
    ;;
  *)
    exec "$@"
    ;;
esac
EOF

EXPOSE 4000 35729

ENTRYPOINT ["/usr/local/bin/entrypoint.sh"]
CMD ["serve"]
