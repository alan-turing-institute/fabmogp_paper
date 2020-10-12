PAPER = fabmogp_paper.pdf
RS_IMAGES = PHILOSOPHICAL_TRANSACTIONS_A_CMYK.pdf\
            RS_Pubs_Logo_Line_CMYK.pdf\
            RSTA_OpenAccesslogo_RGB.pdf\
            RS_crossmark_logo.pdf
RS_TEX = rsta.bst rstransa.cls
LOCALHOST = demo_localhost_16
RESULTS = /home/root/fabmogp/FabSim3/results/${LOCALHOST}
SIMDIR = /home/root/FabSim3/results/${LOCALHOST}
TRAIN_DIR = results/training/${LOCALHOST}
SAMPLE_PATH = RUNS/sample_point_1
NPOINTS = 20
NVALID = 10
NUM_RANGE := $(shell seq 1 ${NPOINTS})
VAL_RANGE := $(shell seq 1 ${NVALID})
FDFAULT_OUT = .py _x.dat _y.dat _U.dat
MOGP_OUT := $(addprefix ${TRAIN_DIR}/${SAMPLE_PATH}/,input_points.npy ed.pickle)
VALID_OUT := $(subst training,validation, ${MOGP_OUT})
FIG_1_FILES_U := $(addprefix results/data/rough_example_ufault,${FDFAULT_OUT})
FIG_1_FILES_VY := $(subst U,vy,$(subst ufault,vybody,${FIG_1_FILES_U}))
FIG_24_FILES_1 := $(addprefix ${TRAIN_DIR}/${SAMPLE_PATH}/data/,$(addprefix simulation_1_ufault,${FDFAULT_OUT}))
FIG_24_FILES += $(foreach N,${NUM_RANGE},$(subst point_1,point_${N},${FIG_24_FILES_1}))
FIG_24_VALID_1 := $(subst training,validation, ${FIG_24_FILES_1})
FIG_24_VALID += $(foreach N,${VAL_RANGE},$(subst point_1,point_${N},${FIG_24_VALID_1}))
FIG_2_FILES = results/input_points.npy results/validation_points.npy \
              results/query_mean.npy results/valid_error.npy
FIG_3_FILES = results/NROY.npy
FIG_4_FILES = results/implausibility.npy
FIG_ALL_FILES = results/query_points.npy
SIM_TEXT = lhc_values.tex validation_points.tex\
           correlation_lengths.tex covariance_scale.tex
FIGURES = $(foreach N,$(shell seq 1 4),figure${N}.pdf)
TUBE_FIG = vecmatk-tubemap-mogp.pdf
CATALOGUE_INPUTS = --code . --input_data input_data
CATALOGUE_OUTPUTS = --output_data results
CATALOGUE_JSON = catalogue_results/20201009-151130.json

$(PAPER) : fabmogp_paper.tex fabmogp_paper.bib ${RS_IMAGES} ${RS_TEX} ${TUBE_FIG} ${FIGURES} ${SIM_TEXT}
	pdflatex $<
	bibtex $(subst .tex,.aux,$<)
	pdflatex $<
	pdflatex $<
	rm -f $(subst .pdf,.aux,$@) $(subst .pdf,.log,$@) $(subst .pdf,.out,$@)
	rm -f $(subst .pdf,.blg,$@) $(subst .pdf,.bbl,$@)

$(FIG_1_FILES_U) $(FIG_1_FILES_VY) : % : run_earthquake.py
	 python $<

figure1.pdf: figure1.py ${FIG_1_FILES_U} ${FIG_1_FILES_VY}
	python $<

figure2.pdf: figure2.py ${FIG_2_FILES} ${FIG_ALL_FILES}
	python $<

figure3.pdf: figure3.py ${FIG_3_FILES} ${FIG_ALL_FILES}
	python $<

figure4.pdf: figure4.py ${FIG_4_FILES} ${FIG_ALL_FILES}
	python $<

$(FIG_24_FILES) $(MOGP_OUT) : % :
	rm -rf ${RESULTS}
	rm -rf ${SIMDIR}
	fabsim localhost mogp_ensemble:demo,sample_points=${NPOINTS},seed=4742322
	fabsim localhost fetch_results
	rsync -pthrvz ${RESULTS} results/training
	rm -rf ${RESULTS}
	rm -rf ${SIMDIR}

$(FIG_24_VALID) $(VALID_OUT): % :
	rm -rf ${RESULTS}
	rm -rf ${SIMDIR}
	fabsim localhost mogp_ensemble:demo,sample_points=${NVALID},seed=63684
	fabsim localhost fetch_results
	rsync -pthrvz ${RESULTS} results/validation
	rm -rf ${RESULTS}
	rm -rf ${SIMDIR}

${FIG_2_FILES} ${FIG_3_FILES} ${FIG_4_FILES} ${FIG_ALL_FILES} ${SIM_TEXT} : % : uq_analysis.py $(FIG_24_FILES) $(MOGP_OUT) $(FIG_24_VALID) $(VALID_OUT)
	python $<

.PHONY: engage
engage:
	catalogue engage ${CATALOGUE_INPUTS}

.PHONY: disengage
disengage:
	catalogue disengage ${CATALOGUE_INPUTS} ${CATALOGUE_OUTPUTS}

.PHONY: compare
compare:
	catalogue compare ${CATALOGUE_JSON} ${CATALOGUE_INPUTS} ${CATALOGUE_OUTPUTS}

.PHONY: clean
clean:
	rm -f ${PAPER} ${FIGURES} ${SIMTEXT}

.PHONY: cleanall
cleanall: clean
	rm -f ${FIG_1_FILES_U} ${FIG_1_FILES_VY} ${FIG_24_FILES} ${FIG_24_VALID}
	rm -f ${MOGP_OUT} ${VALID_OUT} ${FIG_2_FILES} ${FIG_3_FILES}
	rm -f ${FIG_4_FILES} ${FIG_ALL_FILES} results/hyperparameters.npy
