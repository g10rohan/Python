# Write a Python function that takes a number as parameter & check the number is prime or not.
# Note : A prime number (or a prime) is a natural number greater than 1 and that has no positive divisors other than 1 and itself.
def prime(num):
    if num>1:
        for i in range(2,num):
            if num%i!=0:
                print(num,"is Prime");
                break
        else:
            print(num,"Not Prime");


prime(int(input("Tak:-")));