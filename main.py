# link https://www.youtube.com/watch?v=RSl87lqOXDE&t=825s
class Employee:
    def __init__(self, firstname, lastname, salary):
        self.firstname = firstname
        self.lastname = lastname
        self.salary = salary

    @property
    def fullname(self):
        return f"{self.firstname} {self.lastname}".title()

    @fullname.setter
    def fullname(self, full_name):
        full_name = full_name.strip()
        if not full_name:
            raise ValueError("full name is required")
        name = full_name.split(" ", 2)
        first, last = name[0], name[1]
        self.firstname = first
        self.lastname = last

    def __str__(self):
        print(self.fullname)


class Manager(Employee):
    def __init__(self, firstname, lastname, salary, employees=None):
        super().__init__(firstname, lastname, salary)
        if employees is None:
            employees = []
        self.employees = employees

    def add_employee(self, *employees):
        self.employees.extend([emp for emp in employees if emp not in self.employees])

    def remove_employee(self, emp):
        if emp in self.employees:
            self.employees.remove(emp)

    def print_employees(self):
        print(f'{self.fullname} manages:')
        if not self.employees:
            print('no employees found'.capitalize())
            return
        for emp in sorted(self.employees, key=lambda e: e.firstname.lower()):
            print(f"--> {emp.fullname}")


def main():
    # e = Employee('John', 'Smith', 3000)
    # e.fullname = 'Lane Smith 3000'

    emp1 = Employee('john', 'doe', 15_000)
    emp2 = Employee('Cole', 'Smith', 19_000)
    emp3 = Employee('Alice', 'McLover', 18_000)

    manager1 = Manager(firstname='John', lastname='Cooklord', salary=30_000)
    manager2 = Manager(firstname='Peter', lastname='Johnson', salary=40_000, employees=[emp1])
    manager2.add_employee(emp2, emp3)

    [m.print_employees() for m in [manager1, manager2]]


if __name__ == '__main__':
    main()
