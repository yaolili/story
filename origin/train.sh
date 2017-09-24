c#!/bin/bash
#PBS -l nodes=1:ppn=20
#PBS -l walltime=168:00:00
#PBS -N session2_default
#PBS -A course
#PBS -q GpuQ


export CUDA_ROOT=~/cuda/cuda-8.0
export CUDA_HOME=~/cuda/cuda-8.0
export PATH=${CUDA_HOME}/bin:$PATH
export LD_LIBRARY_PATH=${CUDA_HOME}/lib64:$LD_LIBRARY_PATH

THEANO_FLAGS='device=gpu3,floatX=float32,lib.cnmem=0.9' python train_nmt.py



