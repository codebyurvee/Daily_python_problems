#1. Count Numbers Greater Than 10
def count_gt10 ():
    nums = list(map(int, input("enter list numbrss").split(",")))
    count = 0
    for i in nums :
        if i>10:
            count+=1
    print(count)

#2.First and Last Character
def fl_stringchar():
    word= input("enter a word")
    print("first char of string",word[0])
    print("last char of the string",word[-1])
    
# count natural number in a list
def countnum():
    nums = list(map(int, input("enter list numbrss").split(",")))
    count = 0
    for num in nums:
        if num %2==0:
            count+=1
    print(count)

    
    
    
#4. number divisible by 3
def dby3():
    num = int(input("Enter number and check it is divisible by 3 or not: "))
    if num%3 == 0:
        print(num , "it is divisible by 3")
dby3()


#5. Store Names in a List
def storenames():
    names = []
    for i in range(5):
        name = input("enter name: ")
        names.append(name)
    print(names)
    
