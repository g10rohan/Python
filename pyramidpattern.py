g=3
for i in range(0,4):
    k=0
    while k<g:
       print(" ",end='');
       k=k+1
    g=g-1;
    for j in range(0, i + 1):
        print(" *", end='');
    print("");
