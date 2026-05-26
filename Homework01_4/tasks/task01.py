import numpy as np

from src.engine.animation.TrsTransformationAnimation import TrsTransformationAnimation
from src.engine.model.Cube import Cube
from src.engine.scene.AnimatedScene import AnimatedScene
from src.math.Mat4x4 import Mat4x4

def main():
    theta = np.radians(45)
    v = np.array([1.0, 1.0, 1.0])
    u = v / np.linalg.norm(v)

    half_theta = theta / 2.0

    w = np.cos(half_theta)
    x = u[0] * np.sin(half_theta)
    y = u[1] * np.sin(half_theta)
    z = u[2] * np.sin(half_theta)

    r11 = 1 - 2 * y**2 - 2 * z**2
    r12 = 2 * x * y - 2 * z * w
    r13 = 2 * x * z + 2 * y * w

    r21 = 2 * x * y + 2 * z * w
    r22 = 1 - 2 * x**2 - 2 * z**2
    r23 = 2 * y * z - 2 * x * w

    r31 = 2 * x * z - 2 * y * w
    r32 = 2 * y * z + 2 * x * w
    r33 = 1 - 2 * x**2 - 2 * y**2

    R_4x4 = Mat4x4(
        r11, r12, r13, 0,
        r21, r22, r23, 0,
        r31, r32, r33, 0,
        0,   0,   0,   1
    )

    print("ЗАВДАННЯ 1: ПОВОРОТ НАВКОЛО (1,1,1) НА 45°")
    print(f"Нормалізована вісь: {u}")
    print(f"Кватерніон (w, x, y, z): ({w:.4f}, {x:.4f}, {y:.4f}, {z:.4f})")
    print("\nРозрахована матриця повороту R (4x4):\n", R_4x4)

    class QuaternionTask2Scene(AnimatedScene):
        def __init__(self, **kwargs):
            super().__init__(**kwargs)

            cube = Cube(alpha=0.7, color="magenta")
            cube.show_local_frame()
            self["cube"] = cube

    scene = QuaternionTask2Scene()

    animation = TrsTransformationAnimation(
        end=R_4x4,
        channel="cube",
        frames=100
    )

    scene.add_animations(animation)
    scene.show()

if __name__ == '__main__':
    main()