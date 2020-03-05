#17.	Write a C program to find all roots of a quadratic equation.(a=1 b=5 c=6) answer:- -2.0 ,-3.0
import math
a=int(input("Enter value of a"));
b=int(input("Enter value of b"));
c=int(input("Enter value of c"));
q=b**2-4*a*c;
q=math.sqrt(q)
q=-b+q
q=q//2*a;
f=b**2-4*a*c;
q=-b-q
f=math.sqrt(f)
f=q//2*a;
print("Root are:-",q,f,sep=',');