for i in range(0, 10):
    for j in range(0, i + 1):
        print("*", end="")
    print("\r")
for i in range(5):
    for j in range(i):
        print(i,end="")
    print("\n")
    

b=0
for i in range(5,0,-1):
    b+=1
    for j in range(1,i+1):
        print(b,end="")
    print("\r")

for i in range(5,0,-1):
    for j in range(0,i):
         print(10,end="")
    print("\r")
