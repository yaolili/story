import numpy
import os

import numpy
import os

from nmt import train

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
                     optimizer=params['optimizer'][-1],
                     patience=10,
                     maxlen=70,
                     batch_size=50,
                     valid_batch_size=50,
                     validFreq=500,
                     dispFreq=100,
                     saveFreq=500,
                     sampleFreq=500,
                     datasets=['../../data/rocstory.pad-lookback-1.train.query',
                               '../../data/rocstory.pad-lookback-1.train.reply',
                               '../../data/rocstory.pad-lookback-1.train.topic'],
                     valid_datasets=['../../data/rocstory.pad-lookback-1.val.query',
                                     '../../data/rocstory.pad-lookback-1.val.reply',
                                     '../../data/rocstory.pad-lookback-1.val.topic'],
                     dictionaries=['../../data/rocstory.pad-allpair.val.pkl',
                                   '../../data/rocstory.pad-allpair.val.pkl'],
                     #datasets=['../../data/lookback2.train.query',
                     #          '../../data/lookback2.train.reply',
                     #          '../../data/lookback2.train.topic'],
                     #valid_datasets=['../../data/lookback2.dev.query',
                     #                '../../data/lookback2.dev.reply',
                     #                '../../data/lookback2.dev.topic'],
                     #dictionaries=['../../data/rocstory.vanilla.train.pkl',
                     #              '../../data/rocstory.vanilla.train.pkl'],
                     use_dropout=params['use-dropout'][0],
                     overwrite=False)
    return validerr

if __name__ == '__main__':
    main(0, {
        'model': ['../../model/origin/model_origin_lookback-1_debug.npz'],
        'dim_word': [620],
        'dim': [1024],
        'n-words': [36480], #80600],  # 80526
        'optimizer': ['adadelta', 'adam'],  #, 'sgd'
        'decay-c': [0.],
        'clip-c': [1.],
        'use-dropout': [True],
        'learning-rate': [0.001],
        'reload': [False]})
