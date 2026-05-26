import numpy as np
from src.engine.animation.TrsTransformationAnimation import TrsTransformationAnimation
from src.engine.model.Cube import Cube
from src.engine.scene.AnimatedScene import AnimatedScene
from src.math.Mat4x4 import Mat4x4

def main():
    R_4x4 = Mat4x4(
        2/3, -2/3, -1/3, 0,
        1/3,  2/3, -2/3, 0,
        2/3,  1/3,  2/3, 0,
        0,    0,    0, 1
    )

    print("ЗАВДАННЯ 4: КВАТЕРНІОН ДЛЯ ПОВОРОТУ (1,1,0) В (0,1,1)")
    print("Матриця повороту R:\n", R_4x4)

    class QuaternionScene(AnimatedScene):
        def __init__(self, **kwargs):
            super().__init__(**kwargs)
            cube = Cube(alpha=0.7, color="yellow")
            cube.show_local_frame()
            self["cube"] = cube

    scene = QuaternionScene()

    animation = TrsTransformationAnimation(
        end=R_4x4,
        channel="cube",
        frames=100
    )

    scene.add_animations(animation)
    scene.show()

if __name__ == '__main__':
    main()