import csv
import os
from datetime import datetime


input_file = '../../data/processed/hh_positions.csv'
output_dir = '../../data/partitioned'


os.makedirs(output_dir, exist_ok=True)


with open(input_file, 'r', encoding='utf-8') as f:
    reader = csv.DictReader(f)
    data = list(reader)  # тащит в память все данные 


files_by_date = {}
for row in data:

    date = row['created_at'].split('T')[0]
    
    if date not in files_by_date:
        files_by_date[date] = []
    files_by_date[date].append(row)


for date, rows in files_by_date.items():
    output_file = os.path.join(output_dir, f'{date}.csv')
    with open(output_file, 'w', newline='', encoding='utf-8') as f:
        writer = csv.DictWriter(f, fieldnames=reader.fieldnames)
        writer.writeheader()
        writer.writerows(rows)


