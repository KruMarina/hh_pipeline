import csv
import os
from pathlib import Path


def main():

    input_file = Path('../../data/raw/hh.csv')
    output_file = Path('../../data/processed/hh_sorted.csv')

    output_file.parent.mkdir(parents=True, exist_ok=True)

    with open(input_file, 'r', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        data = list(reader)


    data_sorted = sorted(data, key=lambda x: (x['created_at'], x['id']))     # по дате и id


    with open(output_file, 'w', newline='', encoding='utf-8') as f:
        writer = csv.DictWriter(f, fieldnames=reader.fieldnames)
        writer.writeheader()        # запись заголовка
        writer.writerows(data_sorted)


if __name__ == '__main__':
    main()
