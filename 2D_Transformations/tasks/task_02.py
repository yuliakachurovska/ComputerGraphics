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

class Task02Scene(Scene):
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
    scene = Task02Scene(
        coordinate_rect=(-3, -3, 5, 5),
        title="Завдання 2: Розтяг і Поворот",
        grid_show=True,
        base_axis_show=True,
        axis_show=True,
        axis_color=("black", "black"),
        axis_line_style="-"
    )

    S = Mat3x3.scale(2, 1)
    R = Mat3x3.rotation(np.radians(45))
    M = R * S

    print("Завдання 2: Матриці трансформацій")
    print("Матриця розтягу S (x:2, y:1):")
    print(S)
    print("\nМатриця повороту R (45 градусів):")
    print(R)
    print("\nЗагальна матриця M (R * S):")
    print(M)

    scene["final"].transformation = M
    scene.show()