# Raw HTML

## Vue.js syntax

You can use the special attribute `v-html` to use the content of the `rawHTML` variable and set it as content to the `<span>` element defined below.

```html
<span v-html="rawHTML"></span>
```

## Trame syntax

Same as vue.js syntax.

```python
html.Span(
    v_html="rawHTML",
)

state.rawHTML = """
   <label>Hello SC25</label>
   <p>
       We are <b>happy</b> to have you here today in this tutorial.
   </p>
"""
```
