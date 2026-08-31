# vetr0s.css

This is the stylesheet I use on [vetr0s.dev](https://vetr0s.dev/). I pulled it
into its own repository so the typography, colors, and page elements can be
viewed together.

The [live specimen](https://css.vetr0s.dev/) shows the stylesheet in use. The
CSS has no build step or preprocessor.

## Use it

Keep the directory layout and load the two stylesheets:

```html
<link rel="stylesheet" href="/css/reset.css">
<link rel="stylesheet" href="/css/style.css">
```

The stylesheet uses the three ET Book files under `font/`. Copy that directory
with the CSS or update the `@font-face` paths.

`js/theme.js` adds the light and dark theme toggle used by the specimen. The
stylesheet works without the script and follows the operating system theme.

## Check it

```sh
make check
make serve
```

`make serve` starts a local server on port 1314. Set `PORT` to use another port.

## License

The stylesheet is released into the public domain under the Unlicense. The ET
Book font files carry their own license in `font/LICENSE-et-book.txt`.
