---
layout: default
title: Changelog
nav_order: 5
---

# Changelog

## v1.2.0

- Sync theme with the upstream version from MkDocs [v1.6.1](https://github.com/mkdocs/mkdocs/releases/tag/1.4).
    - Includes following commits since last time it was synced:
        - [mkdocs/mkdocs@4d1d1c1](https://github.com/mkdocs/mkdocs/commit/4d1d1c1ba5065dde50ae7ddab4b0a85305781047)
        - [mkdocs/mkdocs@fa52d3a](https://github.com/mkdocs/mkdocs/commit/fa52d3ae71251ae1c760cbe9b31caced816573d1)
        - [mkdocs/mkdocs@cdf8a26](https://github.com/mkdocs/mkdocs/commit/cdf8a26cafa6af6cc78a45766dfec235bd7286cc)
        - [mkdocs/mkdocs@82bd8ba](https://github.com/mkdocs/mkdocs/commit/82bd8ba5ff177347d094b095bd623a85aaa4c80f)
        - [mkdocs/mkdocs@f3f6631](https://github.com/mkdocs/mkdocs/commit/f3f6631d2abddf1b8c3bbfd611a4d1842aede098)
        - [mkdocs/mkdocs@97440ca](https://github.com/mkdocs/mkdocs/commit/97440caf635579712de87f962520fd96b4d716f0)
        - [mkdocs/mkdocs@ea1c6c4](https://github.com/mkdocs/mkdocs/commit/ea1c6c468d6700c88875189421640634cc408e62)
        - [mkdocs/mkdocs@3c3670d](https://github.com/mkdocs/mkdocs/commit/3c3670d92c972d874d7fe927df5abf728e003a66)
        - [mkdocs/mkdocs@b4c02e5](https://github.com/mkdocs/mkdocs/commit/b4c02e53ac1a7075d07677d80f49d16f37f740a4)
        - [mkdocs/mkdocs@c4db02b](https://github.com/mkdocs/mkdocs/commit/c4db02b5863e2289a0c80a5b500cc7b5e7df95aa)
        - [mkdocs/mkdocs@c070dd0](https://github.com/mkdocs/mkdocs/commit/c070dd020203d87012ef278c31a6076af06b4c93)
        - [mkdocs/mkdocs@94544bd](https://github.com/mkdocs/mkdocs/commit/94544bdc6b564c59d2fa79af1ce100536fbff471)
    - Doesn't include:
        - [mkdocs/mkdocs@a012d2e](https://github.com/mkdocs/mkdocs/commit/a012d2e65d8adb923a3768af6ee1ed87d179879b)
            - Breadcrumbs didn't need this change
        - [mkdocs/mkdocs@cc88b5a](https://github.com/mkdocs/mkdocs/commit/cc88b5a6802e1b1fdaee42aa27f171cb416493dd), [mkdocs/mkdocs@e254d4b](https://github.com/mkdocs/mkdocs/commit/e254d4b1bc9b278416af6acefc1d473af42ebf8b), and [mkdocs/mkdocs@8b0971c](https://github.com/mkdocs/mkdocs/commit/8b0971c4fe0115a13920c40fb4d6180f02ef3067)
            - Jinja2 updates not applicable to Jekyll templating system
        - [mkdocs/mkdocs@ca9c8c](https://github.com/mkdocs/mkdocs/commit/ca9c8c1a603283f663044ea7c99fc0d6f6385e73), and [mkdocs/mkdocs@49d02e4](https://github.com/mkdocs/mkdocs/commit/49d02e48edc51a0ae2bd79e16742ddb6027ef135)
            - This feature has been overwritten by this theme version with deeper GH integration.
        - [mkdocs/mkdocs@32d8c3a](https://github.com/mkdocs/mkdocs/commit/32d8c3a986e146cb0b549e024335c6910c3070dc)
            - Feature skipped for config simplicity.
        - [mkdocs/mkdocs@da35dca](https://github.com/mkdocs/mkdocs/commit/da35dcad0c363e7a34e56f9220d93ca28f75c1fd) and [mkdocs/mkdocs@da35dca](https://github.com/mkdocs/mkdocs/commit/da35dcad0c363e7a34e56f9220d93ca28f75c1fd)
            - Navigation reimplemented for Jekyll Liquid templates, not needed.
    - There was also a large number of commits updating the translations, which are not supported in this Jekyll theme version.

## v1.1.0

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
