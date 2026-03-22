from turtle import *
import time
import colorsys

# Configuración inicial
speed(0)
bgcolor("black")

# MENSAJE SORPRESA 🔥
penup()
goto(0, 0)
color("white")
write("Tengo algo para ti...", align="center", font=("Arial", 20, "bold"))

time.sleep(2.5)

# Limpiar pantalla
clear()
bgcolor("black")

# Título
penup()
goto(-120, 250)
color("white")
write("flores amarillas", font=("Arial", 16, "normal"))

# Tallo
penup()
goto(0, -100)
pendown()
color("green")
begin_fill()
right(90)
forward(400)
left(90)
forward(20)
left(90)
forward(400)
left(90)
forward(20)
end_fill()

# FLOR 🌼
penup()
goto(0, 0)
setheading(0)
pendown()

for i in range(18):
    for j in range(10):
        color("yellow")
        right(90)
        circle(120 - j*4, 90)
        left(90)
        circle(120 - j*4, 90)
    
    left(20)

# CENTRO 🌟
penup()
goto(0, -50)
setheading(0)
pendown()

for i in range(50, 0, -5):
    r, g, b = colorsys.hsv_to_rgb(0.1, 1, i/50)
    color(r, g, b)

    begin_fill()
    circle(i)
    end_fill()

# MENSAJE FINAL 💛
penup()
goto(0, 200)
color("white")
write("Para ti Cereza, Te chelo muchote 💛", align="center", font=("Arial", 16, "bold"))

done()