""" x = [1, 2, 3]
y = [1, 2, 3]
z = x

print(x is y)
print(x is z)
print(x is not y) """

""" a = 5
b = 5
print(a is b)
print(a is not b) """

""" a = 3
b = 3.0
print(a == b)
print(a is b)
print(a is not b) """

""" a = [3, 5, 1]
b = a
print(a is b)

a[0] = 2
print(a, b)
print(a is b) """

""" x = 2 ** 3 ** 2
print(x) """

""" print(2 + 3 * 4)
print(10 / 5 / 2)
print(2 ** (3 ** 2))
print(10 % 3 % 2)
print(1 + 2 > 3 and 4 - 1 < 2)
print(not False and True)
print(not True or False and True)
print(1 & 2 | 3 ^ 4)
print(5 in [3, 4, 5] or 2 not in [1, 2, 3])
print(2 * -3 // 2)
print(1 == 2 != 3) """



""" x = 0

if x > 0:   
    print("x is positive")
elif x < 0:
    print("x is negative")
else:
    print("x is zero") """

""" x = 4
if x % 2 == 0:
    print("x is even")
else:
    print("x is odd") """
    
""" a = 1
b = 2
if a == b:
    print("a is b")
else:
    print("a is not b") """

""" x = "b"
if x == "a":
    print("x is a")
elif x == "b":
    print("x is b")
else:
    print("x is not a or b") """

""" fruits = ["apple", "banana", "cherry"]

for fruit in fruits:
    print(fruit) """

""" my_list = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

for row in my_list:
    for num in row:
        print(num) """

for i in range(10):
    print(i)

""" for char in "Python":
    print(char) """

""" fruits = ["apple", "banana", "cherry"]
for fruit in reversed(fruits):
    print(fruit)
for fruit in sorted(fruits, reverse=True):
    print(fruit) """
    
""" for x in range(2,10):
    for y in range(1,10):
        print(x, "*", y, "=", x*y) """

""" rang = [5, 8, 3, 1, 6]
for i in rang:
    print("element :", i)
else:
    print("end process") """
    
""" for i in range(10):
    if i == 7:
        break
    elif i == 1:
        continue
    else:
        pass
    print(i) """

""" i = 1
while i <= 5:
    print(i)
    i += 1 """

""" x = 0
while x <= 9:
    print(x)
    x += 1 """

""" str_word = "python"
i = 0
while i < len(str_word):
    print(str_word[i])
    i += 1 """
    
""" sum = 0
i = 1
while i <= 10:
    sum += i
    i += 1
print(sum) """

""" x = 1
while x <= 100:
    if x % 2 == 0:
        print("x is even", x)
    else:
        print("x is odd", x)
    x += 1 """

""" x = 1
while x <= 100:
    if x % 7 == 0:
        print(x)
    x += 1 """
 