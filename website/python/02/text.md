# Text interpolation

## Vue.js syntax

Inside HTML text node we use the moustache notation.

```html
<label>Hello {{ name }}</label>
```

When it is passed as an attribute to a widget, the JavaScript templating syntax needs to be used.

```html
<SomeWidget
  v-bind:label="`Hello ${name}`"
/>
```

## Trame syntax

Same as vue.js syntax.

```python
html.Label("Hello {{ name }}")
```

For attribute, since it needs to be evaluated (not a static value), the tuple notation is required (same as `:` or `v-bind:` prefix for Vue.js).

```html
SomeWidget(
    label=("`Hello ${name}`",),
)
```