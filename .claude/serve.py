#!/usr/bin/env python3
import http.server
import functools

Handler = functools.partial(
    http.server.SimpleHTTPRequestHandler,
    directory="/Users/emilypickett/Documents/GitHub/blakeyourlocalsparkie.github.io"
)
http.server.HTTPServer(("", 3456), Handler).serve_forever()
