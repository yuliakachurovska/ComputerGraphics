import math
import random

from src.engine.animation.TrsTransformationAnimation import TrsTransformationAnimation
from src.engine.model.Cube import Cube  # Якщо викладач дав клас Tetrahedron, імпортуй його сюди
from src.engine.scene.AnimatedScene import AnimatedScene
from src.math.Mat4x4 import Mat4x4
from src.math.Vec4 import Vec4

if __name__ == '__main__':
    FIGURE_START_KEY = "fig_start"
    FIGURE_ANIMATED_KEY = "fig_animated"

    class RandomScene(AnimatedScene):
        def __init__(self, **kwargs):
            super().__init__(**kwargs)

            fig_start = Cube(alpha=0.1, color="blue")
            self[FIGURE_START_KEY] = fig_start

            fig_animated = Cube(alpha=0.1, color="grey",
                                line_width=0.8, line_style="-.")
            self[FIGURE_ANIMATED_KEY] = fig_animated

    angle_random = random.uniform(10, 90)
    axis_v = Vec4(random.uniform(0.1, 1), random.uniform(0.1, 1), random.uniform(0.1, 1))
    t_vec = Vec4(random.uniform(-5, 5), random.uniform(-5, 5), random.uniform(-5, 5))

    print("=== ЗГЕНЕРОВАНІ ПАРАМЕТРИ ===")
    print(f"Кут обертання: {angle_random:.2f} градусів")
    print(f"Вісь: ({axis_v.x:.2f}, {axis_v.y:.2f}, {axis_v.z:.2f})")
    print(f"Вектор зсуву: ({t_vec.x:.2f}, {t_vec.y:.2f}, {t_vec.z:.2f})\n")

    phi = math.degrees(math.atan2(axis_v.x, axis_v.z))
    v_z_prime = math.sqrt(axis_v.x**2 + axis_v.z**2)
    theta = math.degrees(math.atan2(axis_v.y, v_z_prime))

    Ry = Mat4x4.rotation_y(-phi, is_radians=False)
    Rx = Mat4x4.rotation_x(theta, is_radians=False)
    Rz = Mat4x4.rotation_z(angle_random, is_radians=False)

    R_final = Ry.transpose() * Rx.transpose() * Rz * Rx * Ry
    T_final = Mat4x4.translation(*t_vec.xyz)
    M_total = T_final * R_final

    print("=== ФІНАЛЬНА МАТРИЦЯ ТРАНСФОРМАЦІЇ ===")
    print(M_total)

    animated_scene = RandomScene(
        coordinate_rect=(-8, -8, -8, 8, 8, 8),
        title="Завдання 5: Рандомізоване обертання і зсув"
    )

    animation_move = TrsTransformationAnimation(
        end=M_total,
        channel=FIGURE_ANIMATED_KEY,
        frames=180,
        repeat=False
    )

    animated_scene.add_animations(animation_move)
    animated_scene.show()