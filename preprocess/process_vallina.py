#-*- coding:utf-8 -*-
# AUTHOR:   fuzx
# FILE:     process_vallina.py
# ROLE:     TODO (some explanation)
# CREATED:  2017-09-23 16:50:16
# MODIFIED: 2017-09-23 16:50:22

## Usage: python read_dir write_dir filename

from util import get_noun
from nltk.tokenize import sent_tokenize
import sys, os


# invalid for vanilla, all_invalid for allpair, lookback2_invalid for lookback2
invalid = [8820, 19084, 44800]
all_invalid = []
for i in range(0, 10):
    for j in invalid:
        all_invalid.append(j * 10 + i)
lookback2_invalid = []
for i in range(0, 5):
    for j in invalid:
        lookback2_invalid.append(j * 5 + i)
        
def main(source_file, q_file, r_file, kw_file):
    with open(source_file)as fin:
        for i, line in enumerate(fin):
            if i in lookback2_invalid: continue
            if i % 1000 == 0: print i
            if line.startswith("<bos>"): continue
            list = sent_tokenize(line)
            q = " ".join(list[:-1])
            r = list[-1]
            kw = get_noun(r)
            q_file.write(q + "\n")
            r_file.write(r + "\n")
            kw_file.write(kw + "\n")
    print "Process %s file done!" % (source_file)
    q_file.close()
    r_file.close()
    kw_file.close()
    
if __name__ == "__main__":
    read_path = sys.argv[1] #"../../Processed/"
    write_path = sys.argv[2] #"../../data/"
    file_name = sys.argv[3]
    train_file = os.path.join(read_path, file_name)
    
    train_q_file = open(os.path.join(write_path, file_name + ".query"), "w")
    train_r_file = open(os.path.join(write_path, file_name + ".reply"), "w")
    train_kw_file = open(os.path.join(write_path, file_name + ".topic"), "w")
    '''dev_q_file = open(write_path + "lookback2.dev.query", "w")
    dev_r_file = open(write_path + "lookback2.dev.reply", "w")
    dev_kw_file = open(write_path + "lookback2.dev.topic", "w")
    '''
    main(train_file, train_q_file, train_r_file, train_kw_file)
    #main(valid_file, dev_q_file, dev_r_file, dev_kw_file)
