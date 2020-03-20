# Write a Python script to check if a given key already exists in a dictionary.
dic1={1:10, 2:20};
count=0
k=int(input("Enter key you want to check if present or not:-"));
if k in dic1.keys():
     print(k, " is Present in Dictionary.");
else:
    print(k, " is not Present in Dictionary.");