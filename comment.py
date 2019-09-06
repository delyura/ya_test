# Выгрузите из API, доступного по ссылке, все комментарии, в которых:
# значение в поле email заканчивается на .info;
# количество слов в поле name меньше 4.
# Создайте файл в формате CSV, в котором распределите информацию из комментариев на две колонки следующим образом:
# email — значения поля email;
# words_count — количество слов из поля name

import json
import pandas as pd
import re
import requests

url = "https://jsonplaceholder.typicode.com/comments"
r = requests.get(url)

parsed_string = json.loads(r.text)
pattern = r'(^|\w)[\w.-]+@[\w]+\.info(\s|$)'
email = []
words_count = []
for obj in parsed_string:
    if re.search(pattern, obj['email']):
        if len(re.findall(r'\w+', obj['name']))<4:
            email.append(obj['email'])
            words_count.append(len(re.findall(r'\w+', obj['name'])))

df = pd.DataFrame({'email': email,
                   'words_count': words_count})
df.to_csv('comment.csv')
print(df)
