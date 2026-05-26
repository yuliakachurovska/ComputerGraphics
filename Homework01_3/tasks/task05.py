import numpy as np

from src.engine.animation.TrsTransformationAnimation import TrsTransformationAnimation
from src.engine.model.Cube import Cube
from src.engine.scene.AnimatedScene import AnimatedScene
from src.math.Mat4x4 import Mat4x4

def main():
    t = 0.5

    pos_start = np.array([0.0, 0.0, 0.0])
    pos_end = np.array([5.0, 5.0, 5.0])
    pos_mid = pos_start * (1 - t) + pos_end * t

    angles_start = np.array([0.0, 0.0, 0.0])
    angles_end = np.array([90.0, 45.0, 180.0])
    angles_mid = angles_start * (1 - t) + angles_end * t

    T_mid = Mat4x4.translation(*pos_mid)
    Rx_mid = Mat4x4.rotation_x(np.radians(angles_mid[0]))
    Ry_mid = Mat4x4.rotation_y(np.radians(angles_mid[1]))
    Rz_mid = Mat4x4.rotation_z(np.radians(angles_mid[2]))

    R_mid = Rx_mid * Ry_mid * Rz_mid
    M_mid = T_mid * R_mid

    print("ЗАВДАННЯ 5: ІНТЕРПОЛЯЦІЯ (t = 0.5)")
    print(f"Проміжні координати: {pos_mid}")
    print(f"Проміжні кути (X, Y, Z): {angles_mid}")
    print("\nМатриця повороту R (t=0.5):\n", R_mid)
    print("\nМатриця переміщення T (t=0.5):\n", T_mid)
    print("\nФінальна проміжна матриця M (t=0.5):\n", M_mid)

    T_final = Mat4x4.translation(*pos_end)
    Rx_final = Mat4x4.rotation_x(np.radians(angles_end[0]))
    Ry_final = Mat4x4.rotation_y(np.radians(angles_end[1]))
    Rz_final = Mat4x4.rotation_z(np.radians(angles_end[2]))
    M_final = T_final * (Rx_final * Ry_final * Rz_final)

    class Task05Scene(AnimatedScene):
        def __init__(self, **kwargs):
            super().__init__(**kwargs)

            cube = Cube(alpha=0.7, color="purple")
            cube.show_local_frame()
            self["cube"] = cube

    scene = Task05Scene()

    animation = TrsTransformationAnimation(
        end=M_final,
        channel="cube",
        frames=120
    )

    scene.add_animations(animation)
    scene.show()

if __name__ == '__main__':
    main()