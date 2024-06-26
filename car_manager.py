from turtle import Turtle
import random


COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager():
    def __init__(self):
        self.all_cars = []
        self.move_distance = STARTING_MOVE_DISTANCE
        self.move_increment = MOVE_INCREMENT
           

    def create_car(self):
        random_chance = random.randint(1, 6)
        if random_chance == 1:
            new_car = Turtle()
            new_car.shape('square')
            new_car.shapesize(1, 2)
            new_car.penup()
            new_car.color(random.choice(COLORS))
            y_cor = random.randint(-250, 250)
            new_car.goto(300, y_cor)
            self.all_cars.append(new_car)
        

    def move_cars(self):
        for car in self.all_cars:
            car.backward(self.move_distance)
