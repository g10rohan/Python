# . Write a Python program to print the even numbers from a given list.
# Sample List : [1, 2, 3, 4, 5, 6, 7, 8, 9]
# Expected Result : [2, 4, 6, 8]
mylist=[1, 2, 3, 4, 5, 6, 7, 8, 9]
mylist1=list(filter(lambda x:x%2==0,mylist))
print(mylist1);