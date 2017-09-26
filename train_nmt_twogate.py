import numpy
import os

from nmt_all_twogate import train

def main(job_id, params):
    print(params)
    validerr = train(saveto=params['model'][0],
                     reload_=params['reload'][0],
                     dim_word=params['dim_word'][0],
                     dim=params['dim'][0],
                     n_words=params['n-words'][0],
                     n_words_src=params['n-words'][0],
                     decay_c=params['decay-c'][0],
                     clip_c=params['clip-c'][0],
                     lrate=params['learning-rate'][0],
                     optimizer=params['optimizer'][0],
                     patience=5,
                     maxlen=70,
                     batch_size=50,
                     valid_batch_size=50,
                     validFreq=500,
                     dispFreq=50,
                     saveFreq=500,
                     sampleFreq=500,
                     datasets=['../data/allpair.train.query',
                               '../data/allpair.train.reply',
                               '../data/allpair.train.topic'],
                     valid_datasets=['../data/allpair.dev.query',
                                     '../data/allpair.dev.reply',
                                     '../data/allpair.dev.topic'],
                     dictionaries=['../data/rocstory.vanilla.train.pkl',
                                   '../data/rocstory.vanilla.train.pkl'],
                     use_dropout=params['use-dropout'][0],
                     overwrite=False)
    return validerr

if __name__ == '__main__':
    main(0, {
        'model': ['../model/allpair/twogate/model_twogate.npz'],
        'dim_word': [620],
        'dim': [1024],
        'n-words': [28000],  # 27644
        'optimizer': ['adadelta'],
        'decay-c': [0.],
        'clip-c': [1.],
        'use-dropout': [False],
        'learning-rate': [0.0001],
        'reload': [False]})
