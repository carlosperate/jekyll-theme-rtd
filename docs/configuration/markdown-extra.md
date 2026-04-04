---
layout: default
title: Additional Markdown Features
nav_order: 1
---

# Additional Markdown Features

## Admonitions

Admonitions are highlighted callouts for important context such as notes,
tips, warnings, and cautions.

Admonitions are enabled by default. To disable them, add the following to your
`_config.yml`:

```yaml
admonitions: false
```

This theme uses GitHub Markdown-style admonitions (blockquotes with a special
first line, eg. `[!NOTE]`,`[!WARNING]`, etc).
Each of the following examples shows the Markdown source first, and the
rendered result below it.

### Admonition Types

```markdown
> [!NOTE]
> This is a note admonition.

> [!TIP]
> This is a tip admonition.

> [!IMPORTANT]
> This is an important admonition.

> [!INFO]
> This is an info/hint admonition.

> [!WARNING]
> This is a warning admonition.

> [!CAUTION]
> This is a caution admonition.

> [!DANGER]
> This is a danger admonition.
```

> [!NOTE]
> This is a note admonition.

> [!TIP]
> This is a tip admonition.

> [!IMPORTANT]
> This is an important admonition.

> [!INFO]
> This is an info/hint admonition.

> [!WARNING]
> This is a warning admonition.

> [!CAUTION]
> This is a caution admonition.

> [!DANGER]
> This is a danger admonition.

## Buttons

Links can be styled as buttons using Kramdown's [attribute list syntax](https://kramdown.gettalong.org/syntax.html#attribute-list-definitions).
Apply the `.btn` class to any Markdown link:

```markdown
[Button](#){: .btn }
```

[Button](#buttons){: .btn }

### Button Variants

Colour Variants:

```markdown
[Default](#){: .btn }
[Neutral](#){: .btn .btn-neutral }
[Info](#){: .btn .btn-info }
[Success](#){: .btn .btn-success }
[Warning](#){: .btn .btn-warning }
[Danger](#){: .btn .btn-danger }
```

[Default](#color-variants){: .btn }
[Neutral](#color-variants){: .btn .btn-neutral }
[Info](#color-variants){: .btn .btn-info }
[Success](#color-variants){: .btn .btn-success }
[Warning](#color-variants){: .btn .btn-warning }
[Danger](#color-variants){: .btn .btn-danger }

For smaller buttons add `.btn-small`:

```markdown
[Small button](#){: .btn .btn-small }
[Small info](#){: .btn .btn-info .btn-small }
```

[Small button](#small-buttons){: .btn .btn-small }
[Small info](#small-buttons){: .btn .btn-info .btn-small }

`.btn-link` renders a button with the appearance of a plain link:

```markdown
[Link button](#){: .btn .btn-link }
```

[Link button](#){: .btn .btn-link }
