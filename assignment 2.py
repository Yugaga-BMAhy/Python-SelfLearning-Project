def root(x,y):
    return x**(1/y)

a= int(input("請輸入被開方數字:"))
b=int(input("請輸入開方數字:"))
result= root(a,b)
print(a,"開",b,"次方為",result)