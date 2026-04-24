import numpy as np

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
        coordinate_rect=(-2, -2, -8, 4, 4, 4),
        title="Завдання 7: Обертання та масштабування навколо опорної точки"
    )

    T1 = Mat4x4.translation(-1, -2, -3)
    T2 = Mat4x4.translation(1, 2, 3)

    Sz = Mat4x4.scale(1, 1, 3)
    Rz = Mat4x4.rotation_z(30, is_radians=False)
    M_total = T2 * Rz * Sz * T1

    animation_move = TrsTransformationAnimation(
        end=M_total,
        channel=CUBE_ANIMATED_KEY,
        frames=150,
        repeat=False
    )

    animated_scene.add_animations(animation_move)
    animated_scene.show()