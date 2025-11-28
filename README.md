# ETL Pipeline для вакансий HH.ru

Проект представляет собой полноценный ETL пайплайн для сбора и анализа вакансий с API HH.ru с оркестрацией в Airflow. 



## Цель проекта

Создать программу для сбора данных о вакансиях, их обработки и подготовки к аналитике.

### Технологический стек

- **Python** - язык разработки (3.13 для ручного запуска, 3.11 в Docker)
- **Apache Airflow** - оркестрация
- **Docker** - контейнеризация
- **PostgreSQL** - база данных для Airlfow
- **SQLite** - база данных для результатов ETL
- **Requests** - работа с HTTP API 
- **CSV/JSON** - форматы хранения данных
- **Logging** - логирование выполнения пайплайна
- **Pathlib** - кроссплатформенная работа с путями

### ETL Пайплайн состоит из 7 этапов:

1. **Extract** - получение данных через API HH.ru
2. **Convert** - преобразование из JSON в CSV
3. **Sort** - сортировка вакансий по дате создания
4. **Enrich** - обогащение данных (определение уровня позиции)
5. **Aggregate** - агрегация и статистика + сохранение в SQLite
6. **Partition** - партиционирование по датам
7. **Concatenate** - объединение файлов



## Запуск

### Локальный ETL (docker-compose.yml)

```bash
docker-compose run --rm etl python src/run_etl.py "Data Engineer"
# docker-compose run --rm etl python src/run_etl.py "Data Scientist"
# docker-compose run --rm etl python src/run_etl.py "Data Analyst"
```


### Локальный ETL с просмотром БД

```bash
docker-compose run --rm etl bash -c "python src/run_etl.py 'Data Engineer' && python view.py"
# docker-compose run --rm etl bash -c "python src/run_etl.py 'Data Scientist' && python view.py"
# docker-compose run --rm etl bash -c "python src/run_etl.py 'Data Analyst' && python view.py"
```


### Production с Airflow (docker-compose-airflow.yml)

```bash
docker-compose -f docker-compose-airflow.yml up -d    # запуск
docker-compose -f docker-compose-airflow.yml logs -f   # логи
docker-compose -f docker-compose-airflow.yml down     # остановка
```

### Ручной запуск (без Docker)

```bash
pip install requests pandas
python src/run_etl.py "Data Engineer"
python view.py
```



## Решение проблем

### Права доступа (Windows):

Проект автоматически использует container-native хранилище (/tmp) для обхода ограничений Docker volumes на Windows

**Если всё равно возникают ошибки прав:**

```bash
# Дать права на data папку (Linux/Mac)
chmod -R 755 data
```

### Модули потерялись

Все пути управляются через scripts/config.py



## Эволюция проекта

Проект начинался как учебное задание, но был усовершенствован.

### Рефакторинг архитектуры

- **Было**: Разрозненные bash-скрипты 
- **Стало**: Единый Python пайплайн с кроссплатформенной работой и Docker контейнеризацией

### Улучшения

- Контейнеризация с Docker
- Оркестрация с Apache Airflow
- PostgreSQL для Airflow 
- SQLite база данных для результатов
- Логирование в файл и консоль
- Обработка ошибок на каждом этапе  
- Четкая структура папок

### Результат

Учебное задание превратилось в полноценный ETL пайплайн, демонстрирующий понимание полного цикла данных и готовый к использованию в production