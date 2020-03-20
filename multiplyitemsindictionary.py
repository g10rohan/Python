# Write a Python program to multiply all the items in a dictionary.
d1={1: 10, 2: 20, 3: 30, 4: 40, 5: 50, 6: 60};
mul=1
for value in d1.values():
    mul=value*mul;
print(mul);