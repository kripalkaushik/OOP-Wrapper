class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def display(self):
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")


class Employee(Person):
    def __init__(self, name, age, emp_id, salary):
        super().__init__(name, age)
        self.emp_id = emp_id
        self.salary = salary

    def display(self):
        super().display()
        print(f"Employee ID: {self.emp_id}")
        print(f"Salary: ${self.salary}")


class Manager(Employee):
    def __init__(self, name, age, emp_id, salary, department):
        super().__init__(name, age, emp_id, salary)
        self.department = department

    def display(self):
        super().display()
        print(f"Department: {self.department}")


person = None
employee = None
manager = None

while True:
    print("\n--- Python OOP Project: Employee Management System ---")
    print("1. Create a Person")
    print("2. Create an Employee")
    print("3. Create a Manager")
    print("4. Show Details")
    print("5. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        name = input("Enter Name: ")
        age = int(input("Enter Age: "))
        person = Person(name, age)
        print(f"\nPerson created with name: {name} and age: {age}")

    elif choice == 2:
        name = input("Enter Name: ")
        age = int(input("Enter Age: "))
        emp_id = input("Enter Employee ID: ")
        salary = float(input("Enter Salary: "))
        employee = Employee(name, age, emp_id, salary)
        print(f"\nEmployee created with name: {name}, age: {age}, ID: {emp_id}, and salary: ${salary}")

    elif choice == 3:
        name = input("Enter Name: ")
        age = int(input("Enter Age: "))
        emp_id = input("Enter Employee ID: ")
        salary = float(input("Enter Salary: "))
        department = input("Enter Department: ")
        manager = Manager(name, age, emp_id, salary, department)
        print(f"\nManager created with name: {name}, age: {age}, ID: {emp_id}, salary: ${salary}, and department: {department}")

    elif choice == 4:
        print("\nChoose details to show:")
        print("1. Person")
        print("2. Employee")
        print("3. Manager")
        K_choice = int(input("Enter your choice: "))

        if K_choice == 1 and person:
            print("\nPerson Details:")
            person.display()
        elif K_choice == 2 and employee:
            print("\nEmployee Details:")
            employee.display()
        elif K_choice == 3 and manager:
            print("\nManager Details:")
            manager.display()
        else:
            print("No data available!")

    elif choice == 5:
        print("\nExiting the system. All resources have been freed.")
        print("Goodbye!")
        break

    else:
        print("Invalid choice! Please try again.")
