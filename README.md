# FabMOGP Conference Paper

This repository contains files needed to reproduce the earthquake tutorial simulations in the
conference proceedings on the VECMA workshop at the Alan Turing Institute on 24 January 2020.
The paper manuscript and the necessary LaTex files are also included.

## Requirements

This paper uses several software libraries to carry out the described computations:

* `fdfault`, which simulates dynamic earthquake rupture
* `seistools`, a library containing utilities for fault mechanics research
* `mogp_emulator`, an Uncertainty Quantification toolkit
* `fabsim3`, a simulation management tool to support simulation reproducibility
* `fabmogp`, a `fabsim3` plugin for managing the simulations in this paper

All of these tools are freely available under open source software licenses.

All dependencies required to reproduce this paper are included in the provided Dockerfile and the
corresponding Makefile. You will need to install Docker and Make to build the docker image
to run the simulations and create the PDF of the manuscript.