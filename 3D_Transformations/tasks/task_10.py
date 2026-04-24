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
        coordinate_rect=(-5, -1, -1, 3, 6, 5),
        title="Завдання 10: Комплексна трансформація"
    )

    T1 = Mat4x4.translation(-1, -1, -1)
    T2 = Mat4x4.translation(1, 1, 1)
    Sx = Mat4x4.scale(2, 1, 1)
    Ry = Mat4x4.rotation_y(45, is_radians=False)
    T3 = Mat4x4.translation(-3, 4, 2)
    M_total = T3 * T2 * Ry * Sx * T1

    animation_move = TrsTransformationAnimation(
        end=M_total,
        channel=CUBE_ANIMATED_KEY,
        frames=150,
        repeat=False
    )

    animated_scene.add_animations(animation_move)
    animated_scene.show()