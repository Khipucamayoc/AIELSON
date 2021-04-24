# Common Voice Spanish Dataset
## Create Text Alignment Files
```
python convert_tsv_txt.py
```

## Create WAV Files
Train files at 22050 to match MelGAN/waveglow training. When converting, decrease the gain automatically with -G to avoid decrease volume errors.
```
for f in *.mp3; do sox -G "$f" -r 22050  "${f%.*}.wav"; done	
```

## Missing WAV Files
two missing WAV files listed in training.vst, ran findmissing.py
* common_voice_es_19499893.wav
* common_voice_es_19499901.wav

