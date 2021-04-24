#!/bin/bash

find wavs/ -type f -name "*.wav" -exec sh -c '
for wavfilepath; do # Whitespace-safe and recursive
    txtfile=${wavfilepath%wav}txt
    $( dos2unix ${txtfile} )
    transcription=$( tr "\n" " " < ${txtfile} )
    echo "${wavfilepath}|${transcription}" >> metadata.csv;
done
' _ {} +
