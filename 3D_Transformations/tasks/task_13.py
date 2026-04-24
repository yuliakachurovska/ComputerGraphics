import numpy as np

from src.engine.animation.TrsTransformationAnimation import TrsTransformationAnimation
from src.engine.model.Cube import Cube # Якщо є Tetrahedron, заміни тут
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
        coordinate_rect=(-1, -1, -1, 4, 4, 4),
        title="Завдання 13: Внутрішні обертання (Локальні осі Z -> X -> Y)"
    )

    # Обертання навколо локальної Z
    R1_loc = Mat4x4.rotation_z(45, is_radians=False)

    # Зсув вздовж оновленої локальної X
    T2_loc = Mat4x4.translation(2, 0, 0)

    # Обертання навколо нової локальної Y
    R3_loc = Mat4x4.rotation_y(30, is_radians=False)

    M_total = R1_loc * T2_loc * R3_loc

    animation_move = TrsTransformationAnimation(
        end=M_total,
        channel=FIGURE_ANIMATED_KEY,
        frames=180,
        repeat=False
    )

    animated_scene.add_animations(animation_move)
    animated_scene.show()