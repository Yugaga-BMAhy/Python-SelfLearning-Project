card =['0','A','2,','3','4','5','6','7','8','9','10','J','Q','K']

total=0
for i in range(1,6):
    temp=input("請輸入第"+str(i)+"個牌面:")
    total+= card.index(temp)
print("總點數為",total)    