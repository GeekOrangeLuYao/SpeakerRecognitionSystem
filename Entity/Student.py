class Student:
    def __init__(self, name, real_name, sex, school, date):
        self.name = name
        self.real_name = real_name
        self.sex = sex
        self.school = school
        self.date = date

    def get_name(self):
        return self.name

    def get_real_name(self):
        return self.real_name

    def get_sex(self):
        return self.sex

    def get_school(self):
        return self.school

    def get_date(self):
        return self.date