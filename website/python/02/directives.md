# Directives

Directives are special attributes with the `v-` prefix. Vue provides a number of built-in directives, including `v-html` and `v-bind` which we have introduced above. Directive attribute values are expected to be single JavaScript expressions (with the exception of `v-for`, `v-on` and `v-slot`, which will be discussed in their respective sections later). A directive's job is to reactively apply updates to the DOM when the value of its expression changes.

## Vue.js syntax

```html
<SomeWidget
   v-if="a > 10"
   v-show="isVisible"
   
   v-model="b"
/>
```

## Trame syntax

```python
SomeWidget(
   v_if="a > 10",
   v_show="isVisible",
   
   v_model="b",
)
```

> [!TIP]
> No need to use the tuple expression as it is __always__ a JavaScript expression, unless we want to assign a default value (and reserve that variable name).
