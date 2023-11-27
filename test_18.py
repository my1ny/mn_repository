import pandas as pd

target = "./data/apt.csv"
df = pd.read_csv(target, encoding="CP949")
df.to_csv("./data/apttt.csv", encoding="utf8")
#print(df.head())

df = pd.read_csv("./data/apttt.csv", index_col=0)
df = df.rename(columns={"분양가격(제곱미터)":"분양가"})
df["분양가"] = df["분양가"].convert_dtypes()
#print(df.head())

#정렬
""" #res = df.sort_values(by="지역명")
res = df.sort_values("지역명")
print(res.head(5))
print("\n-----------------------------\n")

#res1 = df.sort_values("지역명", ascending=True)
res1 = df.sort_values("지역명", ascending=False)
print(res1.head(10))
print("\n-----------------------------\n")

#res2 = df.sort_values(by="연도")
#res2 = df.sort_values(by="분양가")
res2 = df.sort_values(by="연도")[10:20]
print(res2)
print("\n-----------------------------\n")
print(res2.head()) """

#컬럼 이름 출력
""" #res = df[["지역명", "연도"]]
#res = df[["지역명", "연도", "분양가"]]
res = df[["지역명", "연도", "분양가"]][:7]
print(res) """

""" #res = df.loc[:, ["지역명", "연도", "분양가"]][:5]
#res = df.loc[:][:5]
res = df.loc[:][:]
print(res) """

""" res = df.iloc[1]
print(res) """

""" #res = df.loc[:6, ["지역명", "연도"]]
#res = df.loc[:6, ["지역명", "연도"]][3:]
res = df.loc[6:, ["지역명", "연도"]][:7]
print(res) """

#필터 출력
""" #res = df.loc[df["지역명"]=="강원"]
#res = df.loc[df["연도"] > 2020]
#res = df.loc[df["지역명"]=="서울", ["지역명", "연도", "분양가"]]
#res = df.loc[df["지역명"]=="서울", ["지역명", "연도", "분양가"]][:10]
res = df.loc[df["지역명"]=="서울", ["지역명", "연도", "분양가"]][-10:]
print(res) """

#인덱스 지정 선택
df0 = df.copy()
#print(df0)

""" #res = df.iloc[2]
res = df.iloc[2][3]
print(res) """

#인덱스 필터
""" res = df[df.index > 3560]
print(res) """

#필터
""" #res = df[df.연도 == 2023]
res = df[df.월 == 3]
print(res) """

#비트 연산 필터
""" res = df[(df.연도 == 2023) & (df.지역명 == "서울")]
#res = df[(df.연도 == 2023) & (df.지역명 == "서울") & (df.월 == 6)]
print(res) """

#컬럼 추가
""" columns=list(df.columns)
print(columns) """

#df1 = df.reindex(index=df.index[:7], columns=list(df.columns) + ["extra"])
df1 = df.reindex(columns=list(df.columns) + ["extra"])
""" print(df)
print("\n-----------------------------\n")
print(df1) """

#NaN 행 제거
#df1.loc[:6, "extra"] = "0"
df1.loc[:4, "extra"] = False
#print(df1)

#복사
df2 = df1.copy()

#NaN 제거
""" #res = df2.dropna(how="any")
res = df2.fillna(value="123", inplace=True)
print(df2)
print("\n-----------------------------\n")

res = df2.dropna(how="any", inplace=True)
print(res)
print("\n-----------------------------\n")

print(df2) """

#NaN 데이터 출력
""" #res = pd.isna(df1)
#res = pd.isna(df0)
res = pd.isna(df2)
print(res) """

#데이터 종류별 출력
""" #res = df["연도"].value_counts()
#res = df["지역명"].value_counts()
#res = df["월"].value_counts()
res = df.월.value_counts()
print(res) """

#그룹핑
""" #res = df.groupby(["지역명", "연도", "월"]).sum()
res = df.groupby(["지역명", "연도", "월"]).all()
print(res) """

res = df.groupby(["지역명", "연도", "월"])["분양가"].agg("sum")
print(res)

