# JavaScript expressions

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
