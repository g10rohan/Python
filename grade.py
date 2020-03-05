# #19.	Write a C program to input marks of five subjects Physics, Chemistry, Biology, Mathematics and Computer. Calculate percentage and grade according to following:
# Percentage >= 90% : Grade A
# Percentage >= 80% : Grade B
# Percentage >= 70% : Grade C
# Percentage >= 60% : Grade D
# Percentage >= 40% : Grade E
# Percentage < 40% : Grade F
p=int(input("Enter Marks of Physics:-"))
c=int(input("Enter Marks of Chemistry:-"))
b=int(input("Enter Marks of Biology:-"))
m=int(input("Enter Marks of Mathematics:-"))
comp=int(input("Enter Marks of  Computer:-"))
per=(p+c+b+m+comp)*100/500
if per>=90:
    print("Grade A with",per,"%");
elif per>=80:
    print("Grade B with",per,"%");
elif per>=70:
    print("Grade C with",per,"%");
elif per>=60:
    print("Grade D with",per,"%");
elif per>=40:
    print("Grade E with",per,"%");
elif per<40:
    print("Grade F with",per,"%");
