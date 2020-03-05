# 3.	Write a C program to check whether a number is negative, positive or zero.
a=int(input("Enter Any Number :-"))
if a < 0:
    print(a," is Negative.")
elif a > 0:
    print(a, " is Positive.")
else:
    print(a, " is Zero.")