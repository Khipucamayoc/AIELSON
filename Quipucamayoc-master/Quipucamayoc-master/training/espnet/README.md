# Train ESPnet (Tacotron 2) on es_ES Victor Villarraza

## Requirements
* nvidia-docker2
* CUDA 10.0
* 16GB or larger GPU

## Install ESPnet and Kaldi
```bash
git clone https://github.com/espnet/espnet.git
git clone https://github.com/kaldi-asr/kaldi
cd kaldi/tools
cat INSTALL
extras/check_dependencies.sh # generates an apt install command
make -j <NUM-CPU>

./extras/install_openblas.sh
cd ../src/
./configure --openblas-root=../tools/OpenBLAS/install --cudatk-dir=/usr/local/cuda-10.0
```

## Modify M-AILABS recipe
Update sampling frequency fs=22050
```bash
vi run.sh
```

## Change Training Epochs
Update training epochs=1000
```bash
vi conf/tuning/train_pytorch_tacotron2.v3.yaml
```

## Train
```bash
cd espnet/docker
./run.sh --docker_gpu 0 --docker_egs m_ailabs/tts1 --ngpu 1 --lang es_ES --spk victor --tag es_AR_scratch
```

## Pretrained Models
[Private Google Drive Folder](https://drive.google.com/drive/folders/1v_BnOP6bi6Y8Aen4mWTSimzftfR5K9pR?usp=sharing)

## Colab
[Colab](../../colabs/TTS_ESPnet_es_AR.ipynb) 

# Fine-tune Peruvian Speaker on Argentinian Dataset

## Copy Training Example folder from m_ailabs
```bash
cd espnet/egs
mkdir es_PE
cd es_PE
cp -r ../m_ailabs/tts1 .
```

## Modify M-AILABS recipe
Overwrite es_PE/tts1/run.sh with es_PE/run.sh in this repo

Copy pretrained_model_download.sh to es_PE local
```bash
cp espnet/egs/arctic/tts1/local/pretrained_model_download.sh espnet/egs/es_PE/tts1/local/
```

Add es_ES_victor_train_trim_pytorch_es_AR_scratch to local/pretrained_model_download.sh with path:
https://drive.google.com/open?id=xxxx
```bash
vi pretrained_model_download.sh
```

Manually download pretrained es_AR model to downloads folder
```bash
mkdir es_ES_victor_train_trim_pytorch_es_AR_scratch
cd es_ES_victor_train_trim_pytorch_es_AR_scratch
touch .complete
```

Pretrained model should have conf, data, exp folders

## Create Dataset Folder
```bash
cd tts1/downloads/es_ES/by_book/male
mkdir es_PE
cd es_PE
mkdir all
```

## Copy Dataset
wavs folder with each wav file at 22050 Hz. Filenames should begin with 01, 02 to avoid sorting issues during data preparation phase.

Sorted metadata.csv file in LJSpeech with format `filename(no suffix)|text|text`. For example: 
```
47|Va a hacer una cosa aquí, ya tenemos algunos planes|Va a hacer una cosa aquí, ya tenemos algunos planes
```

## Train
```bash
cd espnet/docker
./run.sh --docker_gpu 0 --docker_egs es_PE/tts1 --ngpu 1 --tag espnet_es_PE_finetune
```
## Pretrained Models
[Private Google Drive Folder](https://drive.google.com/drive/folders/1NPh6mUFuHqqBYUo0J3NipYYf37vDUa79?usp=sharing)

## Colab
[Colab](../../colabs/TTS_ESPnet_es_PE.ipynb) 
