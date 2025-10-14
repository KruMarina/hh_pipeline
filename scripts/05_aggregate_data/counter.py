import csv
from pathlib import Path


def main():

    input_file = Path('../../data/processed/hh_positions.csv')
    output_file = Path('../../data/processed/hh_uniq_positions.csv')

    output_file.parent.mkdir(parents=True, exist_ok=True)


    with open(input_file, 'r', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        
        counts = {}
        for row in reader:
            position = row['name']
            counts[position] = counts.get(position, 0) + 1      # 0 если еще нет значений этого уровня (аналог defaultdict(int))
                                                            

    with open(output_file, 'w', newline='', encoding='utf-8') as f:
        writer = csv.writer(f)
        writer.writerow(['name', 'count', 'percentage'])
        
        total = sum(counts.values())
        for position, count in counts.items():
            percentage = (count / total) * 100
            writer.writerow([position, count, f"{percentage:.1f}%"])


if __name__ == '__main__':
    main()

