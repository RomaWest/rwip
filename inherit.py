from empl import Employee


class ITEmployee(Employee):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.skills = []

    def add_skill(self, skill):
        self.skills.append(skill)

if __name__ == "__main__":
    empl = ITEmployee()
    empl.set_name("Elena")
    empl.add_skill("Python")
    empl.add_skill("git")
    print(empl)
