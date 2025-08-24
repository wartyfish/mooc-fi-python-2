class Course:
    def __init__(self, name):
        self.__name = name
        self.__grade = None
        self.__credits = 0

    @property
    def grade(self):
        return self.__grade
    
    @grade.setter
    def grade(self, grade):
        try:
            grade = int(grade)
        except ValueError:
            raise ValueError("Grade must be inputted as an integer")

        if grade > 5 or grade <= 0:
            raise ValueError("Grade must be between 1-5")

        if self.__grade is None or grade > self.__grade:
            self.__grade = grade

    @property
    def credits(self):
        return self.__credits
    
    @credits.setter
    def credits(self, credit):
        try:
            credit = int(credit)
        except ValueError:
            raise ValueError("Credit must be inputted as an integer")

        if credit < 0:
            raise ValueError("Credits cannot be negative")

        self.__credits = credit

    def __str__(self):
        return f"{self.__name} ({self.__credits} cr) grade {self.__grade}"

class CourseRecords:
    def __init__(self):
        self.__courses = {}
    
    def add_course(self, name, grade, credit):
        if name not in self.__courses:
            self.__courses[name] = Course(name)

        self.__courses[name].grade = grade
        self.__courses[name].credits = credit

    def search_name(self, name):
        if name in self.__courses:
            return self.__courses[name]
        else:
            return "no entry for this course"
    
    @property
    def course_list(self):
        c_list = list(self.__courses)
        return c_list

    def sum_credits(self):
        total_credits = 0
        for name in self.__courses:
            total_credits += self.__courses[name].credits
        return total_credits

    def sum_grades(self):
        total_grade = 0
        for name in self.__courses:
            total_grade += self.__courses[name].grade
        return total_grade

    def list_grades(self):
        g = {i: 0 for i in range(6)}
        
        for name in self.__courses:
            g[self.__courses[name].grade] += 1

        return g

class UI:
    def __init__(self):
        self.courses = CourseRecords()

    def help(self):
        print("1 add course")
        print("2 get course data")
        print("3 statistics")
        print("0 exit")

    def execute(self):
        self.help()
        while True:
            cmd = input("command: ")

            if cmd == "0":
                break

            elif cmd == "1":
                name = input("course: ")
                grade = int(input("grade: "))
                credit = int(input("credits: "))

                self.courses.add_course(name, grade, credit)

            elif cmd == "2":
                name = input("course: ")
                print(self.courses.search_name(name))

            elif cmd == "3":
                print(f"{len(self.courses.course_list)} completed courses, a total of {self.courses.sum_credits()} credits")
                print(f"mean {self.courses.sum_grades() / len(self.courses.course_list):.1f}")
                print("grade distribution")
                for i in range(5, 0, -1):
                    print(f"{i}: {"x"*self.courses.list_grades()[i]}")



ui= UI()
ui.execute()

if False:
    c = CourseRecords()
    c.add_course("Chem", 5, 5)
    c.add_course("Bio", 3, 5)
    c.add_course("Phys", 3, 4)

    print(f"Number of courses: {len(c.course_list)}")
    print(f"Total credits: {c.sum_credits()}")
    for i in range(6):
        print(f"{i}: {"X"*c.list_grades()[i]}")