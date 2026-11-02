q=input("q=")
print(q.lower())
q=q.lower()
for i in range(len(q)):
    if q==q[::-1]:
        print("Palindrome")
        break
    else:
        print("Not Palindrome")