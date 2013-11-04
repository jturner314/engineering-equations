default:
	latexmk fluid-mechanics.tex

cont:
	latexmk -pvc -view=pdf fluid-mechanics.tex

clean:
	@latexmk -C
	@rm -f *.out
	@rm -rf auto
