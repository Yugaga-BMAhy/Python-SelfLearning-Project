a = input("請輸入一個字串:")
total = 0
for i in a:
    code= ord(i)
    print("ASCII code for '{}' is {}".format(i,code),sep="")
    total += code
print(total)    
    
