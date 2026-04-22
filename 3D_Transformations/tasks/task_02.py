import numpy as np
import math

from src.engine.animation.TrsTransformationAnimation import TrsTransformationAnimation
from src.engine.model.Cube import Cube
from src.engine.scene.AnimatedScene import AnimatedScene
from src.math.Mat4x4 import Mat4x4
from src.math.Vec4 import Vec4

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
        coordinate_rect=(-4, -1, -1, 4, 4, 6),
        title="Завдання 2: Розтяг, обертання (Euler) і зсув"
    )

    # Розтяг
    S = Mat4x4.scale(2.0, 0.5, 1.0)

    # Обертання
    Rx = Mat4x4.rotation_x(30, is_radians=False)
    Ry = Mat4x4.rotation_y(45, is_radians=False)
    Rz = Mat4x4.rotation_z(60, is_radians=False)

    # Зсув
    T = Mat4x4.translation(-3, 2, 5)

    # Композиція: S -> Rx -> Ry -> Rz -> T (множимо справа наліво)
    M_total = T * Rz * Ry * Rx * S

    animation_move = TrsTransformationAnimation(
        end=M_total,
        channel=CUBE_ANIMATED_KEY,
        frames=150,
        repeat=False
    )

    animated_scene.add_animations(animation_move)
    animated_scene.show()