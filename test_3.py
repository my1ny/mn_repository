#input
""" num = input("숫자를 입력하세요")
print("number", int(num)) """

#type
""" a = 12
print(type(a))
a = 12.01
print(type(a))
a = "a"
print(type(a))
a = "abcd"
print(type(a))
a = [1, 2, 3]
print(type(a)) """

#형변환
""" a = 65
a = "65"
print(int(a))
print(str(a))
print(hex(a))
print(oct(a))
print(chr(a))
print(ord("A")) """

""" print(pow(2, 2))
print(pow(2, 6))
print(pow(3, 4))
print(3 ** 4) """

#print(divmod(10, 3))

#print(round(3.14))
#print(round(3.78))

""" a = (3, 5, 7)
b = list(a)
c = tuple(b)
print(b)
print(c)
print(type(b))
print(type(c)) """

#range
""" for i in range(2, 7):
    print(i) """
""" for i in range(6):
    print(i) """
for i in range(1, 20, 3):
    print(i)
    
#max, min, sum
""" a = [3, 4, 5, 9]
print(max(a))
print(min(a))
print(sum(a)) """

#abs
""" print(abs(-3))
print(abs(3.0))
print(abs(-3.0)) """

#sorted
""" a = [5, 3, 1, 9, 4]
print(sorted(a))
print(sorted(a, reverse=True)) """

#enumerate
""" a = [5, 3.14, False, 9, "string"]
print(enumerate(a))
print(*enumerate(a)) """

#zip
""" a = [1, 2, 3]
b = [4, 5, 6]
print(zip(a, b))
print(*zip(a, b)) """

#any, all
""" a = [True, True, False]
b = [True, True, True]
print(any(a))
print(all(a))
print(all(b)) """

#format
""" a = 20
b = 23
c = "a 는 {}, b 는 {}, {}".format(a, b, "python")
print(c) """

#a = 3
""" print(globals())
print(locals()) """
#print(dir(a)
#print(callable(a))

#lambda
""" add = lambda a, b : a + b
sub = lambda a, b : a - b
mul = lambda a, b : a * b
div = lambda a, b : a / b
print(add(2, 3))
print(sub(2, 3))
print(mul(2, 3))
print(div(2, 3)) """

#사용자 정의
""" def add_number(x, y):
    return x + y
result = add_number(4, 5)
print(result) """

""" def greet(name):
    print("Hello, " + name + ". How are you?")
greet("python") """

""" def add(a, b):
    print(a + b)
def sub(a, b):
    return a - b
def mul():
    return 2 * 4
def div():
    print(4 / 2)
add(3, 5)
print(sub(3, 5))
print(mul())
div() """

#1
""" def is_even(x):
    if x % 2 == 0:
        print("짝수")
    else:
        print("홀수")
num = input("숫자를 입력하세요: ")
is_even(int(num)) """

#2
""" def reverse_string(msg):
    return msg[::-1]
in_str = input("문자열: ")
print(reverse_string(in_str)) """

#3
""" def add(a, b):
    return int(a) + int(b)
def sub(a, b):
    return int(a) - int(b)
def mul(a, b):
    return int(a) * int(b)
def div(a, b):
    return int(a) / int(b)
a = input("a 를 입력하세요")
b = input("b 를 입력하세요")
print("더하기: ", add(a, b))
print("뺴기: ", sub(a, b))
print("곱하기: ", mul(a, b))
print("나누기: ", div(a, b)) """

""" def calc(a, b):
    print(int(a) + int(b))
    print(int(a) - int(b))
    print(int(a) * int(b))
    print(int(a) / int(b))
a = input("a 를 입력하세요")
b = input("b 를 입력하세요")
calc(a, b) """

""" def sum_num(num):
    return sum(num)
nums = []

for i in range(1, 6):
    innum = int(input(f"{i} 번째 숫자 입력: "))
    nums.append(innum)
print(sum_num(nums)) """
