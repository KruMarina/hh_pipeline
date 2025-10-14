#!/usr/bin/env python

import subprocess    # для запуска других программ
import sys
import logging
from pathlib import Path
from datetime import datetime


# логирование в файл и в консоль
log_dir = Path(__file__).parent / 'logs'
log_dir.mkdir(exist_ok = True)

log_filename = f'hh_pipeline_{datetime.now().strftime("%Y%m%d_%H%M%S")}.log'
log_filepath = log_dir / log_filename


logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler(log_filepath, encoding='utf-8'),   # в файл
        logging.StreamHandler(sys.stdout)
    ]
)

logger = logging.getLogger(__name__)   


def run_script(script_path, description, vacancy_name):
    
    try:
        script_dir = script_path.parent
        script_file = script_path.name
        
        if script_path.suffix == '.py':
            result = subprocess.run(
                ['python', script_file, vacancy_name],
                check=True, 
                capture_output=True, 
                text=True,
                cwd=script_dir
            )
        else:
            bash_path = r'C:\Users\Vivo\Git\usr\bin\bash.exe'    # для смешанного проекта (python + bash)
            result = subprocess.run(
                [bash_path, script_file], 
                check=True, 
                capture_output=True, 
                text=True,
                cwd=script_dir
            )
            
        logger.info(f'Успешно: {description} [{script_path.name}]')

        if result.stdout.strip():
            logger.info(f'{script_path.name}: {result.stdout.strip()}')

        return True
        
    except subprocess.CalledProcessError as e:
        logger.error(f'Ошибка в {script_path.name}: {e.stderr}')
        return False

def main(vacancy_name):
    project_root = Path(__file__).parent.parent

    data_dirs = [
        project_root / "data/raw",
        project_root / "data/processed", 
        project_root / "data/partitioned"
    ]
    
    for dir_path in data_dirs:
        dir_path.mkdir(parents=True, exist_ok=True)
    
    scripts = [
        ('01_fetch_data/fetch_vacancies.py', 'Извлечение вакансий'),
        ('02_convert_to_csv/json_to_csv.py', 'Конвертация в CSV'),
        ('03_sort_data/sorter.py', 'Сортировка данных'),
        ('04_change_data/cleaner.py', 'Обогащение данных'),
        ('05_aggregate_data/counter.py', 'Агрегация данных'),
        ('06_partition_data/partitioner.py', 'Партиционирование'),
        ('06_partition_data/concatenator.py', 'Конкатенация')
    ]
    
    logger.info(f'Запуск пайплайна для: "{vacancy_name}"')
    
    for script_rel_path, description in scripts:
        script_path = project_root / 'scripts' / script_rel_path
        
        if not run_script(script_path, description, vacancy_name):
            logger.error('Пайплайн прерван')
            return False
    
    logger.info('Пайплайн успешно завершен!')
    return True

if __name__ == '__main__':
    if len(sys.argv) != 2:
        print('Использование: python run_etl.py "вакансия"')
        sys.exit(1)
    
    success = main(sys.argv[1])
    sys.exit(0 if success else 1)