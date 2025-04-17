
def sum_of_digits(n):
    sum=0
    while(n!=0):
        sum=sum+(n%10)
        n=n//10
    return sum

num=int(input("what is the number: "))
sum=0
while((num//10)!=0):
    sum=sum_of_digits(num)
    num=sum
print(f"digital root of number is {num}")