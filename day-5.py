

# 1. Find Largest Number in a List

def largenu():
    nums = [3,9,2,7,8,1]
    max = 0
    for n in nums:
        if n > max:
            max = n
    print ("largest number in this list is",max)
           

### 2. Function: Even or Odd
def even_odd():
    number = int(input("enter a number:"))
    modulus = number %2
    if modulus == 0:
        print("even")
    else:
        print("odd")


### 3. Count Positive Numbers in a List
def positive_list_no():
    li = [3,-4,3,5,-7,-1]
    count = 0
    for i in li:
        if i >=0:
            count += 1
    print(count)
            

### 4. Sum of List Elements

def sum_of_list():
  li = [2,4,5,6,7,3,9]
  total = 0
  for i in li:
    total += i
  print(total)
  
### 5. Function: Reverse String

def reverse_string():
  word = input("enter a word ")
  print(word[::-1])


---
