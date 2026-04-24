import numpy as np
import math

from src.engine.animation.TrsTransformationAnimation import TrsTransformationAnimation
from src.engine.model.Cube import Cube
from src.engine.scene.AnimatedScene import AnimatedScene
from src.math.Mat4x4 import Mat4x4

if __name__ == '__main__':
    CUBE_START_KEY = "cube_start"
    CUBE_ANIMATED_KEY = "cube_animated"

    class CubeScene(AnimatedScene):
        def __init__(self, **kwargs):
            super().__init__(**kwargs)

            cube_start = Cube(alpha=0.1, color="blue")
            self[CUBE_START_KEY] = cube_start

            cube_animated = Cube(alpha=0.1, color="grey",
                                 line_width=0.8, line_style="-.")
            self[CUBE_ANIMATED_KEY] = cube_animated

    animated_scene = CubeScene(
        coordinate_rect=(-2, -1, -3, 4, 5, 3),
        title="Завдання 4: Поворот у системі кутів Ейлера ZYX"
    )

    Rx = Mat4x4.rotation_x(50, is_radians=False)
    Ry = Mat4x4.rotation_y(35, is_radians=False)
    Rz = Mat4x4.rotation_z(20, is_radians=False)

    T_final = Mat4x4.translation(1, 3, -2)

    M_total = T_final * Rz * Ry * Rx

    animation_move = TrsTransformationAnimation(
        end=M_total,
        channel=CUBE_ANIMATED_KEY,
        frames=150,
        repeat=False
    )

    animated_scene.add_animations(animation_move)
    animated_scene.show()