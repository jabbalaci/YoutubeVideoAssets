# Up/Down bookmarklet készítése

**Kapcsolódó videó:** https://www.youtube.com/watch?v=Mkfl_U-WTHU

## Up

```js
window.location.href = document.URL.replace(/(\d+)(?!.*\d)/g, function(match) {
    return String(Number(match) + 1);
});
```

## Down

```js
window.location.href = document.URL.replace(/(\d+)(?!.*\d)/g, function(match) {
    return String(Number(match) - 1);
});
```

## Linkek

* https://bookmarklets.org/maker/
* https://caiorss.github.io/bookmarklet-maker/
