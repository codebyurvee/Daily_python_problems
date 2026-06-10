#1. Find Total Marks
def countmarks():
    marks = [78, 85, 90, 67, 88]
    total = 0
    for i in marks:
        total +=i
    print(total)

#2. Count Names Longer Than 5 Characters
def nl():
    li = ["Aman", "Priyanka", "Neha", "Aryan", "Rohit"]
    count=0
    for name in li:
        if len(name) > 5:
                count+=1
    print(count)
                

# 3. Print Only Names Ending with 'a'
def con():
    li = ["Riya", "Aman", "Neha", "Aryan", "Pooja"]
    for i in li:
        if i[-1]=="a":
            print(i)

# 4. Create a New List of Squares
def square():
    li = [1, 2, 3, 4, 5]
    newli =[]
    for i in li:
        newli.append(i*i)
    print(newli)  


# 5. Find Average Marks
def avg():
    marks = [78, 85, 90, 67, 88]
    total = 0
    for i in marks:
        total += i
    a =len(marks)
    print(total/a)

    
