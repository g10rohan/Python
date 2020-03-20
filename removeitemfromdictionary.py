# 12. Write a Python program to remove a key from a dictionary. pop
d1={1: 10, 2: 20, 3: 30, 4: 40, 5: 50, 6: 60};
print(d1);
k=int(input("Enter Key you want to remove:-"));
d1.pop(k);
print(d1)