# Engineering Equations

This repository contains equations sheets that I am writing for my engineering courses. I will
update this repository periodically.

## Sheets

So far, I have created equations sheets for the following subjects:
- Fluid Mechanics

## Building

The easiest way to build the equations sheets is to use `latexmk`. To build all of them, simply run:

    $ latexmk

or specify an individual sheet by its name, e.g.:

    $ latexmk fluid-mechanics

`latexmk` can also rebuild a sheet continuously as its source files are updated. To do this, add the
`-pvc` option, e.g.:

    $ latexmk -pvc fluid-mechanics

## Contributing

If you'd like to contribute, please create an issue or send a pull request via GitHub.
