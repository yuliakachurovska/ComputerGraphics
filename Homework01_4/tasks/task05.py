import numpy as np
from src.engine.animation.TrsTransformationAnimation import TrsTransformationAnimation
from src.engine.model.Cube import Cube
from src.engine.scene.AnimatedScene import AnimatedScene
from src.math.Mat4x4 import Mat4x4

def main():
    sqrt3 = np.sqrt(3)

    R_4x4 = Mat4x4(
        1/sqrt3,  1/sqrt3,           1/sqrt3,           0,
        -1/sqrt3, (sqrt3+1)/(2*sqrt3), (1-sqrt3)/(2*sqrt3), 0,
        -1/sqrt3, (1-sqrt3)/(2*sqrt3), (sqrt3+1)/(2*sqrt3), 0,
        0,                   0,                   0, 1
    )

    print("ЗАВДАННЯ 5: КВАТЕРНІОН ДЛЯ ПОВОРОТУ (1,1,1) В НАПРЯМОК (1,0,0)")
    print("Матриця повороту R:\n", R_4x4)

    class QuaternionScene(AnimatedScene):
        def __init__(self, **kwargs):
            super().__init__(**kwargs)
            cube = Cube(alpha=0.7, color="green")
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