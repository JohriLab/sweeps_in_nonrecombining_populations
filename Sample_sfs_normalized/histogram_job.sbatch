#!/bin/bash

#SBATCH --mail-user=sackau@unc.edu
#SBATCH --mail-type=ALL
#SBATCH -p general
#SBATCH -N 1
#SBATCH -t 02:00:00
#SBATCH --mem=4g
#SBATCH -a 1-1000
#SBATCH -n 1
#SBATCH -o /nas/longleaf/home/sackau/LOGFILES/hist/hist_%A_%a.o
#SBATCH -e /nas/longleaf/home/sackau/LOGFILES/hist/hist_%A_%a.e

# Load modules
module load python/3.6.6

# Set directories
BASE_DIR="/work/users/s/a/sackau/UNC_work/Corresponding_SFS_sample/Sample_txt_files_1000_20"
OUTPUT_DIR="/work/users/s/a/sackau/UNC_work/Corresponding_SFS_sample/Results/results"

# Create output directory if needed
mkdir -p "$OUTPUT_DIR"

# Run processing for this folder (SLURM_ARRAY_TASK_ID = folder number)
python process_histograms.py "$BASE_DIR" "$SLURM_ARRAY_TASK_ID" "$OUTPUT_DIR"

echo "Completed processing folder $SLURM_ARRAY_TASK_ID"