# 🧑‍💼 Employee Management System (Python OOP Project)

## 📌 Introduction
The **Employee Management System** is a menu-driven console application built using **Python** and **Object-Oriented Programming (OOP)** principles.  
This project demonstrates real-world modeling of people in an organization using **inheritance**, **method overriding**, and **encapsulation**.

The application allows users to create and manage:
- Persons
- Employees
- Managers

It is suitable for **college practicals**, **Python beginners**, and **OOP learning projects**.

---

## 🎯 Objectives
- Understand Python OOP concepts
- Implement inheritance and method overriding
- Build a menu-driven console application
- Practice clean and readable Python code

---

## 🛠️ Technologies Used
- **Language:** Python 3.x
- **Paradigm:** Object-Oriented Programming (OOP)
- **Environment:** Console / Terminal

---

## 📂 Project Structure
```
Employee_Management_System/
│
├── employee_management.py
└── README.md
```

---

## 🧠 OOP Concepts Explained

### 1️⃣ Class
A blueprint used to create objects.

### 2️⃣ Object
An instance of a class.

### 3️⃣ Inheritance
Allows one class to inherit attributes and methods from another class.

### 4️⃣ Method Overriding
Redefining a parent class method in the child class.

### 5️⃣ super() Function
Used to call parent class constructors and methods.

---

## 🧩 Class Description

### 🔹 Person Class
The base class that stores basic personal details.

**Attributes:**
- `name`
- `age`

**Methods:**
- `display()` → Displays name and age

---

### 🔹 Employee Class (Inherits Person)
Adds employee-related information.

**Additional Attributes:**
- `emp_id`
- `salary`

**Methods:**
- Overrides `display()` to show employee details

---

### 🔹 Manager Class (Inherits Employee)
Adds department information for managers.

**Additional Attributes:**
- `department`

**Methods:**
- Overrides `display()` to include department

---

## 💻 Source Code
```python
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
```

---

## ▶️ How to Run the Project
1. Install Python 3.x
2. Save the file as `employee_management.py`
3. Open terminal or command prompt
4. Run the program:
```bash
python employee_management.py
```

---

## 🧪 Sample Output
```
--- Python OOP Project: Employee Management System ---
1. Create a Person
2. Create an Employee
3. Create a Manager
4. Show Details
5. Exit
Enter your choice: 3

Manager created with name: Amit, age: 30, ID: M101, salary: $80000, and department: IT
```

---

## 🚀 Future Enhancements
- Store multiple records using lists
- Add update and delete operations
- File handling (save/load data)
- Database integration (SQLite/MySQL)
- GUI using Tkinter or Web framework

---

## 🎓 Learning Outcomes
After completing this project, you will be able to:
- Apply OOP concepts in Python
- Build real-world console applications
- Use inheritance effectively
- Write clean and structured Python code

---

## 👨‍💻 Author
**Kripal K Prajapati**  
Python | OOP | Data Science Student

---

## ⭐ Conclusion
This Employee Management System is a strong beginner-to-intermediate level Python project.  
It helps in understanding how OOP concepts work together in real applications.

Happy Coding! 🚀
