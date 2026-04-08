import random

pwd=random.randint(0,9)

guessNum = int(input("請輸入數字(0~9):"))
while guessNum !=pwd:
    guessNum = int(input("猜錯，再猜(0~9):"))
print("猜對了，密碼就是",pwd)    