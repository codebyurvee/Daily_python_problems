

#1. Count Special Characters
def countspchar():
    word = input("Enter a word:")
    count = 0
    for w in word:
        if w in "!@$%^&*":
             count +=1
    print(count)
     
             

# 2. Second Largest Digit
def second_large():
    nums = input("Enter a number: ")
    digits = []
    for n  in nums:
        digits.append(int(n))
    
    digits.sort()
    print(digits[-2])
            
        
# 3. Number Triangle
def numtriangle():
    n = int (input("enter a number: "))
    for i in range (1 , n+1):
        for j in range(1, i+1):
           print(j, end= "")
    
        print()
    

# 4. Count Words in a Sentence
def countword():
    sen = input("Enter Your Sentence: ")
    words = sen.split()
    print(len(words))

#5. Remove Vowels

def removevowels():
    word = input("Enter a word: ")
    for w in word:
        if w not in "AIUEOaiueo":
            print(w, end = "")
        
            
            

