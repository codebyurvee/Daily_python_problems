"""1. Number Positive, Negative ya Zero

User se ek number input lo aur print karo:

"Positive"
"Negative"
"Zero"""
num = int(input("enter a number : "))
if num > 0:
    print("Positive")
elif num == 0:
    print("Zero")
else:
    print("Negative")


#2.even or odd
if num %2==0:
    print("even")
elif num%2!=0 :
    print("odd")
else:
    print("value Error")


#3. string reverse
str = input("enter your name: ")
print(str[::-1])

#4.count vowels
str = input("enter your name: ")
count = 0
for i in str:
    if i in "aeiouAEIOU":
        count += 1
print(count)

#5. find max
a = int(input("enter a number: "))
b = int(input("enter a number: "))
c = int(input("enter a number: "))
lis = [a,b,c]
print(max(lis,"max number"))