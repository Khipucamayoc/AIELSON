#!/bin/bash

find wavs16_vv/ -type f -name "*.wav" -exec sh -c '
for wavfilepath; do
    wavfile=${wavfilepath#wavs16_vv/}
    echo $wavfile
    ffmpeg -i ${wavfilepath}  -ar 22050 -ac 1 -f wav -y wavs22_vv/${wavfile};
    sox wavs22_vv/${wavfile} wavs22trimmed_vv/${wavfile} trim .5 -.5;
done
' _ {} +