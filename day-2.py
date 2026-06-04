#1. Count Characters
sen = input("enter a sentence: ")
print(len(sen))

#2. Count Digits
numb = input("enter numbers: ")
countnum = 0
for i in numb:
        countnum += 1
print("count",countnum)

#3. Print Multiplication Table
num = int(input("enter a number: "))
for i in range (1,11,1):
    print(num,"*",i,"=",i*num)

#4. Count Vowels and Consonants
word = input("enter a word: ")
count = 0
constant = 0
for w in word:

    if w in "aieouAEIOU":
        count += 1

    else:
            constant += 1
print("consonants", constant)
print("vowels", count)

#5. Sum of Digits
lis = [int(input("enter list numbers:"))]
print(sum(lis))
