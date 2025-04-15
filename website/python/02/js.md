# JavaScript expressions

While JavaScript is very similar to Python, they are still different.
This page aims to provide some usage examples of what you could be using in your trame/vue template.

## String templating

::: code-group

```html [Text node]
<b>static {{ dynamic }}</b>

<b>
  static 
  {{ message.split(' ').reverse().join(' ') }}
</b>
```

```html [Attributes]
<widget  :label="`static ${dynamic}`" />
```

## Ternary evaluation

::: code-group

```html [Text node]
<b>static {{ ok ? 'yes' : 'no' }}</b>
```

```html [Attributes]
<widget  :label="`static ${ok ? 'yes' : 'no'}`" />
```

## Conditions

::: code-group

```js [Boolean]
a && b || c
```
```js [Equality]
// a=2, b='2' => true
a == b

// a=2, b='2' => false
a === b

// c='4' => true
c > 3
```
```js [Object lookup]
// obj={a:{b:[1,2,3]}}
obj?.a?.b?.[6]
```
```js [Arrays]
['a', 'b'].includes(search)
```
