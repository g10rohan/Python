#Python program to Multiply all numbers in the list
mylist=[]
mylist1=[10,20]
n=int(input("Enter number of element you want to insert:-"))
for i in range(0,n):
    mylist.append(int(input("enter value:")));

mylist1=list(map(lambda x,y:x*y,mylist,mylist1));
print(mylist1);
