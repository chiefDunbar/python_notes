# tee ratkaisusi tänne

class Course:
    def __init__(self, name: str, grade: int, credits: int):
        self.__name = name
        self.__grade = grade
        self.__credits = credits

    @property
    def name(self):
        return self.__name
    
    @property
    def grade(self):
        return self.__grade
    
    @property
    def credits(self):
        return self.__credits

    @grade.setter
    def grade(self, grade):
        if grade > self.__grade:
            self.__grade = grade
    
    @credits.setter
    def credits(self, credits):
        self.__credits = credits

    def __str__(self):
        return f"{self.name} ({self.credits} cr) grade {self.grade}"   

class CourseRegister:
    def __init__(self):
        self.register = {}

    def add_course(self, name: str, grade: int, credits: int):
        if name not in self.register:
            self.register[name] = Course(name, grade, credits)
            return
        self.register[name].grade = grade
        self.register[name].credits = credits

    def get_course(self, name: str):
        if name in self.register:
            return self.register[name]
        return None
    
    def get_statistics(self):
        course_number = len(self.register)
        total_credits = 0
        grade_sum = 0
        grade_distribution = {}

        for grade in range(1, 6):
            grade_distribution[grade] = 0

        for course in self.register.values():
            total_credits += course.credits
            grade_sum += course.grade
            grade_distribution[course.grade] += 1

        return course_number, total_credits, (grade_sum / course_number), grade_distribution

class TrackerApplication:
    def __init__(self):
        self.register = CourseRegister()

    def help(self):
        print("1 add course")
        print("2 get course data")
        print("3 statistics")
        print("0 exit")

    def execute(self):
        self.help()
        while True:
            print("")
            command = input("command: ")
            if command == "1":
                self.add_course()
            elif command == '2':
                self.get_course()
            elif command == '3':
                self.get_statistics()
            elif command == '0':
                break
    
    def add_course(self):
        name = input("course: ")
        grade = int(input("grade: "))
        credits = int(input("credits: "))
        self.register.add_course(name, grade, credits)

    def get_course(self):
        name = input("course: ")
        course = self.register.get_course(name)
        if course is None:
            print("no entry for this course")
            return 
        print(course)
    
    def get_statistics(self):
        course_number, total_credits, grade_mean, grade_distribution = self.register.get_statistics()
        print(f"{course_number} completed courses, a total of {total_credits} credits")
        print(f"mean {grade_mean:.1f}")
        print("grade distribution")
        for grade, frequency in grade_distribution.items():
            print(f"{grade}: {'x' * frequency}")
        
tracker = TrackerApplication()
tracker.execute()