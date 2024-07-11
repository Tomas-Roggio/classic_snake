import turtle
import time
import random

posponer = 0.1

# Puntaje
score = 0
high_score = 0

# Crear la pantalla
wn = turtle.Screen()
wn.title("Snake")
wn.bgcolor("black")
wn.setup(width=600, height=600)

# Esto ayuda a que la pantalla se actualice correctamente
wn.tracer(0)

# Cabeza de serpiente
cabeza = turtle.Turtle()
cabeza.speed(0)
cabeza.shape("square")
cabeza.color("white")
cabeza.penup()
cabeza.goto(0, 0)
cabeza.direction = "stop"

# Comida Serpiente
comida = turtle.Turtle()
comida.speed(0)
comida.shape("circle")
comida.color("red")
comida.penup()
comida.goto(0, 100)

# Cuerpo serpiente
cuerpo = []

# Texto
texto = turtle.Turtle()
texto.speed(0)
texto.color("white")
texto.penup()
texto.hideturtle()
texto.goto(0, 260)
texto.write("Score: 0   High Score: 0", align="center", font=("Courier", 24, "normal"))

# Funciones de movimiento
def arriba():
    if cabeza.direction != "down":
        cabeza.direction = "up"
def abajo():
    if cabeza.direction != "up":
        cabeza.direction = "down"
def izquierda():
    if cabeza.direction != "right":
        cabeza.direction = "left"
def derecha():
    if cabeza.direction != "left":
        cabeza.direction = "right"

def movimiento():
    if cabeza.direction == "up":
        y = cabeza.ycor()
        cabeza.sety(y + 20)

    if cabeza.direction == "down":
        y = cabeza.ycor()
        cabeza.sety(y - 20)

    if cabeza.direction == "right":
        x = cabeza.xcor()
        cabeza.setx(x + 20)

    if cabeza.direction == "left":
        x = cabeza.xcor()
        cabeza.setx(x - 20)

def mover_cuerpo():
    # Mover el cuerpo de la serpiente en orden inverso
    for index in range(len(cuerpo) - 1, 0, -1):
        x = cuerpo[index - 1].xcor()
        y = cuerpo[index - 1].ycor()
        cuerpo[index].goto(x, y)

    # Mover el segmento 0 a la posición de la cabeza
    if len(cuerpo) > 0:
        x = cabeza.xcor()
        y = cabeza.ycor()
        cuerpo[0].goto(x, y)

# Teclado
wn.listen()
wn.onkeypress(arriba, "Up")
wn.onkeypress(abajo, "Down")
wn.onkeypress(izquierda, "Left")
wn.onkeypress(derecha, "Right")

# Main game loop
while True:
    wn.update()

    # Colisiones borde
    if cabeza.xcor() > 290 or cabeza.xcor() < -290 or cabeza.ycor() > 290 or cabeza.ycor() < -290:
        time.sleep(1)
        cabeza.goto(0, 0)
        cabeza.direction = "stop"

        # Esconder los segmentos del cuerpo
        for segmento in cuerpo:
            segmento.goto(1000, 1000)  # Mueve los segmentos fuera de la pantalla
        cuerpo.clear()

        # Reiniciar puntaje
        score = 0
        texto.clear()
        texto.write("Score: {}   High Score: {}".format(score, high_score), align="center", font=("Courier", 24, "normal"))

    # Colisiones cuerpo
    for Pcuerpo in cuerpo:
        if Pcuerpo.distance(cabeza) < 20:
            time.sleep(1)
            cabeza.goto(0,0)
            cabeza.direction = "stop"

            # Esconder los segmentos del cuerpo
            for segmento in cuerpo:
                segmento.goto(1000, 1000)  # Mueve los segmentos fuera de la pantalla
            cuerpo.clear()

            # Reiniciar puntaje
            score = 0
            texto.clear()
            texto.write("Score: {}   High Score: {}".format(score, high_score), align="center", font=("Courier", 24, "normal"))

    # Comportamiento comida
    if cabeza.distance(comida) < 20:
        x = random.randint(-280, 280)
        y = random.randint(-280, 280)
        comida.goto(x, y)

        mas_cuerpo = turtle.Turtle()
        mas_cuerpo.speed(0)
        mas_cuerpo.shape("square")
        mas_cuerpo.color("grey")
        mas_cuerpo.penup()
        cuerpo.append(mas_cuerpo)

        # Actualizar score
        score += 10
        if score > high_score:
            high_score = score

        texto.clear()
        texto.write("Score: {}   High Score: {}".format(score, high_score), align="center", font=("Courier", 24, "normal"))

    mover_cuerpo()
    movimiento()
    time.sleep(posponer)

# Esto mantiene la ventana abierta hasta que se cierre manualmente
turtle.done()
