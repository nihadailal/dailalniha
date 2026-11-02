p=input("p= ")
s=input("s=")
n=0
for i in range(len(p)):
    if p[i]==s:
        n=n+1
        print(n)
print(n)