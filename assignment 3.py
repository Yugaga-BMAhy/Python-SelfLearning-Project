def primeTest(n):
    if n<= 1:
        return"非質數"
    for i in range(2,n):
        if n % i ==0:
            return "非質數"
    return "質數"
while True:
    num = int(input("請輸入整數:"))
    if num == -9999:
        break
    else:
        result = primeTest(num)
        print(num,"為",result)