import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()


screen.setup(width=600, height=600)
screen.tracer(0)
player = Player()

cars = []
scoreboard = Scoreboard()
screen.listen()
screen.onkeypress(player.move, "Up")

loop_counter = 0
game_is_on = True
while game_is_on:
    time.sleep(0.05)
    screen.update()
    loop_counter += 1

    if loop_counter % 6 == 0:
        new_car = CarManager()
        cars.append(new_car)

    for car in cars:
        if car.ycor() - 20 < player.ycor() < car.ycor() + 20 and player.distance(car) < 20:
            game_is_on = False
            scoreboard.gameover()
            break
        car.car_move(scoreboard.level)

    if player.finish == player.ycor():
        player.reset_player()
        scoreboard.level += 1
        scoreboard.show_level()

screen.exitonclick()
