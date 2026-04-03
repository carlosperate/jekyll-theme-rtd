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

### Note

```markdown
> [!NOTE]
> This is a note admonition.
```

> [!NOTE]
> This is a note admonition.

### Tip

```markdown
> [!TIP]
> This is a tip admonition.
```

> [!TIP]
> This is a tip admonition.

### Important

```markdown
> [!IMPORTANT]
> This is an important admonition.
```

> [!IMPORTANT]
> This is an important admonition.

### Warning

```markdown
> [!WARNING]
> This is a warning admonition.
```

> [!WARNING]
> This is a warning admonition.

### Caution

```markdown
> [!CAUTION]
> This is a caution admonition.
```

> [!CAUTION]
> This is a caution admonition.
