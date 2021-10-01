import numpy as np
Array = []
Loop = int(input("Enter your loop: "))
while (Loop%2 !=0):
    print("Please Enter Again")
    Loop = int(input("Enter Your Loop: "))
print("Enter your array: ")
for i in range(Loop) :
    Array += [int(input(""))]
NewArray = np.asarray(Array)
NewArrayNumpy = NewArray.reshape(int(Loop/2),2)
print(NewArrayNumpy) 