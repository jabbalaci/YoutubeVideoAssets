# How to (un)comment in VS Code like a pro?

**Corresponding video (in Hungarian):**
* https://www.youtube.com/watch?v=x4JS05ohCGk

## Steps to follow

Install the VS Code extension **macros** by geddski (author).

Then, open your **Keyboard Shortcuts** in JSON mode and add these lines:

```json
{
    "key": "ctrl+numpad_divide",
    "command": "macros.commentLine",
    "when": "editorTextFocus && !editorReadonly"
},
```

Finally, open your **Settings** (also in JSON mode), and add these lines:

```json
"macros": {
    "commentLine": [
        "editor.action.commentLine",
        "cursorDown"
    ]
},
```

Done.
