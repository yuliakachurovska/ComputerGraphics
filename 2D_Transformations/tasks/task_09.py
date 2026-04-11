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

class Task09Scene(Scene):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        original = Polygon(*SQUARE_VERTICES)
        original.color = "grey"
        original.line_style = "--"
        original.linewidth = 2.0
        original.pivot(1, 1)
        original.show_pivot(True)
        self["original"] = original

        poly1 = Polygon(*SQUARE_VERTICES)
        poly1.color = "red"
        poly1.line_style = "-"
        poly1.pivot(1, 1)
        poly1.show_pivot(True)
        self["poly1"] = poly1

        poly2 = Polygon(*SQUARE_VERTICES)
        poly2.color = "purple"
        poly2.line_style = "-"
        poly2.pivot(1, 1)
        poly2.show_pivot(True)
        self["poly2"] = poly2


if __name__ == '__main__':
    scene = Task09Scene(
        coordinate_rect=(-2, -5, 7, 3),
        title="Завдання 9: Розтяг і переміщення з pivot (1,1)",
        grid_show=True,
        base_axis_show=True,
        axis_show=True,
        axis_color=("black", "black"),
        axis_line_style="-"
    )

    S = Mat3x3.scale(2, 1)
    T = Mat3x3.translation(3, -2)

    px, py = 1, 1
    T_to_origin = Mat3x3.translation(-px, -py)
    T_back = Mat3x3.translation(px, py)

    S_pivot = T_back * S * T_to_origin
    M1 = T * S_pivot
    M2 = S_pivot * T

    print("Завдання 9: Розтяг і переміщення з опорною точкою")
    print("M1 (Розтяг -> Переміщення) [Червоний]:")
    print(M1)
    print("\nM2 (Переміщення -> Розтяг) [Фіолетовий]:")
    print(M2)

    scene["poly1"].transformation = M1
    scene["poly2"].transformation = M2
    scene.show()