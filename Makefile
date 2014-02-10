# Copyright (C) 2013, 2014  Jim Turner
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.

SHELL = /bin/bash

.PHONY: default clean

default: dynamics.pdf fluid-mechanics.pdf heat-transfer.pdf

dynamics.pdf: dynamics.tex preamble.tex firstpage.tex
	latexmk dynamics.tex

fluid-mechanics.pdf: fluid-mechanics.tex moody-diagram.eps preamble.tex firstpage.tex
	latexmk fluid-mechanics.tex

heat-transfer.pdf: heat-transfer.tex preamble.tex firstpage.tex
	latexmk heat-transfer.tex

moody-diagram.eps: moody_diagram.py
	python3 moody_diagram.py

clean:
	@latexmk -C
	@rm -f *.eps *.pdf *.log *.fls
