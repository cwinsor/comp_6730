# 0) Install Anaconda
# 1) Install PyG using Anaconda
# 2) Install the prerequisite Torch:  https://pytorch.org/get-started/locally/#anaconda



### powershell -ExecutionPolicy Bypass

$Env:ENV_NAME='conda_env_uml_6730_proj'
# need to do this otherwise cannot select the environment...
# https://stackoverflow.com/questions/47246350/conda-activate-not-working
conda init powershell
# create empty environment
conda create --name $Env:ENV_NAME python=3.7 --yes
conda activate $Env:ENV_NAME
conda info --envs

conda install PyTorch --yes
conda install pyg -c pyg -c conda-forge --yes

# update using requirements.txt
# conda env update $ENV_NAME --file requirements.txt --prune
# add george
# conda install -c conda-forge george --yes


