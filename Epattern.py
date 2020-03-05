for i in range(0,5):
    for j in range(0,5):
        if i==0 or i==2 or i==4 or j==0:
            print("*",end='');
        else:
            print(" ",end='');
    print("");