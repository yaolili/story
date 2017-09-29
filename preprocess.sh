#!/bin/bash

# tokenize and generate .query, .reply and .topic files.
python ./preprocess/process_vallina.py $1 $2 $3 || printf 'Usage: ./preprocess.sh input_dir, output_dir file_name'; exit

# generate dictionary
python ./preprocess/build_dictionary.py $3 || exit
