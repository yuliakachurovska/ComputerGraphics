import numpy as np

from src.engine.animation.TrsTransformationAnimation import TrsTransformationAnimation
from src.engine.model.Cube import Cube
from src.engine.scene.AnimatedScene import AnimatedScene
from src.math.Mat4x4 import Mat4x4
from src.math.Vec4 import Vec4

def main():
    angle_x = np.radians(20)
    angle_y = np.radians(35)
    angle_z = np.radians(50)

    Rx = Mat4x4.rotation_x(angle_x)
    Ry = Mat4x4.rotation_y(angle_y)
    Rz = Mat4x4.rotation_z(angle_z)

    R = Rx * Ry * Rz
    T = Mat4x4.translation(1.0, 3.0, -2.0)
    M_final = T * R

    print("МАТРИЦІ ТРАНСФОРМАЦІЙ")
    print("Матриця повороту R (Rx * Ry * Rz):\n", R)
    print("\nМатриця переміщення T:\n", T)
    print("\nФінальна матриця M (T * R):\n", M_final)

    print("\nКООРДИНАТИ ДІАГОНАЛІ (0,0,0) - (1,1,1)")
    p_start = Vec4(0, 0, 0, 1)
    p_end = Vec4(1, 1, 1, 1)

    print(f"Після повороту ZYX: (0,0,0) -> {R * p_start}, (1,1,1) -> {R * p_end}")
    print(f"Фінальні координати: (0,0,0) -> {M_final * p_start}, (1,1,1) -> {M_final * p_end}")

    class Task02Scene(AnimatedScene):
        def __init__(self, **kwargs):
            super().__init__(**kwargs)

            cube_initial = Cube(alpha=0.5, color="blue")
            cube_initial.show_local_frame()
            self["cube_initial"] = cube_initial

            cube_final = Cube(alpha=0.8, color="red")
            self["cube_final"] = cube_final

    scene = Task02Scene()

    animation = TrsTransformationAnimation(
        end=M_final,
        channel="cube_final",
        frames=100
    )

    scene.add_animations(animation)
    scene.show()

if __name__ == '__main__':
    main()