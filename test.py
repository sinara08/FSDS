class student:
    def __init__(self, n='',m=0):
        self.name=n
        self.age=m
    def Display(self):
        print("name:",self.name)
        print("age:",self.age)

s=student()
s.Display()

print('---------------------')
s1=student("Ankur",234)
s1.Display()

