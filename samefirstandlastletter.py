# Write a Python program to count the number of strings where the string length is 2 or more and the first and last character are same from a given list of strings.
# Sample List : ['abc', 'xyz', 'aba', '1221']
# Expected Result : 2
mylist=['abc', 'xyz', 'aba', '1221'];
count=0;
for i in range(0,len(mylist)):
        if mylist[i][0]==mylist[i][-1]:
            count+=1
print(count);