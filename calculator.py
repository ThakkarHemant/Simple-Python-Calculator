import math

def add():
    print("the sum of the numbers is",sum(z))

def subtract():
    diff=z[0]        #[1,2,3,4,5], diff=1 
    for n in range(1,len(z)): 
        diff=diff-z[n]       
    print("the difference of the numbers is",diff)

def multi():
    prod=1
    for j in range(len(z)):
        prod=prod*z[j]
    print("the product of the numbers is",prod)

def divide():
    print("which numbers you want to divide?")
    print(z)
    d1=int(input("enter the number here :"))
    d2=int(input("enter the number here :"))
    print(d1/d2,"is the quotient")
    print(d1%d2,"is the remainder")

def power():
    print("tell the number you want to square /cube :")
    d3=int(input()) 
    print("the sqaure of",d3,"is",math.pow(d3,2),"and the cube is",math.pow(d3,3))   


def sqroot():
    print("tell the number you want to square /cube root :")
    d4=int(input())
    print("the sqaure root of",d4,"is",(math.sqrt(d4)),"and the cube root is :",(d4)**1/3)

def factorial():
    print("Enter the number you want factorial of : ")
    d5=int(input())
    fact=1
    for i in range(1,d5+1):
        fact*=i
    print("The factorial of :",d5,"is",fact)

while True:
    print("\n 1.ADD \n 2.SUBTRACT \n 3.MULTIPLY\n 4.DIVIDE \n 5.POWER FUNCTION \n 6.ROOT FUCNTION \n 7.FACTORIAL \n 8.Restart \n 9.End")
    ch=int(input("what do you want to perform on these numbers ?"))
    if ch==1:
        add()
    elif ch==2:
        subtract()
    elif ch==3:
        multi()
    elif ch==4:
        divide()
    elif ch==5:
        power()
    elif ch==6:
        sqroot()
    elif ch==7:
        factorial()
    elif ch==9:
        break
    f=input("do you want more ?(Y/N)")
    if f=="Y" or "y":
        True
    elif f=="N" or "n":
        break
    


        
        





    



