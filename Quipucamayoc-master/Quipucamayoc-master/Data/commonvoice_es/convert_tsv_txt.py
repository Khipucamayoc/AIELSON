import pandas as pd
import os
fp = open('cmnvoice_audio_text_train_filelist.txt', 'w')
for file in ['train.tsv']:
  df = pd.read_csv(file, sep='\t')
  for path, sentence in zip(df['path'].to_list(), df['sentence'].to_list()):
    path = path[:-4]
    fp.write(f"/data/es_commonvoice/clips/{path}.wav|{sentence}\n")
fp.close()

fpt = open('cmnvoice_audio_text_test_filelist.txt', 'w')
for file in ['test.tsv']:
  df = pd.read_csv(file, sep='\t')
  for path, sentence in zip(df['path'].to_list(), df['sentence'].to_list()):
    path = path[:-4]
    fpt.write(f"/data/es_commonvoice/clips/{path}.wav|{sentence}\n")
fpt.close()

fpv = open('cmnvoice_audio_text_val_filelist.txt', 'w')
for file in ['dev.tsv']:
  df = pd.read_csv(file, sep='\t')
  for path, sentence in zip(df['path'].to_list(), df['sentence'].to_list()):
    path = path[:-4]
    fpv.write(f"/data/es_commonvoice/clips/{path}.wav|{sentence}\n")
fpv.close()
