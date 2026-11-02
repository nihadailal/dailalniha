u = int(input("u="))
n = list(map(int, input("n=").split()))
for i in range(len(n)):
    if sum(n) == u:
        print("parfait")
        break
    else:
        print("non parfait") 