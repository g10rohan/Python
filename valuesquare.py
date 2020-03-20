# Write a Python script to sort (ascending and descending) a dictionary by value.


# d1 = {1: 90, 2: 70, 3: 80}
#
#
# d2=sorted([(value,key) for (key,value) in d1.items()])
#
# d2=dict(d2)
# l1=d2.keys()
# l2=d2.values()
# d2=list(zip(l2,l1))
# d2=dict(d2)
# print(d2)

# 6. Write a Python script to generate and print a dictionary that contains a number (between 1 and n) in the form (x, x*x).
# Sample Dictionary ( n = 5) :
# Expected Output : {1: 1, 2: 4, 3: 9, 4: 16, 5: 25}





x=input("Enter number:")
x=int(x)
d1={}
for i in range(1,x+1):
    d1[i]=i*i


print(d1)

