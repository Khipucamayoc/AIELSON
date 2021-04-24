# M-AILABS Spanish Argentinian Dataset

## Utterance length chart

![Chart of Utterance Length for Victor](https://github.com/Khipucamayoc/Quipucamayoc/raw/master/Data/M-AILABS_es_ES/durations_es_ES_vv.png)


## Create Text Alignment Files for Victor Villarraza
join all metadata.csv files across all books for Victor
```bash
cat male/victor_villarraza/*/metadata.csv >> metadata.csv.start
```
Remove all " characters, unmatched " causing problems with csv parsing.
```bash
sed 's/\"//g' metadata.csv.start > metadata_noquotes.csv
```

Execute metadata.py to select only those utterances between 3 and 10 seconds, add folder path and .wav suffix, and remove third column:
```bash
python metadata.py
```

If needed, splittrainval.py to create separate metadata files for training and validation:
```bash
python splittrainval.py
```

## Upsample WAV files
Train files at 22050 to match MelGAN/waveglow training.

Copy all Victor WAV files to one directory
```bash
find es_ES/es_ES/by_book/male/victor_villarraza/*/wavs/ -type f -name *.wav -exec cp {} wavs16_vv \;
```

Use resample_trim_wav.sh to upsample to 22050 and trim the first 1/2 second and last 1/2 second of silence.
```bash
./resample_trim_wav.sh
```

# Create Dataset for all Spanish Speakers

## Create Text Alignment Files
join all metadata.csv files across all books
```bash
cat female/*/*/metadata.csv male/*/*/metadata.csv mix/*/metadata.csv >> metadata.csv.start
```
Remove all " characters, unmatched " causing problems with csv parsing.
```bash
sed 's/\"//g' metadata.csv.start > metadata_noquotes.csv
```
Execute metadata.py to select only those utterances between 3 and 10 seconds, to add folder path and .wav suffix, and remove third column:
```bash
python metadata.py
```
Copy all WAV files to one directory 
```bash
find by_book/*/*/wavs/ -type f -name *.wav -exec cp {} wavs16 \;
find by_book/mix/*/*/wavs/ -type f -name *.wav -exec cp {} wavs16 \;
```
Use resample_trim_wav.sh to upsample to 22050 and trim the first 1/2 second and last 1/2 second of silence.
```bash
./resample_trim_wav.sh
```

If needed, splittrainval.py to create separate metadata files for training and validation:
```bash
python splittrainval.py
```

### One missing WAV file
lacondenada_17_blasco_f000001.wav

