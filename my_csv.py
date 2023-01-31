import gzip
import csv
import json


def create_csv(input_file='train.jsonl.gz', output_name='Data.csv'):
    f = open(output_name, 'w', newline='')
    writer = csv.writer(f)
    with gzip.open(input_file, 'r') as fin:
        for line in fin:
            data = json.loads(line.decode('utf-8'))
            writer.writerow([data["text"], data["label"]])
    f.close()
