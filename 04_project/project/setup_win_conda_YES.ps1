
STOP

The process is very hands-on and manual...

---- EVERY TIME ----------------

conda info --envs
conda activate uml_6730_pytorch_pyg
cd D:\Users\CHRIS\Documents\code_uml_6730_gnn_and_PyG\comp_6730\04_project\project>
code -n .


---- FIRST TIME -----------------

# 0) Install Anaconda (the big GUI, not miniconda and not the command-line)
Start the Anaconda GUI
Using the GUI create an environment (call it "uml_6730_pytorch_pyg")
Push the button to run "cmd" in that environment.

Within CMD window:
conda install -c pytorch pytorch torchvision     # note torchvision not necessary...
conda install pyg -c pyg -c conda-forge

Once the conda env has been established, 
review c:\Users\CHRIS\WindowsPowerShell/profile.ps1  to review ...
open powershell and type "conda init"
review c:\Users\CHRIS\Documents\WindowsPowerShell\profile.ps1  to review ...
the above "conda init" will include a line to initialize conda to 'base'

conda info --envs
conda activate uml_6730_pytorch_pyg

cd D:\Users\CHRIS\Documents\code_uml_6730_gnn_and_PyG\comp_6730\04_project\project>
code -n .



+==================== other crud unsuccessful and not necessary ==============================

### powershell -ExecutionPolicy Bypass

$Env:ENV_NAME='conda_env_uml_6730_proj_k'
# need to do this otherwise cannot select the environment...
# https://stackoverflow.com/questions/47246350/conda-activate-not-working
conda init powershell
# create empty environment
conda create --name $Env:ENV_NAME python=3.7 --yes
conda activate $Env:ENV_NAME
conda info --envs

conda install PyTorch=1.8.0 --yes
conda install pyg -c pyg -c conda-forge --yes

# update using requirements.txt
# conda env update $ENV_NAME --file requirements.txt --prune
# add george
# conda install -c conda-forge george --yes


