for i in range(0,4):
    for j in range(0,4):
        if j==0 or j==3 or i==0 or i==3:
            if i==j:
                print("*",end='');
            else:
                print(" ",end='');

    print("");