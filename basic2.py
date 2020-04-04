# Online Python compiler (interpreter) to run Python online.
# Write Python 3 code in this online editor and run it.
class people:
    def __init__(self, name, weight, height, sex):
        self.name = name
        self.weight = weight
        self.height = height
        self.sex = sex
    def display(self):
        print("My name is " + self.name)
        print("My Weight is " + str(self.weight))
        print("My Height is " + str(self.height))
        print("My Sex is " + self.sex + "\n")
        
class robot:
    def __init__(self, name, weight, color):
        self.name = name
        self.weight = weight
        self.color = color
    
    def display(self):
        print("My name is " + self.name)
        print("My Weight is " + str(self.weight))
        print("My Color is " + self.color + "\n")
        
#Defining the list of people
p1 = people(name = "Mahesh", weight = 88, height = 5.10, sex = "M")
p2 = people(name = "Manjula", weight = 80, height = 5.00, sex = "F")

#Defining the list of Robots
r1 = robot(name = "Tom", weight = 40, color = "Red")
r2 = robot(name = "Jerry", weight = 44, color = "Black")

#Assigning owners to the Robots
p1.robot_owned = r2
p2.robot_owned = r1

#Printing the details of the people and their respective Robots
p1.display()
p1.robot_owned.display()
p2.display()
p2.robot_owned.display()
