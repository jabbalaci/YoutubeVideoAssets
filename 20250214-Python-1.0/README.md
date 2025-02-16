# Compile and try Python 1.0

Original blog post (not from me): https://www.bitecode.dev/p/lets-compile-python-10

## Video

Related video: https://www.youtube.com/watch?v=R93ZIAzyLNM (in Hungarian)

## Summary

Here I sum up the steps in case the blog post above once disappeared.

`$` is the prompt of your host machine.
`#` is the prompt of your container.

```console
$ podman pull docker.io/feverch/debian-legacy:4
$ podman run -it docker.io/feverch/debian-legacy:4  /bin/bash

// inside the container:
# apt-get update && apt-get install -y wget build-essential gcc make libreadline-dev zlib1g-dev

// without closing the container,
// switch to the host machine and download Python 1.0.1:
$ wget https://legacy.python.org/download/releases/src/python1.0.1.tar.gz
// copy it in the container:
$ POD_ID=$(podman ps | grep debian | cut -d" " -f1)
$ podman cp python1.0.1.tar.gz "${POD_ID}:/tmp"

// switch back to the container:
# cd /tmp
# tar xvzf python1.0.1.tar.gz
# cd python-1.0.1/
# ./configure
# make
# make libinstall
# ./python
```

If the download link of `python1.0.1.tar.gz` didn't work,
I have a copy of that file in this folder.

## Links

* Python 1.0.0 is out! by Guido van Rossum: https://groups.google.com/g/comp.lang.misc/c/_QUzdEGFwCo/m/KIFdu0-Dv7sJ?pli=1
* Source code of Python 1.0.1: https://legacy.python.org/download/releases/src/ (I have a local copy here)
* Let's compile Python 1.0: https://www.bitecode.dev/p/lets-compile-python-10
