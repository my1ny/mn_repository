import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
plt.rcParams['font.family'] = 'NanumGothic'

target = "cauv.csv"
df = pd.read_csv(target, encoding="cp949")
df.to_csv("data/cauv1.csv", encoding = "utf8")
print(df.head())

df = pd.read_csv("data/cauv1.csv", index_col=0)
print(df.head())

# 1. 합격 예상 학과 나열
def rate_check(x):
    print("적정 수준 학과입니다.")
    #x와 최종 합격자의 평균 등급이 +-0.1 차이가 나는 학과만 가져오기
    print(df[(df["평균(최종)"] - 0.1 < x) & (df["평균(최종)"] + 0.1 > x)][["모집단위", "최고(최종)", "평균(최종)", "최저(최종)"]])

print("당신의 내신 등급을 입력해 주세요.")
res = input("내신 등급: ") 

rate_check(float(res)) 

# 2. 특정 학과 합격 가능성 
def dept_pass(x,y):
    #선택한 학과 정보 불러오기
    print(df[df["모집단위"]==x][["모집단위", "최고(최종)", "평균(최종)", "최저(최종)"]])

    #내신점수와 +-0.1 차이로 상향, 하향, 적정 구분
    if y > df[df["모집단위"]==x]["평균(최종)"].values[0] + 0.1:
        print("상향 지원 학과 입니다.")
    elif y > df[df["모집단위"]==x]["평균(최종)"].values[0] - 0.1:
        print("하향 지원 학과 입니다.")
    else:
        y > df[df["모집단위"]==x]["평균(최종)"].values[0] - 0.1
        
print("지원하고 싶은 학과 명을 입력해 주세요")
res1 = input("학과 명: ")

print("당신의 내신 등급을 입력해 주세요")
res2 = input("내신 등급: ")

dept_pass(res1, float(res2))

# 예시 데이터 생성
data = {
    '모집단위': ['국어국문학과', '철학과', '국사학과', '영어영문학부'],
    '최고(최종)': [2.79, 2.85, 2.67, 2.76],
    '평균(최종)': [2.94, 3.14, 2.83, 2.91],
    '최저(최종)': [3.14, 3.27, 3.03, 3.02]
}

df = pd.DataFrame(data)

# 3. 최종등록자 기준 최고등급, 평균등급, 최저등급 사이 나의 위치 '그래프' 출력
def dept_pass(x, y):
    # 선택한 학과 정보 불러오기
    department_scores = df[df["모집단위"] == x]["평균(최종)"]
    highest_score = df[df["모집단위"] == x]["최고(최종)"].values[0]
    lowest_score = df[df["모집단위"] == x]["최저(최종)"].values[0]

    # 그래프 그리기
    plt.figure(figsize=(8, 6))
    plt.plot(department_scores, marker='o', linestyle='-')

    # 사용자 점수 표시
    plt.scatter(0, y, color='red', label='Your Score')

    # 최고점수와 최저점수 표시
    plt.scatter(0, highest_score, color='green', label='Highest Score')
    plt.scatter(0, lowest_score, color='orange', label='Lowest Score')

    plt.xlabel('학과')
    plt.ylabel('점수')
    plt.title(f'{x} 학과 내신 등급 분포')
    plt.legend()
    plt.show()

print("지원하고 싶은 학과 명을 입력해 주세요")
res1 = input("학과 명: ")

print("당신의 내신 등급을 입력해 주세요")
res2 = input("내신 등급: ")

dept_pass(res1, float(res2)) 



