import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)


player = Player()
manager = CarManager()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(player.move, 'Up')

game_is_on = True


while game_is_on:
    time.sleep(0.1)
    screen.update()

    manager.create_car()
    manager.move_cars()
    
    #Detect collision with car
    for car in manager.all_cars:
        if player.distance(car) < 20:
            game_is_on = False
            scoreboard.game_over()

    #Detect successful run
    if player.is_at_finish():
        scoreboard.increase_score()
        player.go_to_start()
        manager.level_up()
    



screen.exitonclick()