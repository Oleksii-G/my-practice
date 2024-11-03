'''
import turtle
from tkinter import Button

pero = turtle.Turtle()

# 1 дані
# 2 поведінка
# forward(px) - рухатисаь вперед
# left(deg) - вліво
# right(deg) - вправо
# home() - стартова позиція

pero.speed(1000)


'''
'''
for number in range(200):
    pero.forward(number)
    pero.left(90
'''
'''

btn = Button(text="вперед",command=lambda:pero.forward(10)).pack()
btn2 = Button(text="вліво",command=lambda:pero.left(5)).pack()
btn3 = Button(text="вправо",command=lambda:pero.right(5)).pack()
'''

class Car:
    speed = 0

    def speed_up(self):
        self.speed += 5


my_car = Car()
my_car.speed_up()
print(my_car.speed)

