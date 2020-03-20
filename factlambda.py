l=1
n=int(input("Enter value"))
fact = lambda l: 1 if l == 0 else l * fact(l-1)
print(fact(n))