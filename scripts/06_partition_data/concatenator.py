import csv
from pathlib import Path


def main():
    input_dir = Path('../../data/partitioned')
    output_file = Path('../../data/partitioned/concatenated.csv')

    csv_files = [
        f for f in input_dir.iterdir() 
        if f.is_file() and f.suffix == '.csv' and len(f.stem) == 10  # YYYY-MM-DD
    ]
    
    csv_files.sort()

    if not csv_files:
        print("Нет файлов для объединения")
        return

    all_data = []
    fieldnames = None

    for file_path in csv_files:
        with open(file_path, 'r', encoding='utf-8') as f:
            reader = csv.DictReader(f)
            if fieldnames is None:
                fieldnames = reader.fieldnames
            all_data.extend(list(reader))


    output_file.parent.mkdir(parents=True, exist_ok=True)

    with open(output_file, 'w', newline='', encoding='utf-8') as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(all_data)



if __name__ == '__main__':
    main()
