import turtle

# Variable global para mantener el estado
posicion_x = 0


def adelante(distancia):
    """Adelante"""
    global posicion_x
    turtle.forward(distancia)
    posicion_x += distancia
    print(f"Posición X actual: {posicion_x}")


def abajo(distancia):
    """Abajo"""
    turtle.right(90)
    turtle.forward(distancia)
    turtle.left(90)


def reiniciar():
    """Reinicia"""
    global posicion_x
    posicion_x = 0
    turtle.reset()
    print("Posición reseteada a 0")