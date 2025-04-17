class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def __add__(self, other):
        if isinstance(other, Employee):
            return self.salary + other.salary
        return NotImplemented

    def __sub__(self, other):
        if isinstance(other, Employee):
            return self.salary - other.salary
        return NotImplemented

    def __eq__(self, other):
        if isinstance(other, Employee):
            return self.salary == other.salary
        return NotImplemented

    def __lt__(self, other):
        if isinstance(other, Employee):
            return self.salary < other.salary
        return NotImplemented

    def __le__(self, other):
        if isinstance(other, Employee):
            return self.salary <= other.salary
        return NotImplemented

    def __gt__(self, other):
        if isinstance(other, Employee):
            return self.salary > other.salary
        return NotImplemented

    def __ge__(self, other):
        if isinstance(other, Employee):
            return self.salary >= other.salary
        return NotImplemented

    def __str__(self):
        return f"Employee(name: {self.name}, salary: {self.salary})"

# Example usage:
emp1 = Employee("Alice", 50000)
emp2 = Employee("Bob", 60000)

# Combine salaries
total_salary = emp1 + emp2
print(f"Total Salary: {total_salary}")

# Compare employees
print(f"{emp1.name}'s salary is equal to {emp2.name}'s: {emp1 == emp2}")
print(f"{emp1.name}'s salary is less than {emp2.name}'s: {emp1 < emp2}")
print(f"{emp1.name}'s salary is greater than {emp2.name}'s: {emp1 > emp2}")
