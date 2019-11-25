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

Text can be **bold**, _italic_, or ~~strikethrough~~.

[Link to another page](another-page).

There should be whitespace between paragraphs.

There should be whitespace between paragraphs. We recommend including a README, or a file with information about your project.

# Markdown Kitchen Sink Example

This is a normal paragraph following a header. GitHub is a code hosting platform for version control and collaboration. It lets you and others work together on projects from anywhere.

## Kitchen Header 2 - 1

> This is a blockquote following a header.
>
> When something is important enough, you do it even if the odds are not in your favor.

### Kitchen Header 3 - 1.1

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

#### Kitchen Header 4 - 1.1.1

*   This is an unordered list following a header.
*   This is an unordered list following a header.
*   This is an unordered list following a header.

##### Kitchen Header 5 - 1.1.1.1

1.  This is an ordered list following a header.
2.  This is an ordered list following a header.
3.  This is an ordered list following a header.

###### Kitchen Header 6 - 1.1.1.1.1

| head1        | head two          | three |
|:-------------|:------------------|:------|
| ok           | good swedish fish | nice  |
| out of stock | good and plenty   | nice  |
| ok           | good `oreos`      | hmm   |
| ok           | good `zoute` drop | yumm  |

### Kitchen Header 7 = 1.2

There's a horizontal rule below this.

* * *

### Kitchen Header 8 - 1.3

Here is an unordered list:

*   Item foo
*   Item bar
*   Item baz
*   Item zip

### Kitchen Header 9 - 1.3

And an ordered list:

1.  Item one
1.  Item two
1.  Item three
1.  Item four

### Kitchen Header 10 - 1.4

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

### Kitchen Header 11 - 1.5

Nesting an ol in ul in an ol

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

### Kitchen Header 12 - 1.6

And a task list

- [ ] Hello, this is a TODO item
- [ ] Hello, this is another TODO item
- [x] Goodbye, this item is done

## Kitchen Header 13 - 2

Small image

![](https://github.blog/wp-content/uploads/2019/01/Company@2x-2.png)

### Kitchen Header 14 - 2.1

Large image

![](https://guides.github.com/activities/hello-world/branching.png)

### Kitchen Header 15 - 2.2

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

#### Kitchen Header 16 - 2.2.1

```
Long, single-line code blocks should not wrap. They should horizontally scroll if they are too long. This line should be long enough to demonstrate this.
```

```
The final element.
```
