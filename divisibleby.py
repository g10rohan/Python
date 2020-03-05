#4.	Write a C program to check whether a number is divisible by 5 and 11 or not.
a=int(input("Enter Any Number :-"))
if a%5==0 and a%11==0:
    print(a,"is Divisible by 5 and 11")
else:
    print(a,"is Not Divisible by 5 and 11");