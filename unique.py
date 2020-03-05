# . Write a Python function that takes a list and returns a new list with unique elements of the first list.
# Sample List : [1,2,3,3,3,3,4,5]
# Unique List : [1, 2, 3, 4, 5]
def unique(mylist1):
    unilist=[];
    for i in mylist1:
            if i not in unilist:
                unilist.append(i);
    print(unilist);


mylist=[1,2,3,3,3,3,3,4,5];
unique(mylist);