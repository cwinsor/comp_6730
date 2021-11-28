################################################
# activate the virtual environment
# if the pymote_env does not exist - create it

if (-NOT(Test-Path '.\venv\Scripts\activate' -PathType Leaf)) {

    " "
    "did not find venv - creating it now..."

    # confirm at least we have python with pip
    python --version
    python -m pip --version

    # create an empty virtualenv
    python -m venv venv
    }

# activate the venv
.\venv\Scripts\activate

# ensure pip, setuptools and wheels are up to date
python -m pip install --upgrade pip setuptools wheel

# get the libraries specified in requirements.txt and show a list
python -m pip install --upgrade -r requirements.txt
python -m pip list

################################################
# add to PYTHONPATH for python modules
$Env:PYTHONPATH= '.'
$Env:PYTHONPATH= $Env:PYTHONPATH + ';' + $PSScriptRoot + '\lib;'