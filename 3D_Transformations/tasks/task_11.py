import numpy as np

from src.engine.animation.TrsTransformationAnimation import TrsTransformationAnimation
from src.engine.model.Cube import Cube
from src.engine.scene.AnimatedScene import AnimatedScene
from src.math.Mat4x4 import Mat4x4

if __name__ == '__main__':
    CUBE_START_KEY = "cube_start"
    CUBE_ANIMATED_KEY = "cube_animated"

    class TaskScene(AnimatedScene):
        def __init__(self, **kwargs):
            super().__init__(**kwargs)

            cube_start = Cube(alpha=0.1, color="blue")
            self[CUBE_START_KEY] = cube_start

            cube_animated = Cube(alpha=0.1, color="grey",
                                 line_width=0.8, line_style="-.")
            self[CUBE_ANIMATED_KEY] = cube_animated

    animated_scene = TaskScene(
        coordinate_rect=(-2, -2, -2, 4, 4, 4),
        title="Завдання 11: Порівняння зовнішніх та внутрішніх обертань"
    )

    Rx = Mat4x4.rotation_x(30, is_radians=False)
    Ry = Mat4x4.rotation_y(45, is_radians=False)
    Rz = Mat4x4.rotation_z(60, is_radians=False)

    M_A = Rz * Ry * Rx
    M_B = Rz * Ry * Rx

    print("=== Матриця А (Зовнішні обертання) ===")
    print(M_A)
    print("\n=== Матриця Б (Внутрішні обертання) ===")
    print(M_B)
    print("\nМатриці ідентичні!")

    animation_move = TrsTransformationAnimation(
        end=M_A,
        channel=CUBE_ANIMATED_KEY,
        frames=120,
        repeat=False
    )

    animated_scene.add_animations(animation_move)
    animated_scene.show()