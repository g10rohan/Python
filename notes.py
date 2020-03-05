#13.	Write a C program to count total number of notes in given amount.
a=int(input("Enter amount"))
n5=a//500;
temp=a%500
n1=temp//100
print("Notes of 500:-",n5,"\nNotes of  100:-",n1);