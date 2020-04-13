class Student:
    
    def __init__(self, name, major, gpa, is_on_probabtion):
        self.name = name
        self.major = major
        self.gpa = gpa
        self.is_on_probabtion = is_on_probabtion

    def print(self):
        print("Student[" + self.name +"," + self.major + "," + str(self.gpa) + "," + str(self.is_on_probabtion) + "]")
   # def __str__(self):
   # return "Student[" + self.name +", major" + ", gpa" + str(self.gpa) + "]"