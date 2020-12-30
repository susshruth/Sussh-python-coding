import pandas as pd

input1 = input("Find : ")

df = pd.read_excel('example_pandas.xlsx')

def add(num1, num2, num3):
    return num1 + num2 + num3
a = df['expence'][0]
b = df['expence'][1]
c = df['expence'][2]
aa = df['Name'][0]
bb = df['Age'][0]
cc = df['like color'][0]
dd = df['expence'][0]
df['Total'][0] = ""
ee = df['Total']
df['Total'] = add(a, b, c)
if(aa == input1):
    print("Susshruth")
    aa = "Susshruth"
    bb = "9"
    cc = "green"
    dd = "120"
    ee = "820"
    writer = pd.ExcelWriter('new_book3.xlsx')
    df.to_excel(writer, 'Family')
    writer.save()
else:
    print("no find results")

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
writer1 = pd.ExcelWriter('new_book4.xlsx')
df.to_excel(writer1, 'Family')
writer1.save()