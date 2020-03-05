for i in range(0, 5):
    for j in range(0, 5):
            if i == j or j==i+4 or i==j+4 or i==1 and j==i+2 or i==3 and i==j+2:
                print("*", end='');
            else:
                print(" ", end='');

    print("");
print("___________________________________________________________")
for i in range(0, 5):
    for j in range(0, 5):
        if i == j or i+j==4:
            print("*", end='');
        else:
            print(" ", end='');

    print("");
