# tail

Для запуска скрипта нужно ввести команду с терминала:

```bash
python3 wc.py <files>
```

`files` -- опциональные пути до файлов с текстом.
Если пути до файла не заданы, скрипт будет работать на вводе 
пользователя через `stdin`.

## Работа с файлами

Пример с одиночным файлом можно запустить командой
```bash
python3 wc.py artifacts/example1.txt
```

Сравнение скрипта и утилиты:
![image](./artifacts/pictures/wc_1.png)

Пример с несколькими файлами можно запустить командой
```bash
python3 wc.py artifacts/example1.txt artifacts/example2.txt
```

Сравнение скрипта и утилиты:
![image](./artifacts/pictures/wc_2.png)

## Работа с пользовательским вводом

```bash
python3 wc.py
```

Для окончания работы нужно передать `EOF` символ (`Ctrl-D`).

Пример работы:
![image](./artifacts/pictures/wc_stdin.png)

## Нет файла

Если файла не существует, выводы утилиты и скрипта будут одинаковы:

![image](artifacts/pictures/error.png)
