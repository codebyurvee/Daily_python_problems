# 1. Remove Duplicates from a List

def rld():
    li = [2,3,4,3,2]
    newli =[]
    for l in li :
        if l not in newli:
            newli.append(l) 
    print(newli)    
        
#2. Find Second Largest Number
def fsn():
    li = [3,4,5,6,2,4,9,7]
    max = 0
    second_max = 0
    for i in li:
        if i>max:
            max = i
            
    for i in li:
        if i > second_max and i < max :
            second_max =  i
    print(second_max)
                  
#3. Merge Two Lists
def mergeli():
    a= [2,3,4,5]
    b=[3,4,5,6]
    print(a+b)
    
#4. sorrting a list
def sor():
        li =[2,4,5,3,7,4,99,5,3,2,95]
        li.sort()
        li.sort(reverse =True)
        print(li)
        
#5. Count Names Starting with 'A'
def cnsa():
    li = ["Aman", "Riya", "Ankit", "Neha", "Aryan"]
    count = 0
    for name in li:
        if name[0] =='A':
            count+=1
    print(count)
