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

## További példák

```js
// old reddit
window.location = window.location.toString().replace(/(www|new)\.reddit\.com/,"old.reddit.com");

// new reddit
window.location = window.location.toString().replace(/old\.reddit\.com/,"www.reddit.com");

// strip URL
window.location = /https?:\/\/([^/]*)/.exec(window.location.toString())[0];

// hu-hu
window.location = window.location.toString().replace(/www\.xbox\.com\/..-..\//,"www.xbox.com/hu-hu/");
```

## Linkek

* https://bookmarklets.org/maker/
* https://caiorss.github.io/bookmarklet-maker/
