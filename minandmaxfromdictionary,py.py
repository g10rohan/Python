# 15. Write a Python program to get the maximum and minimum value in a dictionary.
d1={1: 10, 2: 20, 3: 30, 4: 40, 5: 50, 6: 60};
max=0
min=d1[2]
for value in d1.values():
    if max<value and max>=0:
        max=value;
    if min>value :
        min=value;
print(min);
print(max);