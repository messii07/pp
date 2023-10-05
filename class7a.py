class Student:
    def __init__(self, name, sex, course, result):
        self.name = name
        self.sex = sex
        self.course = course
        self.result = result
    
    def display(self):
        print('Name:', self.name)
        print('Sex:', self.sex)
        print('Course:', self.course)
        print('Result:', self.result)

# Create an instance of the Student class
s1 = Student('Ashwin', 'F', 'SDJDFB', '33')

# Call the display method to print student information
s1.display()
