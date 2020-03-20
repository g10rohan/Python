# Write a Python program to add 'ing' at the end of a given string (length should be at least 3). If the given string already ends with 'ing' then add 'ly' instead. If the string length of the given string is less than 3, leave it unchanged.
# Sample String : 'abc'
# Expected Result : 'abcing'
# Sample String : 'string'
# Expected Result : 'stringly'
s1=input("String:-");
if len(s1)>=3 and s1.endswith('ing'):
    s1=s1+'ly'
elif len(s1)>=3:
    s1 = s1 + 'ing'

print(s1);