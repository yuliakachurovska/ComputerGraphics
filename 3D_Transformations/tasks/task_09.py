import numpy as np

from src.engine.animation.TrsTransformationAnimation import TrsTransformationAnimation
from src.engine.model.Cube import Cube
from src.engine.scene.AnimatedScene import AnimatedScene
from src.math.Mat4x4 import Mat4x4

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
        coordinate_rect=(-1, -1, -2, 6, 6, 4),
        title="Завдання 9: Зміна перспективи (обертання навколо X та Y з опорною точкою)"
    )

    T1 = Mat4x4.translation(-3, -3, 0)
    Ry = Mat4x4.rotation_y(60, is_radians=False)
    Rx = Mat4x4.rotation_x(30, is_radians=False)
    T2 = Mat4x4.translation(3, 3, 0)
    M_total = T2 * Rx * Ry * T1

    animation_move = TrsTransformationAnimation(
        end=M_total,
        channel=FIGURE_ANIMATED_KEY,
        frames=150,
        repeat=False
    )

    animated_scene.add_animations(animation_move)
    animated_scene.show()