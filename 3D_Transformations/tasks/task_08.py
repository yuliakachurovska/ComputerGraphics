import numpy as np
import math

from src.engine.animation.TrsTransformationAnimation import TrsTransformationAnimation
from src.engine.model.Cube import Cube  # Якщо є клас Triangle, імпортуй його
from src.engine.scene.AnimatedScene import AnimatedScene
from src.math.Mat4x4 import Mat4x4
from src.math.Vec4 import Vec4

if __name__ == '__main__':
    FIGURE_START_KEY = "fig_start"
    FIGURE_ANIMATED_KEY = "fig_animated"

    class TaskScene(AnimatedScene):
        def __init__(self, **kwargs):
            super().__init__(**kwargs)

            fig_start = Cube(alpha=0.1, color="blue")
            self[FIGURE_START_KEY] = fig_start

            fig_animated = Cube(alpha=0.1, color="grey",
                                line_width=0.8, line_style="-.")
            self[FIGURE_ANIMATED_KEY] = fig_animated

    animated_scene = TaskScene(
        coordinate_rect=(-2, -5, -2, 8, 8, 12),
        title="Завдання 8: Обертання навколо осі, що не проходить через нуль"
    )

    T1 = Mat4x4.translation(-2, -3, -4)

    axis_v = Vec4(1, 1, 1)
    angle_arb = 90

    phi = math.degrees(math.atan2(axis_v.x, axis_v.z))
    v_z_prime = math.sqrt(axis_v.x**2 + axis_v.z**2)
    theta = math.degrees(math.atan2(axis_v.y, v_z_prime))

    Ry = Mat4x4.rotation_y(-phi, is_radians=False)
    Rx = Mat4x4.rotation_x(theta, is_radians=False)
    Rz = Mat4x4.rotation_z(angle_arb, is_radians=False)

    R_arb = Ry.transpose() * Rx.transpose() * Rz * Rx * Ry
    T2 = Mat4x4.translation(2, 3, 4)

    T3 = Mat4x4.translation(0, -3, 2)
    M_total = T3 * T2 * R_arb * T1

    animation_move = TrsTransformationAnimation(
        end=M_total,
        channel=FIGURE_ANIMATED_KEY,
        frames=180,
        repeat=False
    )

    animated_scene.add_animations(animation_move)
    animated_scene.show()