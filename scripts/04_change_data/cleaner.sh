#!/bin/sh



# ПЕРВАЯ ВЕРСИЯ СКРИПТА (учебная)
# столкнулась с проблемой кроссплатформенности + необходимостью установки внешних утилит
# в программе используется усовершенствованный код из cleaner.py



INPUT_FILE="../../data/processed/hh_sorted.csv"
OUTPUT_FILE="../../data/processed/hh_positions.csv"


head -n 1 "$INPUT_FILE" > "$OUTPUT_FILE"

tail -n +2 "$INPUT_FILE" | while IFS= read -r line; do
    # IFS= - не делить строку на части  
    # -r - игнорировать слэши

    myay=""

    if echo "$line" | grep -qi "Junior"; then       # q = quiet, i = игнор регистра
        myay="Junior"                               # grep - команда поиска текста
    fi

    if echo "$line" | grep -qi "Middle"; then
        if [ -n "$myay" ]; then      # -n = "если не пустая"
            myay="$myay/Middle"
        else
            myay="Middle"
        fi
    fi

    if echo "$line" | grep -qi "Senior"; then
        if [ -n "$myay" ]; then
            myay="$myay/Senior"
        else
            myay="Senior"
        fi
    fi


    if [ -z "$myay" ]; then     # # Если уровень непонятен   
        myay='-'
    fi



    new_line=$(echo "$line" | sed -E "s~\"[^\"]*\"~\"$myay\"~3")    # # sed -E....~3" - заменить третье вхождение

    echo "$new_line" >> "$OUTPUT_FILE"

    myay=""
done
