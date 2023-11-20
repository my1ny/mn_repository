import pandas as pd

folder = "data/"
target = folder + "fktemp.csv"

df = pd.read_csv(target)

#비교 연산
""" print(df.name == "권시우")

print(df.company == "양문")

temp = df[df.postcode > 70000]
print(temp)

res = df[df.color == "Lavender"].head(2)
print(res)

res1 = df[df.postcode > 70000][["name", "postcode", "color"]]
print(res1)
print(res1.count())

temp1 = df.postcode.mean()
print(temp1)

temp2 = df.postcode.sum()
print(temp2)

temp3 = df[df.color == "Lavender"].postcode.mean()
print(temp3)

temp4 = df[df.color == "Lavender"].postcode.sum()
print(temp4)

temp5 = df[df.postcode > df.postcode.mean()][["name", "postcode"]]
print(temp5)

temp6 = df[df.postcode > df.postcode.mean()]
print(temp6) """

#결측 확인
""" temp = df.company.isnull()
print(temp)

temp1 = df.name.empty
print(temp1)

temp2 = df[df.company.isnull()][["name", "postcode"]]
print(temp2)

for el in temp:
    if el == True:
        print(el) """

#비트 연산_Nor
""" temp = df[(df.color == "Lavender")]
print(temp)

temp1 = df[~(df.color == "Lavender")]
print(temp1)
print(temp1.count())
print(temp1.color.count())

temp2 = df[~(df.color == "Lavender")][["name"]]
print(temp2) """

#and 연산
""" temp = df[(df.color == "Lavender") & (df.postcode > 30000)]
print(temp) """

#or 연산
""" temp = df[(df.color == "Lavender") | (df.postcode > 30000)]
print(temp)

temp1 = df[(df.color == "Lavender") | (df.postcode > 30000)][["name"]]
print(temp1) """

#정렬
""" temp = df.sort_values("postcode")
print(temp)

temp1 = df.sort_values("postcode", ascending=False)
print(temp1)

temp2 = df.sort_values("name", ascending=True)
print(temp2) """

#데이터 재배열
col = ['Machine','Country','Price','Brand']
data = [['TV','Korea',1000,'A'],
        ['TV','Japan',1300,'B'],
        ['TV','China',300,'C'],
        ['PC','Korea',2000,'A'],
        ['PC','Japan',3000,'E'],
        ['PC','China',450,'F']]
df = pd.DataFrame(data=data, columns=col)
print(df)

print("\n------------------------------\n")
print(df.pivot(index='Machine',columns='Country',values='Price'))
print("\n------------------------------\n")
print(df.pivot(index='Brand',columns='Machine',values='Price'))
print("\n------------------------------\n")
print(df.pivot(index='Country',columns='Machine',values='Price'))
print("\n------------------------------\n")
print(df.pivot(index='Price',columns='Brand',values='Machine'))