#10.	Python program to find sum of elements in list
mylist=[]
n=int(input("Enter number of element you want to insert:-"))
for i in range(0,n):
    mylist.append(int(input("enter value:")));
print("Sum is :- ",sum(mylist));