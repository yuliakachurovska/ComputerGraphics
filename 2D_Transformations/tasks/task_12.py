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

class Task12Scene(Scene):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        original = Polygon(*SQUARE_VERTICES)
        original.color = "blue"
        original.line_style = "--"
        original.linewidth = 2.0
        self["original"] = original

        transformed = Polygon(*SQUARE_VERTICES)
        transformed.color = "red"
        transformed.line_style = "-"
        self["transformed"] = transformed

if __name__ == '__main__':
    scene = Task12Scene(
        coordinate_rect=(-1, -1, 6, 6),
        title="Завдання 12: Розкладання матриці",
        grid_show=True,
        base_axis_show=True,
        axis_show=True,
        axis_color=("black", "black"),
        axis_line_style="-"
    )

    T = Mat3x3(
        0.866, 0.5,   4,
        0.5,   0.866, 3,
        0,     0,     1
    )

    scene["transformed"].transformation = T

    print("Завдання 12: Аналіз матриці")
    print("Задана матриця T:")
    print(T)
    print("\nАналіз розкладання:")
    print("1. Вектор переміщення: легко дістати з останнього стовпця (4, 3).")
    print("2. Перевіряємо лінійну частину (лівий верхній блок 2x2).")
    print("   Якщо матриця складається лише з розтягу по осях та повороту,")
    print("   то її вектори-стовпці мають бути ортогональними.")
    print("   Стовпець 1: v1 = (0.866, 0.5)")
    print("   Стовпець 2: v2 = (0.5, 0.866)")
    print("   Скалярний добуток v1 * v2 = 0.866*0.5 + 0.5*0.866 = 0.866")
    print("\nВИСНОВОК:")
    print("Оскільки скалярний добуток НЕ дорівнює нулю, ці вектори не перпендикулярні.")
    print("Розкласти матрицю T на базові Scale, Rotate і Translate неможливо,")
    print("оскільки вона містить деформацію зсуву/скосу.")

    scene.show()