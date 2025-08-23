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

        self.__credit = credit

    def __str__(self):
        return f"{self.__name} ({self.__credits} cr) grade {self.__grade}"

class CourseRecords:
    def __init__(self):
        self.__courses = {}

    

class UI:
    def __init__(self):
        pass

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
                course = input("course: ")
                grade = int(input("grade: "))
                credit = int(input("credits: "))


if __name__ == "__main__":
    poo_course = Course("pooology")
    poo_course.grade = "bum"
    poo_course.credits = 5

    print(poo_course)