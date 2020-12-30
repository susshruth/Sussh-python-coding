import pandas as pd
from openpyxl import Workbook

df = pd.read_excel('example_pandas.xlsx')
print(df.head())

writer = pd.ExcelWriter('new_book.xlsx')
df.to_excel(writer, 'new_sheet')
writer.save()