for i in range(0, 5):
    for j in range(0, 5):
        if j==0 or i==0 or i==2 or i>2 and i==j or i==1 and j==4:
            print("*", end='');
        else:
            print(" ", end='');

    print("");
