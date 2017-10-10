class Employee:
    def __init__(self, name=None, surname=None, position=None, salary=0):
        self.name = name
        self.surname = surname
        self.position = position
        self.salary = salary

    def set_name(self, name):
        self.name = name

    def set_position(self, position):
        self.position = position

    def full_name(self):
        return str(self.name + " " + self.surname + " " + self.position)

    def income(self, months):
        return self.salary * months

    def __add__(self, other):
        pass


if __name__ == "__main__":
    def __str__(self):
        return "<Employee: " + self.full_name() + ">"

if __name__ == "__main__":
    emp = Employee("Elena", "Pian", "QA")
    print(emp)

