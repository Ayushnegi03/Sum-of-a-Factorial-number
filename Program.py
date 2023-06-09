#Here is a Python program which sum factorail number in digit wise
def rand(rem):
    if rem==1 or rem ==0:
        return 1
    else:
        return rem*rand(rem-1)
    
num=int(input("Enter the number:"))
sum=0
#x=len(num)
m=num
while num > 0:
    rem=num%10
    sum=sum + rand(rem)
    num=num//10
    
if sum==m:
    print("It is equal to:",sum)
else:
    print("It is not equal to:",sum)
#Let's suppose enter the number 145 
#First 5!=5*4*3*2*1=120
#Second 4!=4*3*2*1=24
#Third 1!=1
#The answer is 120+24+1=145 
