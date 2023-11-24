import pandas as pd

""" folder = "data/"
target = folder + "fktemp.csv"

df = pd.read_csv(target) """

#순위 매기기
""" df["aver"] = df.postcode.rank(method="average")
print(df[["postcode", "aver"]])

df["dense"] = df.postcode.rank(method="dense")
print(df[["postcode", "dense"]])

df["first"] = df.postcode.rank(method="first")
print(df[["postcode", "first"]])

df["min"] = df.postcode.rank(method="min")
print(df[["postcode", "min"]])

#df["max"] = df.postcode.rank(method="max", ascending=False)
df["max"] = df.postcode.rank(method="max")
print(df[["postcode", "max"]])

print(df[["postcode", "max", "min", "first" , "dense", "aver"]]) """

#전치 컬럼-로우 변환
""" print(df.transpose()) """

#누적 계산
""" #print(df["postcode"].expanding().sum())
print(df["postcode"].expanding()) """

#내림차순 기준
""" print(df.postcode.idxmax(axis=0))
print(df.postcode.idxmin(axis=0)) """

#empty 추가
""" print(df.empty)
print(df.company.empty) """

#검색
""" print(df.isin([33521]))
print(df.isin(["김예은"]))

print(df.isin([89361, 65421]))

print(df.isin([89361, 65421, "이준호"])) """

#기간 계산
""" period = pd.period_range(start="2023-11-10 00:00:00", end="2023-11-10 02:30:00", freq="30T")
dt = {"col1":[1,2,3,4,5,6],"col2":period}
idx = ["row1","row2","row3","row4","row5","row6"]
pf = pd.DataFrame(data=dt, index=idx)
print(pf) """

#인덱스 시간 - 간격 생성
""" #i = pd.date_range("2023-11-10", periods=10, freq="1H")
i = pd.date_range("2023-11-10", periods=10, freq="3H")
df = pd.DataFrame({"col1":[1,2,3,4,5,6,7,8,9,10]}, index=i)
print(df)
print("\n-----------------------\n") """

#특정 시간 찾기
""" print(df.at_time("09:00"))
print(df.at_time("03:00"))
print("\n-----------------------\n") """

#범위 찾기
""" print(df.between_time(start_time="12:00", end_time="00:00"))
print(df.between_time(start_time="03:00", end_time="09:00")) """

#x일 간격 생성 - 기간별 찾기
""" i = pd.date_range("2023-11-10", periods=10, freq="3D")
#i = pd.date_range("2023-11-10", periods=10, freq="5D")
df = pd.DataFrame({'col1':[1,2,3,4,5,6,7,8,9,10]}, index=i)
print(df)

print(df.first("5D"))
#print(df.last("3D")) """

#코스피 지수
import FinanceDataReader as fdr

ksp = fdr.DataReader("KS11", "2001")
#print(ksp)
print("\n-----------------------\n")

#최고가 확인
""" res = ksp["High"].max()
print(res)

res1 = ksp["High"].idxmax()
print(res1) """

#최저가 확인
""" res = ksp["Low"].min()
print(res)

res1 = ksp["Low"].idxmin()
print(res1) """

#최고가 값 찾기
""" res = ksp["Volume"].nlargest(n=5)
res = ksp["Volume"].nlargest(n=10)
print(res) """

#최저가 값 찾기
""" #res = ksp["Volume"].nsmallest(n=5)
#res = ksp["Close"].nsmallest(n=5)
res = ksp["Close"].nlargest(n=5)
print(res) """

#kospi 3000 최초
""" #cond = ksp["Close"] >= 3000
cond = ksp["Close"] >= 2000
res = ksp[cond].index[0]
print(res) """

#위 값 참조 처리
""" res = ksp["Volume"] > ksp["Volume"].shift()
print(res) """

""" ksp["up"] = ksp["Volume"] > ksp["Volume"].shift()
#print(ksp) """

""" res = ksp["up"] != ksp["up"].shift().cumsum()
print(res) """

""" ksp["grp"] = (ksp["up"] != ksp["up"].shift()).cumsum()
#print(ksp) """

#연속 증가값 확인
""" ksp["up_cnt"] = ksp["grp"].groupby(ksp["grp"].values).cumcount() + 1
#print(ksp)
 """
#연속 상승값 확인
""" print(ksp["up_cnt"].max()) """

#부동산 정보 처리
#변환
""" target = "./data/apt.csv"
df = pd.read_csv(target, encoding="CP949")
df.to_csv("./data/conv_apt.csv", encoding="utf8")
print(df.head()) """

df = pd.read_csv("./data/conv_apt.csv", index_col=0)
#print(df.head())

#컬럼명 변경
df = df.rename(columns={"분양가격(제곱미터)":"분양가"})
#print(df)

#컬럼 타입 변경
#print(df.dtypes)
df["분양가"] = df["분양가"].convert_dtypes()
#print(df.dtypes)

#array 변환
""" arr = df.to_numpy()
print(arr)
print(arr[2])
print(len(arr)) """

#요약 정보
""" print(df.describe()) """

#축 변환
print(df.transpose())
print("\n-----------------------\n")
print(df.T.head())




