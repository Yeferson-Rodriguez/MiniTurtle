# Mini-Turtle Package

Paquete Python para dibujar con turtle usando una arquitectura modular.

## 📦 Instalación
```bash
# Clonar o copiar el proyecto
# Instalar en modo desarrollo
pip install -e .
```

## 🚀 Uso
```python
from mini_turtle import adelante, abajo, reiniciar

# Mover hacia adelante
adelante(100)

# Mover hacia abajo
abajo(50)

# Resetear posición
reiniciar()
```

## 📂 Estructura del Proyecto
```
mini_turtle_task/
├── mini_turtle/              # Paquete principal
│   ├── __init__.py          # Interfaz pública
│   └── drawer_logic.py      # Lógica y estado global
├── main.py                  # Script de prueba
├── README.md               # Documentación
└── pyproject.toml          # Metadata (opcional)
```

## 🎯 Características

- ✅ Separación de lógica e interfaz
- ✅ Variable global para tracking de posición
- ✅ Funciones reutilizables
- ✅ Arquitectura de paquete profesional

## 📝 Funciones Disponibles

- `adelante(distancia)` - Mueve la tortuga hacia adelante
- `abajo(distancia)` - Mueve la tortuga hacia abajo
- `reiniciar()` - Reset de posición a 0

## 👨‍💻 Autor

Yeferson David Rodriguez Gomez
