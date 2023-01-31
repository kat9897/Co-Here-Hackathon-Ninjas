import gzip
import csv
import json

f = open('Data.csv', 'w', newline='')
writer = csv.writer(f)
with gzip.open('train.jsonl.gz', 'r') as fin:
    for line in fin:
        data = json.loads(line.decode('utf-8'))
        writer.writerow([data["text"], data["label"]])
f.close()
