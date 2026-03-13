---
layout: default
title: Changelog
nav_order: 5
---

# Changelog

## V1.1.0

- Sync theme with the upstream version from MkDocs [v1.2](https://github.com/mkdocs/mkdocs/releases/tag/1.2).
    - Includes following commits since last time it was synced:
        - [mkdocs/mkdocs@273e3ba](https://github.com/mkdocs/mkdocs/commit/273e3baa8e47fa5d121402d98757d3f5a5510383)
        - [mkdocs/mkdocs@63b3eb5](https://github.com/mkdocs/mkdocs/commit/63b3eb5a1fbfdfc0e28ee54e5dcc3b714487b1b0)
        - [mkdocs/mkdocs@dd903d3](https://github.com/mkdocs/mkdocs/commit/dd903d3092a9288f6c1ab2291b0a176a48351611)
        - [mkdocs/mkdocs@1beaf22](https://github.com/mkdocs/mkdocs/commit/1beaf2224534453ab07d34ceded77b4596b98283)
        - [mkdocs/mkdocs@eb31d4c](https://github.com/mkdocs/mkdocs/commit/eb31d4c0d70259755b779bd6bf34609ac2adca7b)
    - Doesn't include:
        - [mkdocs/mkdocs@34a425e](https://github.com/mkdocs/mkdocs/commit/34a425e5a53aff5a13b2ef5908bcfc75ce35bdc4)
            - Not needed with the Jekyll changes
        - [mkdocs/mkdocs@e1b77ab](https://github.com/mkdocs/mkdocs/commit/e1b77ab66e8305b5f0373b4842b50d2618390a96)
            - Theme localisation not supported
        - [mkdocs/mkdocs@a8ec4b6](https://github.com/mkdocs/mkdocs/commit/a8ec4b64a3837d5385a15304ae9656ed6236aea6)
            - Theme localisation not supported
        - [mkdocs/mkdocs@80feaf0](https://github.com/mkdocs/mkdocs/commit/80feaf03a42dacdd0740259b647014d5f0f9d839)
            - GAnalytics change within MkDocs, not needed.
- Added a test script to create screenshots of the theme and compare them with the previous version, to easily spot visual changes.

## v1.0.0

Initial stable release.
