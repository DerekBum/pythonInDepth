# nl

Для запуска скрипта нужно ввести команду с терминала:

```bash
python3 nl.py <file>
```

`file` -- опциональный путь до файла с текстом.
Если путь до файла не задан, скрипт будет работать на вводе 
пользователя через `stdin`.

## Работа с файлом

Пример можно запустить командой
```bash
python3 nl.py ./artifacts/example.txt
```

Вывод скрипта:
![image](artifacts/pictures/nl_file.png)

Для сравнения вывод утилиты *nl*:
![image](artifacts/pictures/nl_orig.png)

## Работа с пользовательским вводом

```bash
python3 nl.py
```

Для окончания работы можно передать `KeyboardInterrupt` символ (`Ctrl-C`).

Пример работы:
![image](artifacts/pictures/nl_stdin.png)

## Нет файла

Если файла не существует, выводы утилиты и скрипта будут одинаковы:

![image](artifacts/pictures/error.png)
