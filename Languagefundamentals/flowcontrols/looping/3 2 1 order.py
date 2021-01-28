num=int(input("enter number"))
while(num!=0):
    digit=num%10
    print(digit)
    num//=10

num=int(input("enter number"))
result=""
while(num!=0):
    digit=num%10
    result+=str(digit)
    num//=10
print(result)