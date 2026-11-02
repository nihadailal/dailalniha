z=int(input("z="))
i=2
while i<z:
    if z%i==0:
        print("non premier")
        break
    else:
        print("premier")