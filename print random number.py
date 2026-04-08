import random

while True:
    num = random.randint(1,20)
    if num == 11:
        break
    if num%5 ==0:
        continue
    print(num)
print("亂數到11，結束")    