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

print(total_cost(d,city)) """

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
print(Billy['homework'])



