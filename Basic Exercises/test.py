class student:
    def __init__(self, name, rno):
        self.name = name
        self.rno = rno
    def display(self):
        print("Hi ",self.name ,"your roll number is ", self.rno)

n = student("ravi", 40)
n.display()