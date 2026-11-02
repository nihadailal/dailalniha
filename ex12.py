
n = int(input("Entrez un nombre entier positif : "))
nb = len(str(n))
copie = n
s = 0
for i in range(nb):
    chiffre = copie % 10

    fact = 1
    for k in range(1, chiffre + 1):
        fact *= k
    s=s+ fact
    copie //= 10
if s == n:
    print("Oui")
else:
    print("Non")