
Here is the process to set up environment using Conda/Anaconda/Miniconda

---- EVERY TIME ----------------

conda activate uml_6730_pytorch_pyg
conda info --envs
cd D:\Users\CHRIS\Documents\code_uml_6730_gnn_and_PyG\comp_6730\04_project\project_final
code -n .  
in vs-code (shell command prompt) run conda activate uml_6730_pytorch_pyg
in vs-code view command pallet and "select python interpreter" pointing to the conda python


---- FIRST TIME -----------------

# 0) Install Anaconda (the big GUI, not miniconda and not the command-line)
Start the Anaconda GUI
Using the GUI create an environment (call it "uml_6730_pytorch_pyg")
Push the button to run "cmd" in that environment.

Within CMD window:
conda install -c pytorch pytorch torchvision     # note torchvision may not be necessary for this project...
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

