# Write a Python program to remove duplicates from a list.
mylist=[]
mylist1=[]
n=int(input("Enter number of element you want to insert:-"))
for i in range(0,n):
    mylist.append(int(input("enter value:")));
for i in mylist:
    if i not in mylist1:
        mylist1.append(i);
print(mylist1)