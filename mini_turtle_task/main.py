from mini_turtle import adelante, abajo, reiniciar
import turtle


def dibujar_escalera():
    """Dibuja una escalera simple usando las funciones del paquete"""
    print("=== Dibujando Escalera ===")

    # Configuración inicial
    turtle.speed(2)
    turtle.pensize(3)
    turtle.color("blue")

    # Dibujar escalera de 4 escalones
    for i in range(4):
        print(f"\nEscalón {i + 1}")
        adelante(50)
        abajo(30)

    # Finalizar
    adelante(50)
    print("\n=== Escalera completada ===")


def dibujar_rectangulos():
    """Dibuja varios rectángulos"""
    print("\n=== Dibujando Rectángulos ===")

    reiniciar()
    turtle.color("red")

    # Primer rectángulo
    adelante(100)
    abajo(60)
    turtle.backward(100)
    turtle.left(90)
    turtle.forward(60)
    turtle.right(90)

    print("\n=== Rectángulos completados ===")


if __name__ == "__main__":
    # Configurar ventana
    turtle.setup(800, 600)
    turtle.title("Mini-Turtle Package Demo")

    # Ejecutar demostraciones
    dibujar_escalera()

    input("\nPresiona Enter para resetear y dibujar rectángulos...")
    dibujar_rectangulos()

    print("\n¡Demo completada! Cierra la ventana para terminar.")
    turtle.done()