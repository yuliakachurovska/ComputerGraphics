import numpy as np

from src.engine.animation.TrsTransformationAnimation import TrsTransformationAnimation
from src.engine.model.Cube import Cube
from src.engine.scene.AnimatedScene import AnimatedScene
from src.math.Mat4x4 import Mat4x4

def main():
    Rx1 = Mat4x4.rotation_x(np.radians(45))
    Ry1 = Mat4x4.rotation_y(np.radians(90))
    Rz1 = Mat4x4.rotation_z(0)

    M1 = Rx1 * Ry1 * Rz1

    Rx2 = Mat4x4.rotation_x(0)
    Ry2 = Mat4x4.rotation_y(np.radians(90))
    Rz2 = Mat4x4.rotation_z(np.radians(-45))

    M2 = Rx2 * Ry2 * Rz2

    print("GIMBAL LOCK")
    print("Матриця 1 (X=45, Y=90, Z=0):\n", M1)
    print("\nМатриця 2 (X=0, Y=90, Z=-45):\n", M2)
    print("Матриці ідентичні, осі X та Z 'злилися' в одну!")

    class GimbalLockScene(AnimatedScene):
        def __init__(self, **kwargs):
            super().__init__(**kwargs)

            cube1 = Cube(alpha=0.6, color="red")
            self["cube1"] = cube1

            cube2 = Cube(alpha=0.6, color="blue")
            cube2.transformation = Mat4x4.scale(0.95, 0.95, 0.95) # Зменшуємо синій куб
            self["cube2"] = cube2

    scene = GimbalLockScene()

    anim1 = TrsTransformationAnimation(end=M1, channel="cube1", frames=100)
    anim2 = TrsTransformationAnimation(end=M2, channel="cube2", frames=100)

    scene.add_animations(anim1, anim2)
    scene.show()

if __name__ == '__main__':
    main()