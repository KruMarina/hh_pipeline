import csv
from pathlib import Path
from datetime import datetime


def main():


    input_file = Path('../../data/processed/hh_positions.csv')
    output_dir = Path('../../data/partitioned')


    output_dir.mkdir(parents=True, exist_ok=True)


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
        output_file = output_dir / f'{date}.csv'
        with open(output_file, 'w', newline='', encoding='utf-8') as f:
            writer = csv.DictWriter(f, fieldnames=reader.fieldnames)
            writer.writeheader()
            writer.writerows(rows)



if __name__ == '__main__':
    main()

