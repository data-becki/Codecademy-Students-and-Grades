class Student():
    """
    This will be our data model at the fake hs
    """    
    def __init__(self, name, year):
        """
        Constructor for Student that takes name and year
        """
        self.name = name
        self.year = year
        self.grades = []
    
    def add_grade(self, grade):
        """
        Method to verify if grade is type Grade and if so,
        add it to the Student's .grades
        """
        if type(grade) is Grade:
            self.grades.append(grade)
            
class Grade():
    """
    A class to determine if a student has a passing grade.
    """
    minimum_passing = 65
    
    def __init__(self, score):
        """
        Initializing the score
        """
        self.score = score
        
    def is_passing(self):
        """
        Method that returns whether a Grade has a passing .score.
        """
        if self.score >= Grade.minimum_passing:
            return True
        else:
            return False
        
roger = Student("Roger van der Weyden", 10)
sandro = Student("Sandro Botticelli", 12)
pieter = Student("Pieter Bruegel the Elder", 8)

# Create a new Grade with a score of 100 and add it to 
# pieter's .grade attribute using .add_grade()
# I don't understand the structure of this
pieter.add_grade(Grade(100))
print(pieter.grades)
print(Grade(100).score)

# Why is this generating an error?
# How do you get this to actually show True or False?
pieter.is_passing()

# Write a Student method get_average() that returns the student's average score.

# Add an instance variable to Student that is a dictionary called .attendance, with dates
# as keys and booleans as values that indicate whether the student attended school that day.
