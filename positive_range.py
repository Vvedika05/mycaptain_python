l1=eval(input("Enter a list of integer values"))
print("The positive number in the given list1 are:")
for i in l1:
    if i>0:
        print(i,end=" ")
print("\n")
l2=eval(input("Enter a list of integer values"))
print("The positive number in the given list2 are:")
for i in range(len(l2)):
    if l2[i]>0:
        print(l2[i],end=" ")


