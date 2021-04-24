import os
import glob
import csv

csv_filenames = glob.glob('cmnvoice*.txt')

for csv_filename in csv_filenames:
    with open(csv_filename) as csv_file:
        csv_reader = csv.reader(csv_file, delimiter='|')
        for row in csv_reader:
            filename = row[0]

            try:
                if os.stat(filename).st_size == 0:
                    print(f'{filename} in {csv_filename} is empty')
            except OSError:
                print(f'{filename} in {csv_filename} missing')


