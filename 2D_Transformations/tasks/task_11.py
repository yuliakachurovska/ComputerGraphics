import numpy as np
from src.engine.model.Polygon import Polygon
from src.engine.scene.Scene import Scene
from src.math.Mat3x3 import Mat3x3

TRANSFORMED_VERTICES = [
    2.0, 3.4,
    4.9, 4.0,
    4.5, 6.0,
    1.6, 5.4
]

class Task11Scene(Scene):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        global_rect = Polygon(*TRANSFORMED_VERTICES)
        global_rect.color = "red"
        global_rect.line_style = "-"
        global_rect.linewidth = 2.0
        self["global_rect"] = global_rect

        local_rect = Polygon(*TRANSFORMED_VERTICES)
        local_rect.color = "blue"
        local_rect.line_style = "--"
        local_rect.linewidth = 2.0
        self["local_rect"] = local_rect


if __name__ == '__main__':
    scene = Task11Scene(
        coordinate_rect=(-2, -1, 6, 7),
        title="Завдання 11: Відновлення початкового зображення",
        grid_show=True,
        base_axis_show=True,
        axis_show=True,
        axis_color=("black", "black"),
        axis_line_style="-"
    )

    T = Mat3x3(
        2.934, -0.416, 2.000,
        0.624,  1.956, 3.400,
        0,      0,     1
    )

    T_inv = T.inverse()
    scene["local_rect"].transformation = T_inv

    T_np = np.array([
        [2.934, -0.416, 2.000],
        [0.624,  1.956, 3.400],
        [0.0,    0.0,   1.0]
    ])
    T_inv_np = np.linalg.inv(T_np)

    pts = np.array([
        [2.0, 4.9, 4.5, 1.6],
        [3.4, 4.0, 6.0, 5.4],
        [1.0, 1.0, 1.0, 1.0]
    ])

    local_pts = T_inv_np @ pts

    print("Завдання 11: Відновлення зображення")
    print("1. Зворотна матриця T^(-1):")
    print(np.round(T_inv_np, 3))

    print("\n2. Координати локального (початкового) прямокутника:")
    for i in range(4):
        x = local_pts[0, i]
        y = local_pts[1, i]
        print(f"Вершина {i+1}: ({np.round(x, 1)}, {np.round(y, 1)})")
    scene.show()