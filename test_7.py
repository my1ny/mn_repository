#삼각형 출력
#01
""" for i in range(5, 0, -1):
    print(i * "*") """
    
#02
""" for i in range(1, 6):
    print(i * "*") """

#03
""" for i in range(1, 6):
    print((6-i) * " ", end = " ")
    print((i * 2 - 1) * "*") """

#04, 03번과 연결하면 다이아몬드 모양
""" for i in range(6, 0, -1):
    print((6-i) * " ", end = " ")
    print((i * 2 - 1) * "*") """
    
#5*5 출력
#정상출력
""" num = 0
line = []
for i in range(5):
    for j in range(5):
        num += 1
        line.append(num)
    print(line)
    line = [] """

#세로출력
""" line = []
for i in range(1, 6):
    for j in range(1, 6):
        num = ((j-1) * 5) + i
        line.append(num)
    print(line)
    line = [] """
        
        
#역순출
""" num = 26
line = []
for i in range(5):
    for j in range(5):
        num -= 1
        line.append(num)
    print(line)
    line = [] """
    
#가위바위보
""" import random as rd

def computer_choice():
    choices = ["1", "2", "3"]
    return rd.choice(choices)

def determine_winner(user_choice):
    pcnum = computer_choice()
    print(user_choice, pcnum)
    
    if user_choice == pcnum:
        print("무승부")
        return
    elif ((user_choice == "1" and pcnum == "3") or (user_choice == "2" and pcnum == "1") or user_choice == "3" and pcnum == "2"):
        print("승리")
        return
    else:
        print("패배")
        return
    
print("1: 가위")
print("2: 바위")
print("3: 보")
usnum = input("1~3 숫자를 입력하세요: ")
determine_winner(usnum) """

#파일 처리
#파일 쓰기 권한, 생성
""" file = open("temp.txt", "w")
file.close() """

#파일 쓰기
""" file = open("temp.txt", "w")
file.write("hello\n")
file.write("world")
file.close() """

#01, 02
""" file = open("c:/Users/pc/OneDrive/바탕 화면/tem.txt", "w")
for i in range(100):
    file.write(f"{i}\n")
file.close() """

#03 추가 쓰기
""" file = open("c:/Users/pc/OneDrive/바탕 화면/tem.txt", "a")
file.write("hello\n")
file.write("world")
file.close() """

#파일 읽기
""" file = open("temp.txt", "r")
res = file.read()
print(res)
file.close() """

""" file = open("c:/Users/pc/OneDrive/바탕 화면/tem.txt", "r")
res = file.read()
print(res)
file.close() """

#한라인씩
""" file = open("c:/Users/pc/OneDrive/바탕 화면/tem.txt", "r")
res = file.readline()
print(res)
file.close() """

""" file = open("c:/Users/pc/OneDrive/바탕 화면/tem.txt", "r")
for i in range(110):
    res = file.readline()
    print(res)
file.close() """

#readlines
""" file = open("c:/Users/pc/OneDrive/바탕 화면/tem.txt", "r")
res = file.readlines()
print(res)
file.close() """

""" file = open("c:/Users/pc/OneDrive/바탕 화면/tem.txt", "r")
line = file.readlines()
for l in line:
    print(l)
file.close() """

#file object
""" file = open("c:/Users/pc/OneDrive/바탕 화면/tem.txt", "r")
for l in file:
    print(l)
file.close() """

