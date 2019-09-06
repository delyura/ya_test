# Напишите на Python программу, которая:

# разобьет информацию в CSV-файле на две ключевые колонки;
# отфильтрует все строки, где значение в столбце N не является логином пользователя.
# Требования к логину пользователя:
# состоит только из строчных букв, цифр и символа «-»;
# начинается с буквы;
# не заканчивается на символ «-»;
# имеет длину от 3 до 15 символов.

import pandas as pd

book_df = pd.read_csv("book.csv", sep=";")
book_df = pd.concat([i for _, i in book_df.iteritems()]).reset_index(drop=True)
middle = int(len(book_df.index) / 2)
column_1 = pd.Series(book_df[:middle]).reset_index(drop=True)
column_2 = pd.Series(book_df[middle:]).reset_index(drop=True)
result_df = pd.DataFrame({'col1': column_1,
                          'col2': column_2})
print(result_df)

result_df = result_df.replace(to_replace=r'(?!^(?=.{3,15})[a-z][a-z0-9]*[-]*[a-z0-9])^.+$', value='', regex=True)
print(result_df)
