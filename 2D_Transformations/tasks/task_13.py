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

class Task13Scene(Scene):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        original = Polygon(*SQUARE_VERTICES)
        original.color = "blue"
        original.line_style = "--"
        original.linewidth = 2.0
        self["original"] = original

        final = Polygon(*SQUARE_VERTICES)
        final.color = "red"
        final.line_style = "-"
        self["final"] = final


if __name__ == '__main__':
    scene = Task13Scene(
        coordinate_rect=(-2, -1, 5, 6),
        title="Завдання 13: Розкладання матриці",
        grid_show=True,
        base_axis_show=True,
        axis_show=True,
        axis_color=("black", "black"),
        axis_line_style="-"
    )

    T_given = Mat3x3(
        1.414, -2.121, 1,
        1.414,  2.121, 1,
        0,      0,     1
    )

    scale_matrix = Mat3x3.scale(2, 3)
    rotate_matrix = Mat3x3.rotation(np.radians(45))
    translate_matrix = Mat3x3.translation(1, 1)
    T_calculated = translate_matrix * rotate_matrix * scale_matrix

    print("Завдання 13: Розкладання матриці")
    print("1. Задана матриця T:")
    print(T_given)
    print("\n2. Знайдені компоненти:")
    print(f"Розтяг (Scale) - sx=2, sy=3:\n{scale_matrix}")
    print(f"\nПоворот (Rotate) - 45 градусів:\n{np.round(rotate_matrix.get_matrix(), 3) if hasattr(rotate_matrix, 'get_matrix') else rotate_matrix}")
    print(f"\nПереміщення (Translate) - tx=1, ty=1:\n{translate_matrix}")
    print("\n3. Перевірка (множимо знайдені матриці T * R * S):")
    print(np.round(T_calculated.get_matrix(), 3) if hasattr(T_calculated, 'get_matrix') else T_calculated)

    scene["final"].transformation = T_given
    scene.show()