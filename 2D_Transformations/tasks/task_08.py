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

class Task08Scene(Scene):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        original = Polygon(*SQUARE_VERTICES)
        original.color = "grey"
        original.line_style = "--"
        original.linewidth = 2.0
        self["original"] = original

        self.pivots = [
            ((0.5, 0.5), "red"),
            ((0, 1), "orange"),
            ((1, 1), "purple"),
            ((2, 2), "green")
        ]

        for i, (pivot, color) in enumerate(self.pivots):
            poly = Polygon(*SQUARE_VERTICES)
            poly.color = color
            poly.line_style = "-"

            poly.pivot(*pivot)
            poly.show_pivot(True)
            self[f"scaled_{i}"] = poly


if __name__ == '__main__':
    scene = Task08Scene(
        coordinate_rect=(-3, -5, 4, 5),
        title="Завдання 8: Розтяг навколо опорної точки",
        grid_show=True,
        base_axis_show=True,
        axis_show=True,
        axis_color=("black", "black"),
        axis_line_style="-"
    )

    S = Mat3x3.scale(2, 3)

    print("Завдання 8: Матриці трансформацій")

    for i, (pivot, color) in enumerate(scene.pivots):
        px, py = pivot
        T_to_origin = Mat3x3.translation(-px, -py)
        T_back = Mat3x3.translation(px, py)
        M = T_back * S * T_to_origin

        print(f"\nОпорна точка {pivot} (Колір: {color})")
        print(f"Загальна матриця M:")
        print(M)

        scene[f"scaled_{i}"].transformation = M

    scene.show()