.. Copyright (C) 2013, 2014  Jim Turner

   This work is licensed under the Creative Commons Attribution-ShareAlike 3.0 Unported License. To
   view a copy of this license, visit http://creativecommons.org/licenses/by-sa/3.0/deed.en_US.

#####################
Engineering Equations
#####################

This repository contains equations sheets that I am writing for my engineering courses. I will
update this repository periodically.

Sheets
======

So far, I have created equations sheets for the following subjects:

* Dynamics
* Fluid Mechanics
* Heat Transfer

I am currently working on equation sheets for the following subjects:

* Engineering Design Optimization

To download already-built equation sheets, go to the `releases
<https://github.com/jturner314/engineering-equations/releases>`_ page.

Building
========

The build process depends on GNU Make, ``latexmk``, and Python 3 (with the ``numpy``, ``scipy``, and
``matplotlib`` packages). To build all sheets, run::

    $ make

or, to build an individual sheet, specify its name::

    $ make fluid-mechanics.pdf

Contributing
============

If you'd like to contribute, please create an issue or send a pull request via the GitHub project
located at https://github.com/jturner314/engineering-equations.

License
=======

Some portions of this project are licensed under the Creative Commons Attribution-ShareAlike 4.0
International License (CC-BY-SA), while others are licensed under the GNU General Public License
(GPL) version 3 or later. See the header of each file for its specific license. While these licenses
are, in general, currently not compatible in a single functional program, the portions of this
project that are licensed under different terms are independent of one another. My intent is that
the GPL will cover only the portions that are computer programs, such as the ``Makefile`` and
``moody_diagram.py`` script. These are only used for (1) building the equation sheets or (2)
generating content. Since output of GPL-licensed programs generally does not fall under the GPL, I
can put the generated content under a different license. In this case, I have put it under the
CC-BY-SA license along with the LaTeX sources. The resulting equation sheet PDFs also fall under
CC-BY-SA. I am not a lawyer, so please let me know if you see any issues with this licensing scheme.
