# tail

Для запуска скрипта нужно ввести команду с терминала:

```bash
python3 tail.py <files>
```

`files` -- опциональные пути до файлов с текстом.
Если пути до файла не заданы, скрипт будет работать на вводе 
пользователя через `stdin`.

## Работа с файлами

Пример с одиночным файлом можно запустить командой
```bash
python3 tail.py artifacts/example1.txt
```

Вывод скрипта:
![image](./artifacts/pictures/tail_1.png)

Для сравнения вывод утилиты *tail*:
![image](./artifacts/pictures/tail_1_orig.png)

Пример с несколькими файлами можно запустить командой
```bash
python3 tail.py artifacts/example1.txt artifacts/example2.txt
```

Вывод скрипта:
![image](./artifacts/pictures/tail_2.png)

Для сравнения вывод утилиты *tail*:
![image](./artifacts/pictures/tail_2_orig.png)

## Работа с пользовательским вводом

```bash
python3 tail.py
```

Для окончания работы нужно передать `EOF` символ (`Ctrl-D`).

Пример работы:
![image](./artifacts/pictures/tail_stdin.png)

## Нет файла

Если файла не существует, выводы утилиты и скрипта будут одинаковы:

![image](artifacts/pictures/error.png)
