# NVIDIA tacotron-2 trained on es_AR Spanish
```bash
git clone https://github.com/NVIDIA/tacotron2
cd tacotron2
git submodule init; git submodule update

```

## Create Spanish Cleaner
replace cleaners.py and symbols.py in text folder

## Conda Env
```bash
conda create -n taco2_p36 python=3.6
conda activate taco2_p36
conda install pytorch==1.2.0 cudatoolkit=10.0 -c pytorch
conda install future
pip install matplotlib tensorflow-gpu==1.15.2 numpy inflect librosa scipy Unidecode pillow
```
Install Apex
```bash
cd ..
git clone https://github.com/NVIDIA/apex
cd apex
pip install -v --no-cache-dir --global-option="--cpp_ext" --global-option="--cuda_ext" ./
cd ../tacotron2
```

## Update hparams.py
```bash
training_files='filelists/vv_3to10sec_train_metadata.txt',
validation_files='filelists/vv_3to10sec_val_metadata.txt',
text_cleaners=['es_cleaners'],
batch_size=64
```

## Train
```
python train.py --output_directory=outdir --log_directory=logdir
```

## Pretrained Models
[Private Google Drive Folder](https://drive.google.com/drive/folders/1NPzfbVITBYhxnUhSD85mhw85fN2NNoYB?usp=sharing)

## Colab
[Colab](../../colabs/TTS_NVIDIA_Tacotron2_es_AR.ipynb)

The WaveGlow vocoder generates a high-pitched whine, that can be removed with a high pass filter.

# Fine-tune es_AR with es_PE dataset

## Update hparams.py for fine-tuning
```
python train.py --output_directory=outdir --log_directory=logdir -c outdir_cuda10.0_torch1.2_ffmpeg_final_2/checkpoint_215000 --warm_start
```

## Pretrained Models
[Private Google Drive Folder](https://drive.google.com/drive/folders/1BK3aK1-ww44E1Ma3iCnkJDuW65e_LN5o?usp=sharing)

## Colab
[Colab](../../colabs/TTS_NVIDIA_Tacotron2_es_PE.ipynb)

The WaveGlow vocoder generates a high-pitched whine, that can be removed with a high pass filter.
