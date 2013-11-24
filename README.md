# Engineering Equations

This repository contains equations sheets that I am writing for my engineering courses. I will
update this repository periodically.

## Sheets

So far, I have created equations sheets for the following subjects:
- Fluid Mechanics
- Heat Transfer

## Building

The build process depends on GNU Make, `latexmk`, and Python 3 (with the `numpy`, `scipy`, and
`matplotlib` packages). To build all sheets, run:

    $ make

or, to build an individual sheet, specify its name:

    $ make fluid-mechanics.pdf

## Contributing

If you'd like to contribute, please create an issue or send a pull request via GitHub.
