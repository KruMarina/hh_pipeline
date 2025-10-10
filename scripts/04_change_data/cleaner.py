import csv


with open('../../data/processed/hh_sorted.csv', 'r', encoding='utf-8') as f:
    reader = csv.DictReader(f)
    rows = list(reader)


for row in rows:
    name = row['name'].lower()
    if 'junior' in name:
        row['name'] = 'Junior'
    elif 'middle' in name:
        row['name'] = 'Middle' 
    elif 'senior' in name:
        row['name'] = 'Senior'
    else:
        row['name'] = '-'


with open('../../data/processed/hh_positions.csv', 'w', newline='', encoding='utf-8') as f:
    writer = csv.DictWriter(f, fieldnames=reader.fieldnames)
    writer.writeheader()
    writer.writerows(rows)
