#-*- coding:utf-8 -*-
# AUTHOR:   fuzx
# FILE:     get_loss.py
# ROLE:     TODO (some explanation)
# CREATED:  2017-09-24 14:52:03
# MODIFIED: 2017-09-24 21:44:54


def main(log_file, result_file):
    result = open(result_file, "a+")
    result.write("Current log: " + log_file + "\n")
    with open(log_file, "r")as fin:
        for i, line in enumerate(fin):
            line = line.strip()
            if line.startswith('Valid'):
                _, value = line.split()
                result.write(value + "\n")
    result.close()
    
    
if __name__ == "__main__":
    #main("../allpair.twogate.log", "stat.txt")
    main("../origin/allpair.origin.log", "stat.txt")
