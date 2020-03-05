#12.	Python program to find smallest number in a list
mylist=[]
n=int(input("Enter number of element you want to insert:-"))
for i in range(0,n):
    mylist.append(int(input("enter value:")));
mylist.sort();
print(mylist[0])