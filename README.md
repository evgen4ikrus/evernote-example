# evernote-example
Утилита для работы с API Evernote.
### Как установить

Для работы со скриптами вам понадобится Python третьей версии.

Скачайте код с GitHub. Затем установите зависимости:

```sh
pip install -r requirements.txt
```
### Переменные окружения
Для работы с API Evernote вам потребуется создать файл .env в папке с проектом.
В файле создать несколько переменных окружения:
* EVERNOTE_CONSUMER_KEY и EVERNOTE_CONSUMER_SECRET получите по [ссылке](https://dev.evernote.com/doc/).
* EVERNOTE_PERSONAL_TOKEN получите [здесь](https://dev.evernote.com/get-token/).
* Создайте свой первый блокнот на тестовом сайте для разработчиков [evernote.com](https://sandbox.evernote.com/), после чего введите в терминале команду:
```
python list_notebooks.py
```
В консоли вы увидите id и название блокнота. JOURNAL_NOTEBOOK_GUID это и есть id блокнота, запишите его в файл .env.
* Создайте заметку на сайте [evernote.com](https://sandbox.evernote.com/), скопируйте ссылку на заметку и достаньте из сылки id заметки. Например в ссылке:
```
https://sandbox.evernote.com/shard/s1/nl/617325/3cc4fd7a-6d8d-42bb-b8b5-f2c60f424c98?title=%D0%9F%D0%B5%D1%80%D0%B2%D0%B0%D1%8F%20%D0%B7%D0%B0%D0%BC%D0%B5%D1%82%D0%BA%D0%B0
```
id заметки является:
```
3cc4fd7a-6d8d-42bb-b8b5-f2c60f424c98
```
id заметки это JOURNAL_TEMPLATE_NOTE_GUID, запишите его в файл .env, эта заметка будет использоваться как шаблон, для автоматической генерации заметок в скрипте add_note2journal.py (см.далее).
* INBOX_NOTEBOOK_GUID - id блокнота, заметки которого будут показаны с помощью скрипта dump_inbox.py(см.далее).

В резулятате файл .env будет выглядеть примерно так:
```
EVERNOTE_CONSUMER_KEY=user33
EVERNOTE_CONSUMER_SECRET=91127cae157ecd12
EVERNOTE_PERSONAL_TOKEN=S=s1:U=96b63:E=1896a309878:C=182127f6c88:P=81:A=evgen-33:V=2:H=7bb015c85fca63ea4a5ec338b3d2a7ab
JOURNAL_NOTEBOOK_GUID=763aa4ea-5f01-4d5a-bd4e-265dd2d1c105
JOURNAL_TEMPLATE_NOTE_GUID=ecc4091a-5e18-4ff8-b1dc-eeea2357c115
INBOX_NOTEBOOK_GUID=763aa4ea-5f08-4d3a-bd4e-268dd3d1c105
```
### Скрипты
#### list_notebooks.py
Скрипт выведет в консоль id блокнотов и их названия. Все что у вас созданы.

Для запуска введите в терминале:
```
python list_notebooks.py
```
#### dump_inbox.py
Скрипт выводит все заметки из блокнота, id которого указано в переменной INBOX_NOTEBOOK_GUID в файле .env.

Для запуска воспользуйтесь командой:
```
python dump_inbox.py <количество_заметок>
```
<количество заметок> вводить не обязательно, по умолчанию будет выбрано 10.

#### add_note2journal.py
Скрипт создает запись по шаблону JOURNAL_TEMPLATE_NOTE_GUID и сохраняет ее в блокноте, id которого указанно в JOURNAL_NOTEBOOK_GUID.

Для запуска:
```
python add_note2journal.py
```
Содержимое и заголовок шаблона копируются в новую заметку. Можно использовать 2 автоматически подставляемых значения:
* {date} - заменяется на текущую дату
* {dow} - заменяется на название текущего дня недели (по-русски с маленькой буквы)

Можно передать дату параметром при вызове скрипта в формате - YYYY-MM-DD.
```
python add_note2journal.py <YYYY-MM-DD>
```
Если параметр не передать, то будет вставлена сегодняшняя дата и день недели.
