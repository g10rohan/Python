# 3.	Python program to remove Nth occurrence of the given word
mylist=list(input("Enter any word:-"));
print("You Entered:-",mylist);
oc=input("Enter the letter you want to remove")
c= mylist.count(oc);
for i in range(0,c):
    mylist.remove(oc);

print(mylist);
