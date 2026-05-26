import numpy as np

from src.engine.animation.TrsTransformationAnimation import TrsTransformationAnimation
from src.engine.model.Cube import Cube
from src.engine.scene.AnimatedScene import AnimatedScene
from src.math.Mat4x4 import Mat4x4
from src.math.Vec4 import Vec4

def main():
    S = Mat4x4.scale(2.0, 0.5, 1.0)

    angle_x, angle_y, angle_z = np.radians(30), np.radians(45), np.radians(60)
    Rx = Mat4x4.rotation_x(angle_x)
    Ry = Mat4x4.rotation_y(angle_y)
    Rz = Mat4x4.rotation_z(angle_z)

    R = Rz * Ry * Rx
    T = Mat4x4.translation(-3.0, 2.0, 5.0)
    M_final = T * R * S

    print("МАТРИЦІ ТРАНСФОРМАЦІЙ")
    print("Матриця розтягу S:\n", S)
    print("\nМатриця повороту R (Rz * Ry * Rx):\n", R)
    print("\nМатриця переміщення T:\n", T)
    print("\nФінальна матриця M (T * R * S):\n", M_final)

    print("\nКООРДИНАТИ ДІАГОНАЛІ (0,0,0) - (1,1,1)")
    p_start = Vec4(0, 0, 0, 1)
    p_end = Vec4(1, 1, 1, 1)

    print(f"Після розтягу: (0,0,0) -> {S * p_start}, (1,1,1) -> {S * p_end}")
    print(f"Після повороту: (0,0,0) -> {RS * p_start}, (1,1,1) -> {RS * p_end}")
    print(f"Фінальні координати: (0,0,0) -> {M_final * p_start}, (1,1,1) -> {M_final * p_end}")

    class Task00Scene(AnimatedScene):
        def __init__(self, **kwargs):
            super().__init__(**kwargs)

            cube_initial = Cube(alpha=0.5, color="blue")
            cube_initial.show_local_frame()
            self["cube_initial"] = cube_initial

            cube_final = Cube(alpha=0.8, color="red")
            self["cube_final"] = cube_final

    scene = Task00Scene()

    animation = TrsTransformationAnimation(
        end=M_final,
        channel="cube_final",
        frames=100
    )

    scene.add_animations(animation)
    scene.show()

if __name__ == '__main__':
    main()