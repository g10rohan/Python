#1.	Python program to interchange first and last elements in a list
mylist=[1,2,3,4,5,6];
print(mylist);
temp=mylist[0];
mylist[0]=mylist[-1];
mylist[-1]=temp;
print(mylist);