# Write a Python program to get a string from a given string where all occurrences of its first char have been changed to '$', except the first char itself.
# Sample String : 'restart'
# Expected Result : 'resta$t'
s1=input("String:-");
n=s1.count(s1[0]);
s2=s1[1:len(s1)+1].replace(s1[0],'$',n);
s1=s1[0]+s2
print(s1)