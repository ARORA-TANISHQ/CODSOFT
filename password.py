import random
i=0
n=int(input("Enter the length of password:-"))
arr=[]
for i in range (n):
    asci_val = random.randint(33, 126)
    elem=chr(asci_val)
    arr.append(elem)
    i=+1
print("YOUR PASSWORD IS =>")
print(*arr,sep=" ")
