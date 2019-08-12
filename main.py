from random import randint
a = randint (0,100)
b = randint (0,100)
res = float(a/b)
print("number one:",a)
print("number two:",b)
c = res % 0.01
d = res - c
print(d)
print("divide!!!!")
ans = float(input())
if (ans == d):
    print("correct")
else: 
    print("wrong")
    