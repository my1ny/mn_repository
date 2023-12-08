#가톨릭 대학교 수시(교과 전형)
#학과/합격자 평균 성적 그래프
#지원자 성적 입력 > 

import pandas as pd
import matplotlib.pyplot as plt

#파일 불러오기
target = "data/cauv.csv"
df = pd.read_csv(target, encoding="CP949")
df.to_csv("data/cauv_cp.csv", encoding="utf8")
#print(df.head())

df = pd.read_csv("data/cauv_cp.csv", index_col=0)
#print(df.head())
print(df)

#합격 예상 함수 만들기
def rate_check():
    