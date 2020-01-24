a=input("input any string")
d=0
l=0
for i in a:
    if i.isdigit():
        d=d+1

    elif i.isalpha():
        l=l+1
    else:
        pass
    
print(" number if letter and digits are",d)
print("leter ",l)