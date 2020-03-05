#9.	Python program to Count occurrences of an element in a list
mylist=list(input("Enter any word:-"));
print("You Entered:-",mylist);
oc=input("Enter the letter you want occurence of:-")
c= mylist.count(oc);
print(oc,"occured",c,"Times")