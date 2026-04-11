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

class Task05Scene(Scene):
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
    scene = Task05Scene(
        coordinate_rect=(-3, -3, 5, 5),
        title="Завдання 5: Переміщення і Масштабування",
        grid_show=True,
        base_axis_show=True,
        axis_show=True,
        axis_color=("black", "black"),
        axis_line_style="-"
    )

    T = Mat3x3.translation(1, -1)
    S = Mat3x3.scale(2, 2)
    M = S * T

    print("Завдання 5: Матриці трансформацій")
    print("Матриця переміщення T (1, -1):")
    print(T)
    print("\nМатриця масштабування S (x:2, y:2):")
    print(S)
    print("\nЗагальна матриця M (S * T):")
    print(M)

    scene["final"].transformation = M
    scene.show()