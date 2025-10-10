import csv
import os

input_file = '../../data/raw/hh.csv'
output_file = '../../data/processed/hh_sorted.csv'


with open(input_file, 'r', encoding='utf-8') as f:
    reader = csv.DictReader(f)
    data = list(reader)


data_sorted = sorted(data, key=lambda x: (x['created_at'], x['id']))     # по дате и id


os.makedirs('../../data/processed', exist_ok=True)


with open(output_file, 'w', newline='', encoding='utf-8') as f:
    writer = csv.DictWriter(f, fieldnames=reader.fieldnames)
    writer.writeheader()        # запись заголовка
    writer.writerows(data_sorted)
