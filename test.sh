#!/bin/bash
#PBS -l nodes=1:ppn=24
#PBS -l walltime=24:00:00
#PBS -N session2_default
#PBS -A course
#PBS -q ShortQ

export THEANO_FLAGS=device=cpu,floatX=float32

python translate.py -n -p 2 \
	../model/vanilla/twogate/model_twogate.npz  \
	../data/rocstory.vanilla.train.pkl \
	../data/rocstory.vanilla.train.pkl \
	../data/yao.dev.query \
    ../data/vanilla.dev.topic \
	./yao.tok



