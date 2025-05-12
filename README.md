# Here are all the scripts and code used to perform analyses in the manuscript entitled "Genetic diversity during selective sweeps in non-recombining populations" by Sachin Kaushik, Kavita Jain, and Parul Johri.
#The manuscript can be accessed here - https://www.biorxiv.org/content/10.1101/2024.09.12.612756v1.abstract

#Below is the description of all files/folders present here:

>> CI.slim file is the simulation script to obtain an SFS post-fixation of a beneficial mutation when there is clonal interference. 

>> Diffusion_theory_sfs.nb is the mathematica file where the diffusion equations framework is provided to obtain the SFS. Further details are present in each folder in the respective mathematica file.

>> Ns_100_post_fixation_recombination.slim is the SLiM script to simulate a selective sweep conditional on fixation in a recombining population.

>> post_fix.slim is the SLiM script to simulate a selective sweep conditional on fixation in a nonrecombining population. More specific details are within the each folder where simulations are done for each figure.

>> post_fix_python.py is a python script that was used to obtain the SFS from SLiM's output, where particularly all 10^6 simulation replicates (txt files) are processed.

>> python_CI.py script generate the SFS for clonal interference case.

For each file
The running script process is same

Step 1: 
Run the bash file for slim gui
It will run replicates of slim code, and store the information in a file, there will be 1000 folder with 1000 replicates each, meaning we have 10^6 replicates

Step 2:
Run the bash file written for python code to generate the SFS

Step 3:
Average the SFS generated in the previous step by the python script
