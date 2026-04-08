setA = set(input("輸入A的興趣(空白分隔): ").split())
setB = set(input("輸入B的興趣(空白分隔): ").split())

print("A與B所有的興趣:", sorted(setA|setB))
print("A與B共同的興趣:", sorted(setA&setB))
print("A與B彼此沒有的興趣:", sorted(setA^setB))
print("A有但B沒有的興趣:", sorted(setA-setB))
