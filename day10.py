# Problem 1: Student Class

class Student:
    def __init__(self, name, age, course):
        self.name = name
        self.age = age
        self.course = course

    def display(self):
        print("Name:", self.name)
        print("Age:", self.age)
        print("Course:", self.course)

    def change_course(self, new_course):
        self.course = new_course


# Create Object
s1 = Student("Esha", 22, "BCA")

# Display Details
s1.display()

# Change Course
s1.change_course("AI")

print("\nAfter Changing Course:")
s1.display()


#2.Bank Account
class BankAccount:
    def __init__(self,account_holder,balance):
        self.account_holder = account_holder
        self.balance = balance
    def display(self):
        print("Account Holder name is : ",self.account_holder)
        print("Your account Balance is :",self.balance)
    def deposit(self,amount):
        self.balance += amount
        print("Deposit is successful")
    def withdraw(self,amount):
        if self.balance < amount:
            print("insuffocient balance")
        else:
            self.balance-=amount
            print("withdran is successful")
    def show_balance(self):
        print("Balance:", self.balance)
b1 = BankAccount("Urvashi",10)
b1.display()
b1.deposit(30)
b1.withdraw(20)
b1.show_balance()

#Problem no .3. Rectangle
class Rectangle:
    def __init__(self,length,width):
        self.length=length
        self.width=width
    def area(self):
        print("area of Rectange is :", self.length*self.width)
    def perimeter(self):
        p = 2*(self.length+self.width)
        print("Perimeter of Rectangle is: ",p)
r1=Rectangle(2,4)
r1.area()
r1.perimeter()

# Problem 4: Employee Salary

class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def display(self):
        print("Employee Name:", self.name)
        print("Employee Salary:", self.salary)

    def increase_salary(self, percent):
        increase = self.salary * percent / 100
        self.salary += increase
        print("Salary increased successfully!")


# Create Object
e1 = Employee("Esha", 40000)

# Display Details
e1.display()

# Increase Salary by 10%
e1.increase_salary(10)

# Display Updated Details
e1.display()

#problem no.5 Library Book
class Book:
    def __init__(self,title,author,available = True):
        self.title = title
        self.author = author
        self.available = available
    def show(self):
        print("Title of the book: ",self.title)
        print("Author of the book: ",self.author)
        print("The book is Available in our library")
b1 = Book("hey","esha")
b1.show()
