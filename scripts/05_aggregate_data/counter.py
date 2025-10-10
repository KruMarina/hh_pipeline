import csv


with open('../../data/processed/hh_positions.csv', 'r', encoding='utf-8') as f:
    reader = csv.DictReader(f)
    
    counts = {}
    for row in reader:
        position = row['name']
        counts[position] = counts.get(position, 0) + 1      # 0 если еще нет значений этого уровня (аналог defaultdict(int))
                                                        

with open('../../data/processed/hh_uniq_positions.csv', 'w', newline='', encoding='utf-8') as f:
    writer = csv.writer(f)
    writer.writerow(['name', 'count', 'percentage'])
    
    total = sum(counts.values())
    for position, count in counts.items():
        percentage = (count / total) * 100
        writer.writerow([position, count, f"{percentage:.1f}%"])

