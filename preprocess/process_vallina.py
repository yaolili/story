#-*- coding:utf-8 -*-
# AUTHOR:   fuzx
# FILE:     process_vallina.py
# ROLE:     TODO (some explanation)
# CREATED:  2017-09-23 16:50:16
# MODIFIED: 2017-09-23 16:50:22

## Usage: python read_dir write_dir filename

from util import get_noun, tokenize
from nltk.tokenize import sent_tokenize
import sys, os
import codecs as cs

# invalid for vanilla, all_invalid for allpair, lookback2_invalid for lookback2
#invalid = [8820, 19084, 44800]
#all_invalid = []
#for i in range(0, 10):
#    for j in invalid:
#        all_invalid.append(j * 10 + i)
#lookback2_invalid = []
#for i in range(0, 5):
#    for j in invalid:
#        lookback2_invalid.append(j * 5 + i)
        
def main(source_file, q_file, r_file, kw_file):
    with cs.open(source_file, encoding='utf-8')as fin:
        for i, line in enumerate(fin):
            #if i in all_invalid: continue
            if i % 1000 == 0 and i > 0: print i
            if not line: continue  #line.startswith("<bos>") or 
            list = sent_tokenize(line)
            if len(list) == 1: 
                list = list[0].strip().split('\t')
            #q = tokenize(" ".join(list[:-1]))
            q = map(lambda x: ' '.join(x), map(tokenize, list[:-1]))
            q = ' '.join(q)
            r = tokenize(list[-1])
            kw = get_noun(r)
            r = ' '.join(r)
            q_file.write(q + "\n")
            r_file.write(r + "\n")
            kw_file.write(kw + "\n")
    print "Process %s file done!" % (source_file)
    q_file.close()
    r_file.close()
    kw_file.close()
    
if __name__ == "__main__":
    '''
    train_file = read_path + "rocstory.allpair.train"
    valid_file = read_path + "rocstory.allpair.val"
    
    train_q_file = open(write_path + "allpair.train.query", "w")
    train_r_file = open(write_path + "allpair.train.reply", "w")
    train_kw_file = open(write_path + "allpair.train.topic", "w")
    dev_q_file = open(write_path + "allpair.dev.query", "w")
    dev_r_file = open(write_path + "allpair.dev.reply", "w")
    dev_kw_file = open(write_path + "allpair.dev.topic", "w")
    '''

    read_path = sys.argv[1] #"../../Processed/"
    write_path = sys.argv[2] #"../../data/"
    file_name = sys.argv[3]
    train_file = os.path.join(read_path, file_name)
    
    train_q_file = cs.open(os.path.join(write_path, file_name + ".query"), "w", encoding='utf-8')
    train_r_file = cs.open(os.path.join(write_path, file_name + ".reply"), "w", encoding='utf-8')
    train_kw_file = cs.open(os.path.join(write_path, file_name + ".topic"), "w", encoding='utf-8')
    
    main(train_file, train_q_file, train_r_file, train_kw_file)
    #main(valid_file, dev_q_file, dev_r_file, dev_kw_file)
