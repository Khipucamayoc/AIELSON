import csv
import re
import sys
import sox

csv_metadata = 'metadata_noquotes.csv'

csv.field_size_limit(sys.maxsize)

with open(csv_metadata, 'r') as csv_input_file:
  csv_reader = csv.reader(csv_input_file, delimiter='|')
  with open(f'metadata3to10sec.csv', 'w') as csv_file:
    csv_writer = csv.writer(csv_file, delimiter='|')
    line_count = 0
    for row in csv_reader:
        line_count += 1
        if row[0] == "":
          print('failed')
        seconds = sox.file_info.duration(f'wavs/{row[0]}.wav')
        if seconds >= 4 and seconds <= 11:  # durations 3 to 10 seconds after 1 second trimmed
          filename = "/data/es_ES/wavs/" + row[0] + ".wav"
          text = row[1]
          csv_writer.writerow([filename, text])
        else:
          print(seconds)
    print(f'Processed {line_count} lines.')