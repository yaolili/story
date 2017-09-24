#-*- coding:utf-8 -*-
# AUTHOR:   fuzx
# FILE:     clear_model.py
# ROLE:     TODO (some explanation)
# CREATED:  2017-09-24 11:08:23
# MODIFIED: 2017-09-24 11:08:25

import os

path = "../../model/"

def clear(model, best_iter):
    num = best_iter * 2
    prefix = path + model + "/model_" + model + ".iter"
    while True:
        file = prefix + str(num) + ".npz"
        if not os.path.isfile(file): break
        cmd = "rm " + file
        os.system(cmd)
        num += 500

if __name__ == "__main__":
    clear("origin", 12000)
    clear("twogate", 12000)