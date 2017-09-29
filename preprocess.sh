#!/bin/bash

# tokenize and generate .query, .reply and .topic files.
printf 'tokenize and generate .query, .reply and .topic files.\n'
python ./preprocess/process_vallina.py $1 $2 $3 || (printf 'Usage: ./preprocess.sh input_dir, output_dir file_name'; exit)

# generate dictionary
printf 'Generating dictionary!\n'
python ./preprocess/build_dictionary.py $1/$3 || exit

mv $1/${3}.pkl ${2}/${3}
