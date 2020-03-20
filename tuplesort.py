# Write a Python program to get a list, sorted in increasing order by the last element in each tuple from a given list of non-empty tuples.
# Sample List : [(2, 5), (1, 2), (4, 4), (2, 3), (2, 1)]
# Expected Result : [(2, 1), (1, 2), (2, 3), (4, 4), (2, 5)]
mylist=[(2, 5), (1, 2), (4, 4), (2, 3), (2, 1)];
for i in range(0,len(mylist)):
    for j in range(i+1,len(mylist)):
            if mylist[i][1]>mylist[j][1]:
                temp=mylist[i];
                mylist[i]=mylist[j]
                mylist[j]=temp;
print(mylist)