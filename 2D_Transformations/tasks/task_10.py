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

class Task10Scene(Scene):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        original = Polygon(*SQUARE_VERTICES)
        original.color = "grey"
        original.line_style = "--"
        original.linewidth = 2.0
        original.pivot(0.5, 0.5)
        original.show_pivot(True)
        self["original"] = original

        poly1 = Polygon(*SQUARE_VERTICES)
        poly1.color = "red"
        poly1.line_style = "-"
        poly1.pivot(0.5, 0.5)
        poly1.show_pivot(True)
        self["poly1"] = poly1

        poly2 = Polygon(*SQUARE_VERTICES)
        poly2.color = "purple"
        poly2.line_style = "-"
        poly2.pivot(0.5, 0.5)
        poly2.show_pivot(True)
        self["poly2"] = poly2

        poly3 = Polygon(*SQUARE_VERTICES)
        poly3.color = "green"
        poly3.line_style = "-"
        poly3.pivot(0.5, 0.5)
        poly3.show_pivot(True)
        self["poly3"] = poly3


if __name__ == '__main__':
    scene = Task10Scene(
        coordinate_rect=(-4, -3, 6, 5),
        title="Завдання 10: Зсув і масштабування (3 порядки)",
        grid_show=True,
        base_axis_show=True,
        axis_show=True,
        axis_color=("black", "black"),
        axis_line_style="-"
    )

    S = Mat3x3.scale(2, 2)
    R = Mat3x3.rotation(np.radians(30))
    T = Mat3x3.translation(1, -1)

    px, py = 0.5, 0.5
    T_to_origin = Mat3x3.translation(-px, -py)
    T_back = Mat3x3.translation(px, py)

    S_p = T_back * S * T_to_origin
    R_p = T_back * R * T_to_origin

    M1 = T * R_p * S_p
    M2 = R_p * S_p * T
    M3 = R_p * T * S_p

    print("Завдання 10: Загальні матриці трансформацій")
    print("M1 (Масштаб -> Обертання -> Зсув) [Червоний]:")
    print(M1)
    print("\nM2 (Зсув -> Масштаб -> Обертання) [Фіолетовий]:")
    print(M2)
    print("\nM3 (Масштаб -> Зсув -> Обертання) [Зелений]:")
    print(M3)

    scene["poly1"].transformation = M1
    scene["poly2"].transformation = M2
    scene["poly3"].transformation = M3
    scene.show()