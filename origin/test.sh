#!/bin/bash
#PBS -l nodes=1:ppn=24
#PBS -l walltime=24:00:00
#PBS -N session2_default
#PBS -A course
#PBS -q ShortQ

export THEANO_FLAGS=device=cpu,floatX=float32

python translate.py -n -p 20 \
	../../model/allpair/origin/model_origin.npz  \
	../../data/rocstory.vanilla.train.pkl \
	../../data/rocstory.vanilla.train.pkl \
	../../data/vanilla.dev.query \
	./allpair.origin.tok



