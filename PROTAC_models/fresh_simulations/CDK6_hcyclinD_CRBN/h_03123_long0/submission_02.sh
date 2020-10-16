#!/usr/bin/env bash
# Set walltime limit
#BSUB -W 168:00
#
# Set output file
#BSUB -o  production.log
#
# Specify node group
#BSUB -m "ls-gpu lg-gpu lt-gpu lp-gpu ld-gpu lv-gpu"
#BSUB -q gpuqueue
#
# nodes: number of nodes and GPU request (ptile: number of processes per node)
#BSUB -n 1 -R "rusage[mem=8] span[ptile=1]"
#BSUB -gpu "num=1:j_exclusive=yes:mode=shared"
#
# job name (default = name of script file)
#BSUB -J "h_s123CDK6_0"
#

module add cuda/9.0

python 02.unbiased_simulation.py
