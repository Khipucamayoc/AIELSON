import csv
import re
import sys 
import random

csv_metadatas = ['metadata3to10sec.csv']

csv.field_size_limit(sys.maxsize)

for idx, csv_metadata in enumerate(csv_metadatas):
  with open(csv_metadata, 'r') as csv_input_file:
    csv_reader = csv.reader(csv_input_file, delimiter='|')
    with open(f'train_metadata.csv', 'w') as csv_file:
      with open(f'val_metadata.csv', 'w') as val_csv_file:
        csv_writer = csv.writer(csv_file, delimiter='|')
        val_csv_writer = csv.writer(val_csv_file, delimiter='|')
        line_count = 0
        for row in csv_reader:
            line_count += 1
            if row[0] == "":
                print("failed")
            filename = row[0]
            text = row[1]
            s = random.randint(0, 9)
            if s == 0:
                val_csv_writer.writerow([filename, text])
            else:
                csv_writer.writerow([filename, text])
        print(f'Processed {line_count} lines.')