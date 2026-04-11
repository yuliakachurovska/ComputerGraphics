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

class Task07Scene(Scene):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        original = Polygon(*SQUARE_VERTICES)
        original.color = "grey"
        original.line_style = "--"
        original.linewidth = 2.0
        self["original"] = original

        self.pivots = [
            ((0.5, 0.5), "red"),     # Центр
            ((0, 1), "orange"),      # Лівий верхній кут
            ((1, 1), "purple"),      # Правий верхній кут
            ((2, 2), "green")        # Точка за межами квадрата
        ]

        for i, (pivot, color) in enumerate(self.pivots):
            poly = Polygon(*SQUARE_VERTICES)
            poly.color = color
            poly.line_style = "-"

            poly.pivot(*pivot)
            poly.show_pivot(True)

            self[f"rotated_{i}"] = poly


if __name__ == '__main__':
    scene = Task07Scene(
        coordinate_rect=(-4, -4, 4, 4),
        title="Завдання 7: Поворот навколо опорної точки",
        grid_show=True,
        base_axis_show=True,
        axis_show=True,
        axis_color=("black", "black"),
        axis_line_style="-"
    )

    R = Mat3x3.rotation(np.radians(60))

    print("Завдання 7: Матриці трансформацій")

    for i, (pivot, color) in enumerate(scene.pivots):
        px, py = pivot

        # Зсуваємо в (0, 0)
        T_to_origin = Mat3x3.translation(-px, -py)
        T_back = Mat3x3.translation(px, py)
        # Зсув -> Поворот -> Зсув назад
        M = T_back * R * T_to_origin

        print(f"\nОпорна точка {pivot} (Колір: {color})")
        print(f"Матриця M:")
        print(M)

        scene[f"rotated_{i}"].transformation = M

    scene.show()