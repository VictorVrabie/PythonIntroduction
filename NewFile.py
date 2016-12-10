#1st exercise
"""def Median(numbers):
    ln = len(numbers)
    srt = sorted(numbers)

    return numpy.median(numpy.array(x))
print(Median([1,2,15,16]))


#2nd exercise
city = input("Where you are going ? ")
d = int(input("How many days you are staying"))

def Hotel_cost(d, city):
    if city == "Paris":
        return 180*d
    if city == "London":
        return 220 * d
    if city == "Brussels":
        return 240 * d
    if city == "New York":
        return 500 * d
    else:
        return 140 * d

def car_cost(d):
    if d>=7:
        return (40*d)-50
    else:
        return (40*d)

def total_cost(d,city):
    return Hotel_cost(d,city)+car_cost(d)

print(total_cost(d,city))

#3rd exercise

Billy = {
    "name":"Billy",
    "homework": [90.0,97.0,75.0,92.0],
    "quizzes": [88.0,40.0,94.0],
    "test": [75.0,90.0],
}
Joyce = {
    "name":"Joyce",
    "homework": [100.0,92.0,98.0,100.0],
    "quizzes": [82.0,83.0,91.0],
    "test": [89.0,97.0],
}

Steven = {
    "name":"Steven",
    "homework": [0.0,87.0,75.0,22.0],
    "quizzes": [0.0,75.0,734.0],
    "test": [100.0,100.0],
}

students = [Billy,Joyce,Steven]
for student in students:
    for key in student.keys():
        print(student.keys())

def average(numbers):
    total = float(sum(numbers))
    return total/len(numbers)

def get_average(student):
    home1 = average(student['homework'])
    quiz1 = average(student['quizzes'])
    test1 = average(student['test'])
    return 0.1*home1+0.4*quiz1+0.5*test1

print(get_average(Steven))"""


#4th exercise
class Shape(object):
    def shrink(self,factor):
        return (self)
    def surface(self):
        return 0
class Circle(Shape):
    def __init__(self,color,radius):
        self.color = color
        self.radius  = radius
    def shrink(self,factor):
        self.radius += factor

class Square(Shape):
    def __init__(self,color,side):
        self.color = color
        self.side  = side
    def surface(self,factor):
        surf = self.side * self.side
        return surf

