RS_IMAGES = PHILOSOPHICAL_TRANSACTIONS_A_CMYK.pdf\
            RS_Pubs_Logo_Line_CMYK.pdf\
            RSTA_OpenAccesslogo_RGB.pdf\
            RS_crossmark_logo.pdf
RS_TEX = rsta.bst rstransa.cls
RESULTS = /home/root/fabmogp/FabSim3/results/
LOCALHOST = demo_localhost_16
NPOINTS = 20
NVALID = 10
NUM_RANGE := $(shell seq 1 ${NPOINTS})
VAL_RANGE := $(shell seq 1 ${NVALID})
FDFAULT_OUT = .py _x.dat _y.dat _U.dat
MOGP_OUT := $(addprefix results/training/RUNS/sample_point_1/,input_points.npy ed.pickle)
VALID_OUT := $(subst training,validation, ${MOGP_OUT})
FIG_1_FILES_U := $(addprefix results/data/rough_example_ufault,${FDFAULT_OUT})
FIG_1_FILES_VY := $(subst U,vy,$(subst ufault,vybody,${FIG_1_FILES_U}))
FIG_24_FILES_1 := $(addprefix results/${LOCALHOST}/RUNS/sample_point_1/data/,$(addprefix simulation_1_ufault,${FDFAULT_OUT}))
FIG_24_FILES += $(foreach N,${NUM_RANGE},$(subst point_1,point_${N},${FIG_24_FILES_1}))
FIG_24_VALID := $(subst training,validation, ${FIG_24_FILES})
SIM_TEXT = lhc_values.tex validation_points.tex\
           correlation_lengths.tex covariance_scale.tex
FIG24 = figure2.pdf figure3.pdf figure4.pdf
FIGURES = ${FIG24} figure1.pdf FabMogpMap.pdf

fabmogp_paper.pdf : fabmogp_paper.tex fabmogp_paper.bib ${RS_IMAGES} ${RS_TEX} ${FIGURES} ${SIM_TEXT}
	pdflatex $<
	bibtex $(subst .tex,.aux,$<)
	pdflatex $<
	pdflatex $<
	rm -f $(subst .pdf,.aux,$@) $(subst .pdf,.log,$@) $(subst .pdf,.out,$@)
	rm -f $(subst .pdf,.blg,$@) $(subst .pdf,.bbl,$@)

$(FIG_1_FILES_U) $(FIG_1_FILES_VY) : % : figure1_sim.py
	 python $<

figure1.pdf: figure1.py ${FIG_1_FILES_U} ${FIG_1_FILES_VY}
	python $<

$(FIG_24_FILES) $(FIG_24_VALID) $(MOGP_OUT) $(VALID_OUT): % :
	fabsim localhost mogp_ensemble:demo,sample_points=${NPOINTS},seed=4742322
	fabsim localhost fetch_results
	rsync -pthrvz ${RESULTS}/${LOCALHOST} results/training
	rm -rf ${RESULTS}/${LOCALHOST}
	fabsim localhost mogp_ensemble:demo,sample_points=${NVALID},seed=48273
	fabsim localhost fetch_results
	rsync -pthrvz ${RESULTS}/${LOCALHOST} results/validation
	rm -rf ${RESULTS}/${LOCALHOST}

$(FIG24) $(SIM_TEXT) : % : figure24.py ${FIG_24_FILES} ${FIG_24_VALID} ${MOGP_OUT} ${VALID_OUT}
	python $<

.PHONY: clean
clean:
	rm -f ${PAPER} ${FIGURES} ${SIMTEXT}

.PHONY: cleanall
cleanall:
	rm -f ${FIG_1_FILES_U} ${FIG_1_FILES_VY} ${FIG_24_FILES}
