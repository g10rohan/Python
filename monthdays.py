#12.	Write a C program to input month number and print number of days in that month.
a=int(input("Enter Number between 1-12:-"))

if a<=12 and a>0:
    if a<=7 and a>0:
        if a==2:
            print("The days might be 28 or 29 as per leap year");
        elif(a%2!=0):
            print("31 Days");
        else:
            print("30 Days")
    elif a>7 and a<=12:
        if a%2==0:
            print("31 Days");
        else:
            print("30 Days")
else:
    print("Invalid Number");