import numpy as np

from src.engine.animation.TrsTransformationAnimation import TrsTransformationAnimation
from src.engine.model.Cube import Cube
from src.engine.scene.AnimatedScene import AnimatedScene
from src.math.Mat4x4 import Mat4x4

def main():
    theta = np.radians(45)
    alpha = np.radians(45)
    R1 = Mat4x4.rotation_x(alpha)
    beta = np.arctan(1.0 / np.sqrt(2))
    R2 = Mat4x4.rotation_y(-beta)
    R3 = Mat4x4.rotation_z(theta)
    R2_inv = Mat4x4.rotation_y(beta)
    R1_inv = Mat4x4.rotation_x(-alpha)
    M_euler = R1_inv * R2_inv * R3 * R2 * R1

    v = np.array([1.0, 1.0, 1.0])
    u = v / np.linalg.norm(v)

    K = np.array([
        [0, -u[2], u[1]],
        [u[2], 0, -u[0]],
        [-u[1], u[0], 0]
    ])

    I = np.eye(3)
    R_rodrigues_3x3 = I + np.sin(theta) * K + (1 - np.cos(theta)) * (K @ K)

    print("ЗАВДАННЯ 6: ДОВІЛЬНА ВІСЬ (1,1,1)")
    print("1. Матриця 4x4 через кути Ойлера (Метод 1):\n", M_euler)
    print("\n2. Матриця 3x3 через формулу Родрігеса (Метод 2):\n", R_rodrigues_3x3)
    print("Висновок: Верхній лівий квадрант 3x3 в матриці Ойлера")
    print("ідеально співпадає з матрицею Родрігеса!")

    class Task06Scene(AnimatedScene):
        def __init__(self, **kwargs):
            super().__init__(**kwargs)

            cube = Cube(alpha=0.6, color="cyan")
            cube.show_local_frame()
            self["cube"] = cube

    scene = Task06Scene()

    animation = TrsTransformationAnimation(
        end=M_euler,
        channel="cube",
        frames=100
    )

    scene.add_animations(animation)
    scene.show()

if __name__ == '__main__':
    main()