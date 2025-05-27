#!/bin/bash

#SBATCH --mail-user=sackau@unc.edu
#SBATCH --mail-type=ALL
#SBATCH -p general
#SBATCH -N 1
#SBATCH -t 01:00:00
#SBATCH --mem=8g
#SBATCH -o /nas/longleaf/home/sackau/LOGFILES/combine_%j.o
#SBATCH -e /nas/longleaf/home/sackau/LOGFILES/combine_%j.e

module load python/3.6.6

OUTPUT_DIR="/work/users/s/a/sackau/UNC_work/Corresponding_SFS_sample/Results/results"

python /work/users/s/a/sackau/UNC_work/Corresponding_SFS_sample/combine_results.py --output_dir "$OUTPUT_DIR" --max_key 20

# Optional: Clean up individual result files
# rm "$OUTPUT_DIR"/results_*.npz