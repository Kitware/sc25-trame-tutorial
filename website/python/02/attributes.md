# Attribue binding


> [!WARNING]
> Mustaches cannot be used inside HTML attributes.

## Vue.js syntax

```html
<SomeWidget
   label="Sample code"
   min="0"

   v-bind:value="a"
   :style="`color: ${ a > 10 ? 'red' : 'green'};`"
   v-bind="{ a:1, b:2, c:3 }"
/>
```

## Trame syntax

```python
SomeWidget(
    label="Sample code",
    min=0,
 
    value=("a",),
    style=(""...same as JS...",),
    v_bind=("manyProps", dict(...)),
)
```

> [!TIP]
> The tuple expression is to indicate we have a JavaScript expression. Moreover, the second argument of the tuple can be used to assign a default value and reserve that variable name.

> [!TIP]
> Missing attribute mapping can be added using the `__properties` keyword argument.
> ```
> __properties=[
>    ("py_name", "vue-name:weird"),
>    ("py_name2", "vue-name:weird2"),
> ]
> ```

