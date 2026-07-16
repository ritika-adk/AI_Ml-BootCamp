num=int(input("Enter any number"))
rev=0
original =num

while(num>0):
    r=num%10;
    rev=rev*10+r
    num=num//10

if(original==rev):
    print("The number is palindrome")
else:
    print("The number is not palindrome")        
