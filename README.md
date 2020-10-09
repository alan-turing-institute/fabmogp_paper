# FabMOGP Conference Paper

This repository contains files needed to reproduce the earthquake tutorial simulations in the
conference proceedings on the VECMA workshop at the Alan Turing Institute on 24 January 2020.
The paper manuscript and the necessary LaTex files are also included.

## Requirements

This paper uses several software libraries to carry out the described computations:

* `fdfault`, which simulates dynamic earthquake rupture
* `mogp_emulator`, an Uncertainty Quantification toolkit
* `fabsim3`, a simulation management tool to support simulation reproducibility
* `fabmogp`, a `fabsim3` plugin for managing the simulations in this paper

All of these tools are freely available under open source software licenses.

All dependencies required to reproduce this paper are included in the provided Dockerfile and the
corresponding Makefile includes all build instructions.
You will need to install Docker and Make to build the docker image
to run the simulations and create the PDF of the manuscript.
The results of the computations that were submitted for publication have
also been hashed, and a tool is pre-installed in the docker image that
allows the user to easily compare the results of re-running the computations
with those that were previously obtained.

NOTE: I have only tested this on MacOS, though I believe it should also work on Linux with no changes.
If you are running Windows, you may need to alter some of the pre-packaged commands in the
Makefile to work on your system.

## Building the Docker Image

From the `docker` directory, you should be able to build the docker container with the command

```bash
make fabmogp_build
```

You will need to have Make and Docker installed, and Docker must be running. This will build
the image of the computational environment needed to produce the simulations (you will need an
internet connection to download all of the packages).

## Running the Simulations and Typesetting the Manuscript

Once the build completes, you can
start the container by running the command

```bash
make fabmogp_docker
```

This will create a directory `output` in the current directory, and mount that directory
in the docker image to retrieve any outputs. Once the container is running, it will give you
a bash shell. Once in the container, you will see the command prompt below

```bash
[fabmogp] /home/root/fabmogp/fabmopg_paper/manuscript $
```

To run all simulations, create all figures and outputs, and typeset the manuscript,
simply enter `make` at this prompt.
On a 4 core Mac Book, this may take up to 20 minutes. All outputs (figures and the manuscript)
will be created in this directory.

To remove any outputs from the container, you can copy to the shared mounted directory (which has been
defined as an environment variable in the container for convenience). For instance,
to save the paper to your hard drive, type

```bash
cp fabmogp_paper.pdf $OUTPUT
```

This will cause the paper to show up in the `docker/output` directory on your machine.

## Comparing with the Hashed Results

Once all the simulations have been run, you can easily compare your results with
those obtained when the paper was submitted. This uses the `repro-catalogue`
tool, which hashes all of the outputs from the simulations so that they can
be compared later. To do this, from the
same prompt in the container, type `make compare`. The hashing tool will
print out the files that match and those that do not match -- note that
there will be some instances where the files do not match,
which is mainly because the FabSim3
tool saves log files and YAML files containing environment variables
from the simulation runs, both of which include timestamps and thus will
not match across repeated simulations. As long as none of the
files ending in `.dat`, `.npy`, `.load`, or `.surf` show up in the section
where the files did not agree, then the computational results are identical
and have been successfully reproduced.
