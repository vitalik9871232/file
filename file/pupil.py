import time

class pupil():
    def __init__(self, surname, name, mark):
        self.surname = surname
        self.name = name
        self.mark = mark

# Список для зберігання обьектів

pupils = []

def print_class(list): # Виводить всіх з списку
    for pupil in list:
        print(pupil.surname, pupil.name, " - ",pupil.mark)
    print("\n")

def print_fine(list):
    for pupil in pupils:
        if pupil.mark == 5:
            print(pupil.surname)
    print("\n")

def find_average(list):
    average = 0
    for pupil in pupils:
        average += int(pupil.mark)
    average /= len(pupils)
    print("Середня оцінка класу: ",average)

with open("pupil.txt", "r", encoding="utf-8") as file:
    for line in file:
        data = line.split(" ")
        pupil2 = pupil(data[0], data[1], data[2])
        pupils.append(pupil2)

print_class(pupils)
print_fine(pupils)
find_average(pupils)