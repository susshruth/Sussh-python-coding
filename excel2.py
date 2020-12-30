import pandas as pd

df1 = pd.read_excel('example_pandas.xlsx')
df2 = pd.read_excel('example_pandas2.xlsx')
df3 = pd.read_excel('example_pandas3.xlsx')
# def f1():
def add1(num1, num2, num3):
    if num1 < 10:
        return df1['Age'][0].value("someone is under ten")
    elif num2 < 10:
        return df1['Age'][1].value("someone is under ten")
    elif num3 < 10:
        return df1['Age'][2].apply("someone is under ten")
    else:
        return num1 + num2 + num3
a = df1['expence'][0]
b = df1['expence'][1]
c = df1['expence'][2]
df1['Total'] = add1(a, b, c)

def add2(num1, num2, num3):
    return num1 + num2 + num3
d = df2['expence'][0]
e = df2['expence'][1]
f = df2['expence'][2]
df2['Total'] = add2(d, e, f)

def add3(num1, num2, num3):
    return num1 + num2 + num3
g = df3['expence'][0]
h = df3['expence'][1]
i = df3['expence'][2]
df2['Total'] = add2(g, h, i)

groups = {'Family1':df1, 'Family2':df2, 'Family3':df3}
writer = pd.ExcelWriter('Familydata.xlsx')
for sheet_name in groups.keys():
    groups[sheet_name].to_excel(writer, sheet_name=sheet_name, index=False)
writer.save()   

# ------------------------
# Comments
# ------------------------

# print(df.head())
    # print(a)
    # print(b)
    # print(c)
    # print(add(a, b, c))

# df1.to_excel(writer, 'family1')
# writer.save()
# writer2 = pd.ExcelWriter('new_book3.xlsx')
# df2.to_excel(writer2, 'family2')
# writer2.save()