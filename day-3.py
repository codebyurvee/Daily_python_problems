
# 1. Count Uppercase Letters

def countupper():
    text = input("enter a text ")
    countup = 0
    for i in text:
        if i.isupper():
            countup += 1
    print(countup)

    
#2. Find Largest Digit
def findlarge():
    nums = input("enter a number ")
    max = nums[0]
    for i in nums:
        if i > max:
            max = i
    print(max)

#3. Print Stars Pattern
def starpattern():
    n = int(input("enter a number "))
    for i in range(1, n + 1):
        print("*" * i)


#4. count spaces
def countspace():
    text = input("enter a text: ")
    countsp = 0
    for i in text:
        if i.isspace():
            countsp += 1
    print(countsp)


#5. palidrome check
def palindrome():
    word = input("enter a word: ")
    if word == word[::-1]:
        print("Palindrome")
    else:
        print("Not Palindrome")
palindrome(     )
