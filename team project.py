#가톨릭 대학교 수시(교과 전형)
#학과/합격자 평균 성적 그래프
#지원자 성적 입력 > 적정 등급 학과 나열
#원하는 학과 입력 > 상향, 적정, 하향 중 어느 쪽인지 계산

import pandas as pd
import matplotlib.pyplot as plt

#파일 불러오기
target = "data/cauv.csv"
df = pd.read_csv(target, encoding="CP949")
df.to_csv("data/cauv1.csv", encoding="utf8")
#print(df.head())

df = pd.read_csv("data/cauv1.csv", index_col=0)
#print(df.head())
#print(df)

#합격 예상 학과 나열
def rate_check(x):
    print("적정 수준 학과입니다.")
    #x와 최종 합격자의 평균 등급이 +-0.1 차이가 나는 학과만 가져오기
    print(df[(df["평균(최종)"] - 0.1 < x) & (df["평균(최종)"] + 0.1 > x)][["모집단위", "최고(최종)", "평균(최종)", "최저(최종)"]])

print("당신의 내신 등급을 입력해 주세요.")
res = input("내신 등급: ")

rate_check(float(res))

#특정 학과 합격 가능성
def dept_pass(x, y):
    #선택한 학과 정보 불러오기
    print(df[df["모집단위"]==x][["모집단위", "최고(최종)", "평균(최종)", "최저(최종)"]])
    
    #내신점수와 +-0.1 차이로 상향, 하향, 적정 구분
    if y > df[df["모집단위"]==x]["평균(최종)"].values[0] + 0.1:
        print("상향 지원 학과입니다.")
    elif y < df[df["모집단위"]==x]["평균(최종)"].values[0] - 0.1:
        print("하향 지원 학과입니다.")
    else:
        print("적정 지원 학과입니다.")

print("지원하고 싶은 학과 명을 입력해 주세요.")
res1 = input("학과 명: ")

print("당신의 내신 등급을 입력해 주세요.")
res2 = input("내신 등급: ")

dept_pass(res1, float(res2))