import json
import csv
from pathlib import Path



def main():
    input_path = Path('../../data/raw/hh.json')
    output_path = Path('../../data/raw/hh.csv')
    
    with open(input_path, 'r', encoding='utf-8') as f:
        data = json.load(f)
    
    headers = ["id", "created_at", "name", "has_test", "alternate_url"]
    
    with open(output_path, 'w', newline='', encoding='utf-8') as f:     # newline отключает автообработку переносов строк
        writer = csv.writer(f)
        writer.writerow(headers)
        
        for item in data.get('items', []):   # получаем пустой список если нет items
            row = [item.get(field) for field in headers]
            writer.writerow(row)
    


if __name__ == '__main__':
    main()