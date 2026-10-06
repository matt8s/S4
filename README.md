If you are looking for a more user-friendly interface to S4 (wavelength-dependent calculations, material management etc.), check out my Python3 package [RayFlare](https://rayflare.readthedocs.io).

# Installation instructions (64-bit Ubuntu 16/18/20 or MacOS):

## Python prerequisites

Use a supported Python 3 environment with pip. The build installs its Python build dependencies from `pyproject.toml`.

```bash
python -m pip install --upgrade pip
```

## Key steps:

```
git clone https://github.com/phoebe-p/S4
cd S4
make S4_pyext
```

Running the `make boost` command before `make S4_pyext` should automatically download and compile the relevant Boost libraries in the local S4 directory. 
HOWEVER, this appears to cause problems on macOS, so if you are installing on macOS you should install the boost libraries 
using Homebrew (see below). If you want to use Boost libraries in a different location you will have to edit the Makefile.

**Note for users of new (late 2020 onwards) Apple machines with M1/Apple silicon/ARM chips: you will need to use Makefile.m1
to compile successfully, see notes below on how to do this.**

## Python package build

The Python extension now uses a checked-in setuptools configuration and PEP 517 metadata rather than generating `setup.py` during each build.
The existing distribution name (`S4`) and version (`1.1`) are preserved.
The build uses the active `python3` by default; set `PYTHON=/path/to/python` when another interpreter is required.

Linux CI builds and imports the extension across multiple Python and NumPy versions, including NumPy 1.26 and NumPy 2.x runtime environments.

## Installing relevant libraries etc.:

**On Ubuntu (with a working version of Python3):**

```
sudo apt-get update
sudo apt install make git gcc g++
sudo apt install libopenblas-dev libfftw3-dev libsuitesparse-dev
```

- libopenblas installs OpenBLAS, to satisfy the LAPACK and BLAS requirements
- lib fftw3 install FFTW3, to satisfy the FFTW requirements
- libsuitesparse install libraries to satisdy CHOLMOD & related requirements

If you want, you can also install the boost libraries using `sudo apt install libboost-all-dev` instead of running `make boost`.

**On MacOS using Homebrew:**

```
brew install fftw suite-sparse openblas lapack boost
```

You can get the make and git commands from homebrew, or through Apple Developer Tools. If the packages are installed/symlinked by Homebrew to the default location (/usr/local/include) you should not have to modify the Makefile, and you should be able to use the same Makefile as Ubuntu/Linux (i.e. no need to use Makefile.osx).

*If you have multiple Python versions, you may need to modify the S4_pyext part of the Makefile:*

````
pip3 install --upgrade ./
````

to e.g.:
```
[path of target python or virtual environment] setup.py install
```

You can install S4 into a virtual environment automatically by activating that environment before running `make S4_pyext`.
You can also select the interpreter explicitly, for example `make S4_pyext PYTHON=python3.12`.

See [here](https://rayflare.readthedocs.io/en/latest/Installation/installation.html) for more extensive instructions.


**On MacOS with M1/ARM chips:**

Some of the flags used in the default Makefile cause issues with the new chip architecture. Run the following instead:

```
git clone https://github.com/phoebe-p/S4
cd S4
make S4_pyext --file="Makefile.m1"
```

Installing the libraries with Homebrew should work as expected.

-------------------------------------

S4: Stanford Stratified Structure Solver (http://fan.group.stanford.edu/S4/)

A program for computing electromagnetic fields in periodic, layered
structures, developed by Victor Liu (victorliu@alumni.stanford.edu) of the
Fan group in the Stanford Electrical Engineering Department.

See the S4 manual, in doc/index.html, for a complete
description of the package and its user interface, as well as
installation instructions, the license and copyright, contact
addresses, and other important information.

---------------------------------------

sajidmc: The MakefileHPC is created to compile the S4 in HPC environment without
root access. Also added an example for python extension testing: 

Check Wiki for details: https://github.com/sajidmc/S4/wiki
Example result: https://raw.githubusercontent.com/sajidmc/S4/master/examples/bontempi_et_al_Nanoscale_2017.png

