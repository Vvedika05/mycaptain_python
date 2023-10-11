n=int(input("Enter the number of terms to be printed:"))
a,b=0,1
print(a,b)
for i in range(n):
    c=a+b
    a=b
    b=c
    print(c)


