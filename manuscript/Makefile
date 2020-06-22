PAPER = fabmogp_paper.pdf
RS_IMAGES = PHILOSOPHICAL_TRANSACTIONS_A_CMYK.pdf RS_Pubs_Logo_Line_CMYK.pdf RSTA_OpenAccesslogo_RGB.pdf RS_crossmark_logo.pdf

paper: ${PAPER}

%.pdf: %.tex ${RS_IMAGES}
	pdflatex $<
	pdflatex $<
	pdflatex $<
	rm -rf $*.aux $*.log $*.out

.PHONY: clean
clean:
	rm -rf ${PAPER}