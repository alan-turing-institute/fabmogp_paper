PAPER = fabmogp_paper.pdf
RS_IMAGES = PHILOSOPHICAL_TRANSACTIONS_A_CMYK.pdf RS_Pubs_Logo_Line_CMYK.pdf RSTA_OpenAccesslogo_RGB.pdf RS_crossmark_logo.pdf
SIM_TEXT = lhc_values.tex correlation_lengths.tex covariance_scale.tex
FIGURES = figure1.pdf figure2.pdf figure3.pdf

paper: ${PAPER}

figure1.pdf: figure1.py
	python $<

figure2.pdf figure3.pdf ${SIM_TEXT}: figure23.py
	fabsim localhost mogp_ensemble:demo,sample_points=20,seed=84362
	fabsim localhost fetch_results
	rsync -pthrvz demo_localhost_16 results
	python $<

%.pdf: %.tex ${RS_IMAGES} ${SIM_TEXT} ${FIGURES}
	pdflatex $<
	pdflatex $<
	pdflatex $<
	rm -rf $*.aux $*.log $*.out

.PHONY: clean
clean:
	rm -rf ${PAPER}