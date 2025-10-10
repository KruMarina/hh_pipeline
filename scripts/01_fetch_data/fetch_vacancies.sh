#!/bin/sh


# ПЕРВАЯ ВЕРСИЯ СКРИПТА (учебная)
# столкнулась с проблемой кроссплатформенности + необходимостью установки внешних утилит
# в программе используется усовершенствованный код из fetch_vacancies.py



if [ -z "$VACANCY_NAME" ]; then                     # -z = true если строка пустая
    echo "Использование: VACANCY_NAME='Data Scientist' python run_etl.py"
    exit 1
fi

VACANCY=$(jq -n --arg vacancy "$VACANCY_NAME" '$vacancy | @uri')    # jq создает перемен $vacancy и применяет к ней фильтр @uri (в URL-формат)

curl -s "https://api.hh.ru/vacancies?text=$VACANCY&per_page=20" | jq '.' > ../../data/raw/hh.json

# jq '.' - передает json без изменений

