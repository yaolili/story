#-*- coding:utf-8 -*-
# AUTHOR:   fuzx
# FILE:     process_vallina.py
# ROLE:     TODO (some explanation)
# CREATED:  2017-09-23 16:50:16
# MODIFIED: 2017-09-23 16:50:22

from util import get_noun
from nltk.tokenize import sent_tokenize

read_path = "../../Processed/"
write_path = "../../data/"


invalid = [8820, 19084, 44800]
all_invalid = []
for i in range(0, 10):
    for j in invalid:
        all_invalid.append(j * 10 + i)
        
def main(source_file, q_file, r_file, kw_file):
    with open(source_file)as fin:
        for i, line in enumerate(fin):
            if i in invalid: continue
            if i % 1000 == 0: print i
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
    train_file = read_path + "rocstory.vanilla.train"
    valid_file = read_path + "rocstory.vanilla.val"
    
    train_q_file = open(write_path + "vanilla.train.query", "w")
    train_r_file = open(write_path + "vanilla.train.reply", "w")
    train_kw_file = open(write_path + "vanilla.train.topic", "w")
    dev_q_file = open(write_path + "vanilla.dev.query", "w")
    dev_r_file = open(write_path + "vanilla.dev.reply", "w")
    dev_kw_file = open(write_path + "vanilla.dev.topic", "w")
    
    main(train_file, train_q_file, train_r_file, train_kw_file)
    main(valid_file, dev_q_file, dev_r_file, dev_kw_file)
        

   
            
        