---
# This example file is based on index-test.md from Just the Docs Jekyll Theme.
# Original file copyright (c) 2016 Patrick Marsceill:
# https://github.com/pmarsceill/just-the-docs/blob/v0.2.7-r/docs/index-test.md
# Changes have been made to adapt it for this project.

layout: default
title: Markdown Kitchen Sink Example
excerpt: A sample description for SEO.
nav_order: 2
---

Text can be **bold**, _italic_, ~~strikethrough~~, ***bold and italic***, or ~~**bold strikethrough**~~.

Inline code `looks like this`.

[Link to another page](../quickstart.html).

There should be whitespace between this paragraph and the one below.

There should be whitespace this paragraph and the one above.
But consecutive lines in the Markdown, like these two, are rendered in the same paragraph.

# Markdown Kitchen Sink Example

Hovering over the headers show anchor links on their left.

## Header h2
### Header h3
#### Header h4
##### Header h5
##### Header h6

## Quotes 2 - 1

> This is a blockquote following a header.
>
> When something is important enough, you do it even if the odds are not in your favor.

### Admonitions 3 - 1.1

[Admonitions (more info here)](../configuration/markdown-extra.html#admonitions) are added via Markdown blockquotes and rendered like this:

> [!TIP]
> Hover over any code block from the following section to reveal the copy-to-clipboard button.

> [!WARNING]
> Admonitons and Mermaid diagrams are transformed on page load.

> [!DANGER]
> 
> Not locking a theme version (`remote_theme: carlosperate/jekyll-theme-rtd@v1.4.0`)
> in your `_config.yml` file could result in changes on your built site
> between theme releases.

#### Code Blocks 4 - 1.1.1

Hover on the code blocks to show a "copy code to clipboard" button on the top right corner.

```js
// Javascript code with syntax highlighting.
var fun = function lang(l) {
  dateformat.i18n = require('./lang/' + l)
  return true;
}
```

```ruby
# Ruby code with syntax highlighting
GitHubPages::Dependencies.gems.each do |gem, version|
  s.add_dependency(gem, "= #{version}")
end
```

```python
# Python code with syntax highlighting
from microbit import *

while True:
    reading = accelerometer.get_x()
    if reading > 20:
        display.show("R")
    elif reading < -20:
        display.show("L")
    else:
        display.show("-")
```

##### Buttons 5 - 1.1.1.1

[Buttons (more info here)](../configuration/markdown-extra.html#buttons) are inlined and have multiple options:

[Default](#kitchen-header-5---1111){: .btn }
[Neutral](#kitchen-header-5---1111){: .btn .btn-neutral }
[Info](#kitchen-header-5---1111){: .btn .btn-info }
[Success](#kitchen-header-5---1111){: .btn .btn-success }
[Warning](#kitchen-header-5---1111){: .btn .btn-warning }
[Danger](#kitchen-header-5---1111){: .btn .btn-danger }
[Small button](#kitchen-header-5---1111){: .btn .btn-small }
[Link button](#kitchen-header-5---1111){: .btn .btn-link }

###### Tables 6 - 1.1.1.1.1

| head1        | head two          | three |
|:-------------|:------------------|:------|
| ok           | good swedish fish | nice  |
| out of stock | good and plenty   | nice  |
| ok           | good `oreos`      | hmm   |
| ok           | good `zoute` drop | yumm  |

### Labels 7 - 1.2 *New*{: .label .label-green }

[Labels (more info here)](../configuration/markdown-extra.html#labels) are
badges for status, releases, or other metadata: *Default colour*{: .label }

Blue
{: .label .label-blue }

Green
{: .label .label-green }

Fuchsia
{: .label .label-fuchsia }

Yellow
{: .label .label-yellow }

Red
{: .label .label-red }

Gray
{: .label .label-gray }

<br>

### Lists 8 - 1.3

Here is an unordered list:

*   Item foo
*   Item bar
*   Item baz
*   Item zip

And an ordered list:

1.  Item one
1.  Item two
1.  Item three
1.  Item four

#### Nested Lists 9 - 1.3.1

And a nested list:

- level 1 item
  - level 2 item
  - level 2 item
    - level 3 item
    - level 3 item
- level 1 item
  - level 2 item
  - level 2 item
  - level 2 item
- level 1 item
  - level 2 item
  - level 2 item
- level 1 item

Nesting an ol in ul in an ol:

- level 1 item (ul)
  1. level 2 item (ol)
  1. level 2 item (ol)
    - level 3 item (ul)
    - level 3 item (ul)
- level 1 item (ul)
  1. level 2 item (ol)
  1. level 2 item (ol)
    - level 3 item (ul)
    - level 3 item (ul)
  1. level 4 item (ol)
  1. level 4 item (ol)
    - level 3 item (ul)
    - level 3 item (ul)
- level 1 item (ul)

#### Task List 10 - 1.3.2

And a task list

- [ ] Hello, this is a TODO item
- [ ] Hello, this is another TODO item
- [x] Goodbye, this item is done

### Images 11 - 1.4

Small image

![](https://carlosperate.github.io/jekyll-theme-rtd/assets/img/jekyll-rtd-logo-250px.jpg)

### Large Image 12 - 1.5

![](https://carlosperate.github.io/jekyll-theme-rtd/assets/img/jekyll-rtd-social-media.jpg)

## Definition Lists 13 - 2

Definition lists can be used with HTML syntax.

<dl>
<dt>Name</dt>
<dd>Godzilla</dd>
<dt>Born</dt>
<dd>1952</dd>
<dt>Birthplace</dt>
<dd>Japan</dd>
<dt>Color</dt>
<dd>Green</dd>
</dl>

### Collapsibles 14 - 2.1

This is a `<details>/<summary>` collapsible :

<details>
<summary>Click to expand/collapse</summary>
This content is hidden by default and can be revealed by clicking the summary above. You can put any content here, including text, images, code blocks, etc.
</details>

### Horizonal Rule 15 - 2.2

There's a horizontal rule below this.

* * *

#### Mermaid Diagrams 16 - 2.2.1

[Mermaid diagrams (more info here)](../configuration/mermaid-diagrams.html) are rendered from code blocks with language `mermaid`:

```mermaid
sequenceDiagram
Alice->>John: Hello John, how are you?
loop HealthCheck
    John->>John: Fight against hypochondria
end
Note right of John: Rational thoughts!
John-->>Alice: Great!
John->>Bob: How about you?
Bob-->>John: Jolly good!
```
