################################################
# activate the virtual environment
# if venv does not exist - create it

if (-NOT (Test-Path '.\venv\Scripts\activate' -PathType Leaf)) {
    "did not find venv\Scripts\activate - creating now..."

    # confirm at least we have python with pip
    python -m pip --version

    # create empty venv
    python -m venv venv
    }

# activate the venv
.\venv\Scripts\activate

# ensure pip, setuptools and wheels are up to date
python -m pip install --upgrade pip setuptools wheel

# get the libraries specified in requirements.txt
python -m pip install -r requirements.txt
python -m pip list

################################################
# PYTHONPATH

$Env:PYTHONPATH=''

$Env:PYTHONPATH=$ENV:PYTHONPATH + $PSScriptRoot
$Env:PYTHONPATH=$ENV:PYTHONPATH + ';'

$Env:PYTHONPATH=$ENV:PYTHONPATH + $PSScriptRoot + ';'


################################################
# PATH

$ENV:PATH = "../libraries/gnuplot_5_2_8/gp528-win64-mingw/gnuplot/bin;$ENV:PATH"
$ENV:PATH = "../libraries/Graphviz/bin;$ENV:PATH"

