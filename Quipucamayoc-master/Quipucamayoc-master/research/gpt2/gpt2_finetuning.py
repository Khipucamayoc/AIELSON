import os
import shutil
import gpt_2_simple as gpt2
from datetime import datetime

model_name = '355M'
if not os.path.isdir(os.path.join('models', model_name)):
	print(f'Downloading {model_name} model...')
	gpt2.download_gpt2(model_name=model_name)

merge_filename = 'train.txt'

with open(merge_filename,'wb') as wfd:
    for f in ['../../Data/.txt/Eielson', '../../Data/.txt/PaolaPoetry', '../../Data/.txt/Vicuña']:
        with open(f,'rb') as fd:
            shutil.copyfileobj(fd, wfd)

sess = gpt2.start_tf_sess()
gpt2.finetune(sess,
    dataset=merge_filename,
    model_name=model_name,
    steps=2000,
    restore_from='fresh',
    run_name='run1',
    print_every=10,
    sample_every=200,
    save_every=500
    )

gpt2.generate(sess)
