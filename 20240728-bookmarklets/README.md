# Some Useful Bookmarklets

**Corresponding Videos (in Hungarian):**
* https://www.youtube.com/watch?v=Mkfl_U-WTHU (Up/Down)

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

## Show Generated HTML Source of the Current Page

```js
function escapeHTML(str) {
    return str.replace(/[&<>'"]/g, function(tag) {
        var tagsToReplace = {
            '&': '&amp;',
            '<': '&lt;',
            '>': '&gt;',
            "'": '&#39;',
            '"': '&quot;'
        };
        return tagsToReplace[tag] || tag;
    });
}
var generatedHTML = document.documentElement.outerHTML;
var escapedHTML = escapeHTML(generatedHTML);
var newWindow = window.open();
newWindow.document.write('<!DOCTYPE html><html><head><title>Generated Source</title><style>body{white-space:pre-wrap;word-wrap:break-word;font-family:monospace;}</style></head><body>' + escapedHTML + '</body></html>');
newWindow.document.close();
```

## More Examples

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

## Links

* https://bookmarklets.org/maker/
* https://caiorss.github.io/bookmarklet-maker/
