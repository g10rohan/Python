# Write a Python script to sort (ascending and descending) a dictionary by value.

#Write a Python program to sort a dictionary by key.
d1 = {2: 70, 1: 90, 3: 80}


d2=sorted([(value,key) for (value,key) in d1.items()])
d3=sorted([(value,key) for (key,value) in d1.items()])

d2=dict(d2)
d3=dict(d3)
print("Sort by key:-",d2)
l1=d3.keys()
l2=d3.values()
d3=list(zip(l2,l1))
d3=dict(d3)
print("Sort by Value",d3)
#
# print(d2)
