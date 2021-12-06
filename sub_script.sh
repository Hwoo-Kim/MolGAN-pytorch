#!/bin/bash

#PBS -N HWKim_MolGAN_ZINC_train
#PBS -o /home/wykgroup/hwkim/MolGAN/out.out
#PBS -l nodes=horus12:ppn=28
#PBS -l walltime=7:00:00:00
#PBS -e /home/wykgroup/hwkim/MolGAN/error.error


##### Run ##### 
#NODE=$(uniq < $PBS_NODEFILE)

date

source ~/hwkim/.bashrc

cd /home/wykgroup/hwkim/MolGAN/

python main.py

date
