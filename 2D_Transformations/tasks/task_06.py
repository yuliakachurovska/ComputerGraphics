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

class Task06Scene(Scene):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        original = Polygon(*SQUARE_VERTICES)
        original.color = "blue"
        self["original"] = original

        final_order_1 = Polygon(*SQUARE_VERTICES)
        final_order_1.color = "red"
        final_order_1.line_style = "-"
        self["final_order_1"] = final_order_1

        final_order_2 = Polygon(*SQUARE_VERTICES)
        final_order_2.color = "purple"
        final_order_2.line_style = "-"
        self["final_order_2"] = final_order_2


if __name__ == '__main__':
    scene = Task06Scene(
        coordinate_rect=(-10, -2, 6, 12),
        title="Завдання 6: Композиція трьох трансформацій",
        grid_show=True,
        base_axis_show=True,
        axis_show=True,
        axis_color=("black", "black"),
        axis_line_style="-"
    )

    S = Mat3x3.scale(1, 3)
    R = Mat3x3.rotation(np.radians(60))
    T = Mat3x3.translation(2, 3)

    # Розтяг -> Поворот -> Переміщення
    M1 = T * R * S

    # Переміщення -> Розтяг -> Поворот
    M2 = R * S * T

    print("Завдання 6: Композиція трьох трансформацій")
    print("Базові матриці:")
    print("S (Розтяг y:3):")
    print(S)
    print("\nR (Поворот 60°):")
    print("\nT (Переміщення 2, 3):")
    print(T)

    print("\nЗагальні матриці")
    print("M1 (Розтяг -> Поворот -> Переміщення) (червоний):")
    print(M1)
    print("\nM2 (Переміщення -> Розтяг -> Поворот) (фіолетовий):")
    print(M2)

    scene["final_order_1"].transformation = M1
    scene["final_order_2"].transformation = M2
    scene.show()