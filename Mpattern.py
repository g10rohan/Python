for i in range(0, 5):
    for j in range(0, 5):
        if j==0 or j==4 or i<3 and i==j or i+j==4 and i<3:
            print("*", end='');
        else:
            print(" ", end='');

    print("");
