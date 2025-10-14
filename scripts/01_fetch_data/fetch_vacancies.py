import sys
import requests
import json
import urllib.parse
from pathlib import Path


def main():
    if len(sys.argv) != 2:
        print("Write: python fetch_vacancies.py 'название вакансии'")
        exit(1)
    
    vacancy_name = sys.argv[1]
    
    vacancy_encoded = urllib.parse.quote(vacancy_name)   # кодируем для URL
    
    url = f"https://api.hh.ru/vacancies?text={vacancy_encoded}&per_page=20"
    
    response = requests.get(url)
    response.raise_for_status() 

    data = response.json()   # делаем словарь из текста
    
    output_path = Path('../../data/raw/hh.json')   # делает правильные разделители для всех ОС
    output_path.parent.mkdir(parents=True, exist_ok=True)
    
    with open(output_path, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=2) 

        # ensure_ascii=False — разрешает сохранение не-ASCII символов (кириллицы, иероглифов и т.д.)
    


if __name__ == '__main__':
    main()