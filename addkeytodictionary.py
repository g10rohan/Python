#Write a Python script to add a key to a dictionary.

x=input("Enter number:")
x=int(x)
d1={}
for i in range(1,x+1):
    k = int(input("Enter key:"));
    v = input("Enter value:");
    d1.update({k: v});
print(d1);
k=int(input("Enter key:"));
v=input("Enter value:");
d1.update({k:v});
print(d1)
