class Cars:
    make = "Honda"
    def __init__(self, color, year):
        self.color = color
        self.year = year
    #print("You created a new car!")

car_1 = Cars("Blue", 2020)
print(car_1.color)
car_2 = Cars("Red", 2026)
print(car_2.color)
print(car_2.make)
car_2.make = "Lexus"
print(car_2.make)