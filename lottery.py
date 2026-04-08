import random
lottoList = list()
for i in range(7):
    temp =random.randint(1,49)
#避免重複
    while temp in lottoList: 
        temp = random.randint(1,49)
    lottoList.append(temp)
#print(lottoList)
special =lottoList.pop()
print("樂透中獎號碼:",sorted(lottoList))
print("特別獎:",special)    
