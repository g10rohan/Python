#5.	Python | Ways to check if element exists in list
mylist=list(input("Enter any word:-"));
ele=input("Enter element you want to checkl:-")
if ele in mylist:
    print("The given element",ele,"found",mylist.count(ele), "Times in list");
else:
    print("No similar Element found!!!!1");