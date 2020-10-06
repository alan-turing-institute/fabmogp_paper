fabmogp_response.pdf : fabmogp_response.tex
	pdflatex $<
	pdflatex $<
	rm -f $(subst .pdf,.aux,$@) $(subst .pdf,.log,$@) $(subst .pdf,.out,$@)

.PHONY: clean
clean:
	rm -f fabmogp_response.pdf

