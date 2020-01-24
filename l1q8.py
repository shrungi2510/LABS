import random

a=random.randrange(10)

for x in range(0,10):
    b=int(input())

    if (a==b) :
        print("you are right")
        break
    elif (a<b):
        print("high")
    else:
        print("low")
 
print(a)