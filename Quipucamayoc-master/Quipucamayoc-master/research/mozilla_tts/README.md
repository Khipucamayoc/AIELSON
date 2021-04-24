# Train es_AR on Mozilla TTS

Trained using es_la phonemes. Only Griffin-Lim vocoder is available.

## Install
```
git clone https://github.com/mozilla/TTS.git
cd TTS
git checkout Tacotron2-iter-260K-824c091
```

## Set up configuration

Copy config_es_AR_260K.json to config folder
 
Replace Dockerfile with file in this repo

Replace requirements.txt with file in this repo

## Train
```bash
nvidia-docker run --ipc=host -u $(id -u):$(id -g) -it -rm -p 5002:5002 -v scripts:/scripts -v $(pwd)/scripts:/srv/app/scripts -v $(pwd)/data:/srv/app/data mozilla-tts python train.py --config_path scripts/config_es_AR_260k.json
```

## Pretrained Model
https://drive.google.com/drive/folders/11p1kJ2GugjGqzzeHRFbRMAhs0uyxHkhk?usp=sharing
