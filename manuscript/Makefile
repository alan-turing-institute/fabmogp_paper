RS_IMAGES = PHILOSOPHICAL_TRANSACTIONS_A_CMYK.pdf\
            RS_Pubs_Logo_Line_CMYK.pdf\
			RSTA_OpenAccesslogo_RGB.pdf\
			RS_crossmark_logo.pdf
RESULTS = /home/root/fabmogp/FabSim3/results/
LOCALHOST = demo_localhost_16
NPOINTS = 20
NUM_RANGE := $(shell seq 1 ${NPOINTS})
FDFAULT_OUT = .py _x.dat _y.dat _U.dat
MOGP_OUT := $(addprefix results/${LOCALHOST}/RUNS/sample_point_1/,input_points.npy ed.pickle)
FIG_1_FILES_U := $(addprefix results/data/rough_example_ufault,${FDFAULT_OUT})
FIG_1_FILES_VY := $(subst U,vy,$(subst ufault,vybody,${FIG_1_FILES_U}))
FIG_23_FILES_1 := $(addprefix results/${LOCALHOST}/RUNS/sample_point_1/data/,$(addprefix simulation_1_ufault,${FDFAULT_OUT}))
FIG_23_FILES += $(foreach N,${NUM_RANGE},$(subst point_1,point_${N},${FIG_23_FILES_1}))
SIM_TEXT = lhc_values.tex correlation_lengths.tex covariance_scale.tex
FIGURES = figure1.pdf figure2.pdf figure3.pdf

fabmogp_paper.pdf : fabmogp_paper.tex ${RS_IMAGES} ${SIM_TEXT} ${FIGURES}
	pdflatex $<
	pdflatex $<
	pdflatex $<
	rm -rf $(subst .pdf,.aux,$@) $(subst .pdf,.log,$@) $(subst .pdf,.out,$@)

$(FIG_1_FILES_U) $(FIG_1_FILES_VY) : % : figure1_sim.py
	 python $<

figure1.pdf: figure1.py ${FIG_1_FILES_U} ${FIG_1_FILES_VY}
	python $<

$(FIG_23_FILES) $(MOGP_OUT) : % :
	fabsim localhost mogp_ensemble:demo,sample_points=${NPOINTS},seed=4742322
	fabsim localhost fetch_results
	rsync -pthrvz ${RESULTS}/${LOCALHOST} results/

$(FIGURES) $(SIM_TEXT) : % : figure23.py ${FIG_23_FILES} ${MOGP_OUT}
	python $<

.PHONY: clean
clean:
	rm -f ${PAPER} ${FIGURES} ${SIMTEXT}

.PHONY: cleanall
cleanall:
	rm -f ${FIG_1_FILES_U} ${FIG_1_FILES_VY} ${FIG_23_FILES}