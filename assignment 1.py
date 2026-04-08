a=int(input("請輸入初始值:"))
b=int(input("請輸入結束值:"))

count=0
total=0

for i in range(a,b+1):
    if i%7==0 or i%11==0:
        print(f"{i:<4d}", end="")
        count+=1
        total+=i
        if count %10 ==0:
            print()
print()
print("總數共有",count,"個")        
print("數字總合為",total)
