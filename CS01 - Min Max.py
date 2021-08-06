Num = int(input("Enter your loop: "))
Num2 = []
print("Enter your data: ")
for i in range(Num):
    data = int(input(""))
    Num2 += [data]
print(Num2,end=" ")
Num2.sort()
print("--->",end="")
print(Num2)
print("Min",Num2[0])
print("Max",Num2[-1])