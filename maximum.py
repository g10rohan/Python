#2.	Write a C program to find maximum between three numbers.
a=int(input("Enter Any Number :-"))
b=int(input("Enter Any Number :-"))
c=int(input("Enter Any Number :-"))
if a>b and a>c:
    print(a,"is the greatest number.")
elif b>a and b>c :
    print(b,"is the greatest number.")
elif c>a and c>b:
    print(c,"is the greatest number.")