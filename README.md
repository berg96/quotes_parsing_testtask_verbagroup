# Проект Quotes Parsing 

## Описание проекта 

Проект реализован на фреймворке Scrapy и включает в себя парсинг сайта [Quotes to Scrape](https://quotes.toscrape.com/) ([https://quotes.toscrape.com/](https://quotes.toscrape.com/)) с записью результатов в папку results файл 'quotes_ДатаВремя.json', в котором записаны все цитаты, автор каждой и связанные с ней теги. А также создается База Данных SQLite с таблицей Quote.

### Автор backend Артём Куликов

tg: [@Berg1005](https://t.me/berg1005)

[GitHub](https://github.com/berg96)

## Используемые технологии 

Проект использует реляционную базу данных SQLite для хранения данных и реализован на языке python c использованием следующего технгологического стека:

* Scrapy
* SQLAlchemy

## Как запустить проект

Клонировать репозиторий:
```
git clone https://github.com/berg96/quotes_parsing_testtask_verbagroup.git
```
Перейти в него в командной строке:
```
cd quotes_parsing_testtask_verbagroup
```
Cоздать и активировать виртуальное окружение:

```
python -m venv venv
```

* Если у вас Linux/macOS

    ```
    source venv/bin/activate
    ```

* Если у вас windows

    ```
    source venv/scripts/activate
    ```

Установить зависимости из файла requirements.txt:

```
python -m pip install --upgrade pip

pip install -r requirements.txt
```

Запустить паука:

```
scrapy crawl quotes
```
