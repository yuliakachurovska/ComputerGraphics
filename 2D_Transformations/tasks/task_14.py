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

class Task14Scene(Scene):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        original = Polygon(*SQUARE_VERTICES)
        original.color = "grey"
        original.line_style = "--"
        original.linewidth = 2.0
        original.pivot(1, 1)
        original.show_pivot(True)
        self["original"] = original

        final = Polygon(*SQUARE_VERTICES)
        final.color = "green"
        final.line_style = "-"
        final.linewidth = 2.0
        self["final"] = final


if __name__ == '__main__':
    scene = Task14Scene(
        coordinate_rect=(-1, -5, 8, 3),
        title="Завдання 14: Розкладання з опорною точкою (1,1)",
        grid_show=True,
        base_axis_show=True,
        axis_show=True,
        axis_color=("black", "black"),
        axis_line_style="-"
    )

    T_given = Mat3x3(
        1.732, -1.000,  5.0,
        1.000,  1.732, -3.0,
        0.0,    0.0,    1.0
    )

    S = Mat3x3.scale(2, 2)
    R = Mat3x3.rotation(np.radians(30))
    T_to_origin = Mat3x3.translation(-1, -1)
    T_back = Mat3x3.translation(1, 1)
    Tr = Mat3x3.translation(4.732, -1.268)
    T_calculated = Tr * T_back * R * S * T_to_origin

    print("--- Завдання 14: Фінальний бос! ---")
    print("1. Задана матриця T:")
    print(T_given)

    print("\n2. Знайдені компоненти:")
    print("   - Масштаб: по обох осях у 2 рази")
    print("   - Поворот: 30 градусів")
    print("   - Опорна точка (pivot): (1, 1)")
    print("   - Фінальне переміщення: вектор (4.732, -1.268)")

    print("\n3. Перевірка результату (перемножуємо знайдені матриці):")
    print(np.round(T_calculated.get_matrix(), 3) if hasattr(T_calculated, 'get_matrix') else T_calculated)
    print("\nВИСНОВОК: Розрахована матриця повністю співпадає з заданою!")

    scene["final"].transformation = T_given
    scene.show()