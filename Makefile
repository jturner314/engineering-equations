SHELL = /bin/bash

.PHONY: default

default: fluid-mechanics.pdf heat-transfer.pdf

fluid-mechanics.pdf: fluid-mechanics.tex moody-diagram.eps preamble.tex firstpage.tex
	latexmk fluid-mechanics.tex

heat-transfer.pdf: heat-transfer.tex preamble.tex firstpage.tex
	latexmk heat-transfer.tex

moody-diagram.eps: moody_diagram.py
	python3 moody_diagram.py

clean:
	@latexmk -C
	@rm -f *.eps *.pdf *.log *.fls
