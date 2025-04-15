# Event handling

Trame do not show any difference between an attribute or an event.

In vue.js, we have [modifiers](https://vuejs.org/guide/essentials/event-handling#event-modifiers) to handle DOM event details (`stop`, `prevent`, `self`, `capture`, `once`, `passive`).


## Vue.js syntax

```html
<button v-on:click="doSomething">Click Me</button>
<button @click="doSomething">Click Me</button>

<!-- with modifier -->
<button @click.stop.once="doSomething">Click Me</button>
```

## Trame syntax

```python
html.Button(
   "Click Me",
   click="doSomething",
)

# Modifiers tends to be missing in trame
html.Button(
   "Click Me",
   click_stop_once="doSomething",

   __events=[
    ("click_stop_once", "click.stop.once"),
   ],
)
```


> [!TIP]
> Missing event mapping can be added using the `__events` keyword argument.
> ```
> __events=[
>    ("py_name", "vue-name.modifier"),
>    ("my_click", "click.stop.once"),
> ]
> ```
