import csv
import os

input_dir = '../../data/partitioned'
output_file = '../../data/partitioned/concatenated.csv'


csv_files = [f for f in os.listdir(input_dir) if f.endswith('.csv') and len(f) == 14]   # YYYY-MM-DD.csv
# os.listdir получает список файлов в папке
csv_files.sort()

if not csv_files:
    print("Нет файлов для объединения")
    exit(0)

all_data = []
fieldnames = None   # пока не знаем колонки в файлах


for filename in csv_files:
    with open(os.path.join(input_dir, filename), 'r', encoding='utf-8') as f:   # os.path.join() делает правильный разделитель (кроссплатформенность)
                                                                               
        reader = csv.DictReader(f)  # работает итеративно
        if fieldnames is None:
            fieldnames = reader.fieldnames  # если это первый файл, вытаскиваем названия
        all_data.extend(list(reader))


with open(output_file, 'w', newline='', encoding='utf-8') as f:
    writer = csv.DictWriter(f, fieldnames=fieldnames)
    writer.writeheader()
    writer.writerows(all_data)
