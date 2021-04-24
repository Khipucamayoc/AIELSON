#!/bin/bash
find . -type f -name "*.wav" -exec sh -c '
for wavfilepath; do # Whitespace-safe and recursive
    wavfile=$(basename "${wavfilepath}")
    
    sox $wavfilepath "../trimmed/$wavfile" trim 0.5 reverse trim 0.5 reverse
done
' _ {} +
