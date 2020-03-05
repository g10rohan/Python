# Write a Python function that accepts a string and calculate the number of upper case letters and lower case letters.
# Sample String : 'The quick Brow Fox'
# Expected Output :
# No. of Upper case characters : 3
# No. of Lower case Characters : 12

def calculate(str):
    upper=0;
    lower=0;
    for j in str:
        i=ord(j);
        if i>65 and i<=90:
            upper=upper+1
        elif(i>=97 and i<=122):
            lower=lower+1;
    print("Upper Case Letter :-",upper);
    print("Lower Case Letter :-",lower);

str1=input("Enter the String:-");
calculate(str);