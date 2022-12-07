# question 5

l=int(input("enter the limit: "))
s=0
for i in range(0,l+1):
    if i%3==0 or i%5==0:
        s=s+i
print("sum of multiples of 3 and 5 are: ",s)
