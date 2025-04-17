n=int(input("enter number of test cases:"))
while(n):
    n=n-1
    num=(input("enter a number:"))
    count=0
    for a in num:
        if int(a)!=0:
            if int(num)%int(a)==0:
                count=count+1
    print(count)               