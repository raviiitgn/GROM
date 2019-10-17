#!/bin/bash
#SBATCH -J Askenazi
#SBATCH --partition=p_ccib_1
#SBATCH -N1
#SBATCH -n1
#SBATCH --mem=120000
#SBATCH --cpus-per-task=2
#SBATCH --exclusive
#SBATCH --time=10:00:00

##module load gnu/4.7.3
##module load atlas/3.10.1_w_fPIC


module load gcc/4.9.3
module load python/2.7.12
module load intel/17.0.4
python /projects/f_grigorie_1/rk824/Decision_model_previous.py
