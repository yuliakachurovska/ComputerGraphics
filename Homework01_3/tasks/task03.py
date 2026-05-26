import numpy as np

from src.engine.animation.TrsTransformationAnimation import TrsTransformationAnimation
from src.engine.model.Cube import Cube
from src.engine.scene.AnimatedScene import AnimatedScene
from src.math.Mat4x4 import Mat4x4
from src.math.Vec4 import Vec4

def main():
    alpha = np.radians(45)
    beta = np.radians(30)
    gamma = np.radians(60)

    Rx = Mat4x4.rotation_x(alpha)
    Ry = Mat4x4.rotation_y(beta)
    Rz = Mat4x4.rotation_z(gamma)

    M_xyz = Rz * Ry * Rx
    M_zyx = Rx * Ry * Rz

    print("ЗАВДАННЯ 3: МАТРИЦІ ТРАНСФОРМАЦІЙ")
    print("1. Матриця M_xyz (Конвенція XYZ):\n", M_xyz)
    print("\n2. Матриця M_zyx (Конвенція ZYX):\n", M_zyx)

    p_start = Vec4(0, 0, 0, 1)
    p_end = Vec4(1, 1, 1, 1)

    print("\nКООРДИНАТИ ДІАГОНАЛІ (0,0,0) - (1,1,1)")
    print(f"XYZ фінал: (0,0,0) -> {M_xyz * p_start}, (1,1,1) -> {M_xyz * p_end}")
    print(f"ZYX фінал: (0,0,0) -> {M_zyx * p_start}, (1,1,1) -> {M_zyx * p_end}")

    class Task03Scene(AnimatedScene):
        def __init__(self, **kwargs):
            super().__init__(**kwargs)

            cube_xyz = Cube(alpha=0.7, color="red")
            self["cube_xyz"] = cube_xyz

            cube_zyx = Cube(alpha=0.7, color="green")
            self["cube_zyx"] = cube_zyx

    scene = Task03Scene()

    anim_xyz = TrsTransformationAnimation(end=M_xyz, channel="cube_xyz", frames=100)
    anim_zyx = TrsTransformationAnimation(end=M_zyx, channel="cube_zyx", frames=100)

    scene.add_animations(anim_xyz, anim_zyx)
    scene.show()

if __name__ == '__main__':
    main()