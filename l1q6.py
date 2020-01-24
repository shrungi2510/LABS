def handle(x,y):
    try:
        r=x/y
        print("this is possible",r)
    except ZeroDivisionError:
        print("this is not possible")


t=int(input())
b=int(input())
handle(t,b)