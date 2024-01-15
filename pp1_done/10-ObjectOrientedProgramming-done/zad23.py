class C():
    def __init__(self, name, surname, age, seniority):
        self.name = name
        self.surname = surname
        self.age = age
        self.seniority = seniority
    def __str__(self):
        if(self.age >= 18):
            result = (f"{self.surname.upper()}{self.name[:1].upper()}{self.seniority}")
            return result
        if(self.age < 18):
            result = (f"{self.surname.lower()}{self.name[:1].lower()}{self.seniority}")
            return result

em1 = C("Anna", "May", 17, 7)
em2 = C("George","Brown",21,4)

print(em1)
print(em2)