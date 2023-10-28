def most_frequent(Input):
    d={}
    d1={}
    #count the number of times each alphabet is repeated and sstore it in the dictionary 
    for i in Input:
        if i in d:
            d[i]=d[i]+1
        else:
            d[i]=1
    print(d)
    #prints the letters in decreasing order of frequency. 
    def remo():
        s=0
        for i in d:
            if d[i]>s:
                s=d[i]
                d1[s]=i
                a=i
        print(d1[s],"=",s)
        d1.popitem()
        del d[a]
    #calling the function remo for each letter present in the dictionary
    for j in range(len(d)):
        remo()
Input=input("Please Enter a string")
#caling the function 
most_frequent(Input)
