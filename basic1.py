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
p1 = people(name = "Mahesh", weight = 88, height = 5.10, sex = "M")
p2 = people(name = "Manjula", weight = 80, height = 5.00, sex = "F")
p1.display()
p2.display()
