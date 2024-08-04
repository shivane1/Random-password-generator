#random password generator
import random
import string

val=random.choice("shivane") #random char
print(val)

password=""
n=input("enter the size of password")
x=bool(input("do you want letters in your password?"))
x1=int(input("enter length of letters"))
if(x==True):
    for i in range(0,x1):
        password+=(random.choice(string.ascii_letters))
        
y=bool(input("do you want punchuation in your password?"))
y1=int(input("enter length of punchuation"))
if(y==True):
    for i in range(0,y1):
        password+=(random.choice(string.punctuation))    
        
z=bool(input("do you want digits in your password?"))
z1=int(input("enter length of digit"))
if(z==True):
    for i in range(0,z1):
        password+=(random.choice(string.digits))       
                    
if(x1+y1+z1!=n):
    print("Your password length is ",x1+y1+z1,"not",n)    
print("your random password is",password)
