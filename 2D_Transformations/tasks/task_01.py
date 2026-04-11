import numpy as np
from src.engine.model.Polygon import Polygon
from src.engine.scene.Scene import Scene
from src.math.Mat3x3 import Mat3x3

SQUARE_VERTICES = [
    0, 0,
    1, 0,
    1, 1,
    0, 1
]

class Task01Scene(Scene):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        original = Polygon(*SQUARE_VERTICES)
        original.color = "blue"
        self["original"] = original

        final = Polygon(*SQUARE_VERTICES)
        final.color = "red"
        final.line_style = "-"
        self["final"] = final


if __name__ == '__main__':
    scene = Task01Scene(
        coordinate_rect=(-3, -3, 5, 5),
        title="Завдання 1: Поворот і Переміщення",
        grid_show=True,
        base_axis_show=True,
        axis_show=True,
        axis_color=("black", "black"),
        axis_line_style="-"
    )

    R = Mat3x3.rotation(np.radians(30))
    T = Mat3x3.translation(2, 3)
    M = T * R

    print("Завдання 1: Матриці трансформацій")
    print("Матриця повороту R (30 градусів):")
    print(R)
    print("\nМатриця переміщення T (2, 3):")
    print(T)
    print("\nЗагальна матриця M (T * R):")
    print(M)

    scene["final"].transformation = M
    scene.show()