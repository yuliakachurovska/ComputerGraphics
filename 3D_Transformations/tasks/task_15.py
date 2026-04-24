import numpy as np
import math

from src.engine.animation.TrsTransformationAnimation import TrsTransformationAnimation
from src.engine.model.Cube import Cube
from src.engine.scene.AnimatedScene import AnimatedScene
from src.math.Mat4x4 import Mat4x4

def decompose_matrix(m_array):
    """
    Приймає 4x4 numpy масив (афінну матрицю).
    Повертає: вектор переміщення, вектор масштабу, кут обертання, вісь обертання.
    """
    translation = m_array[0:3, 3]

    M33 = m_array[0:3, 0:3]
    sx = np.linalg.norm(M33[:, 0])
    sy = np.linalg.norm(M33[:, 1])
    sz = np.linalg.norm(M33[:, 2])
    scale = (sx, sy, sz)

    R = np.copy(M33)
    R[:, 0] /= sx
    R[:, 1] /= sy
    R[:, 2] /= sz

    trace = np.trace(R)
    cos_theta = np.clip((trace - 1) / 2.0, -1.0, 1.0)
    angle_rad = math.acos(cos_theta)
    angle_deg = math.degrees(angle_rad)

    sin_theta = math.sin(angle_rad)
    if sin_theta > 1e-5:
        ux = (R[2, 1] - R[1, 2]) / (2 * sin_theta)
        uy = (R[0, 2] - R[2, 0]) / (2 * sin_theta)
        uz = (R[1, 0] - R[0, 1]) / (2 * sin_theta)
        axis = (ux, uy, uz)
    else:
        axis = (0, 0, 1)

    return translation, scale, angle_deg, axis


if __name__ == '__main__':
    CUBE_START_KEY = "cube_start"
    CUBE_ANIMATED_KEY = "cube_animated"

    class TaskScene(AnimatedScene):
        def __init__(self, **kwargs):
            super().__init__(**kwargs)
            cube_start = Cube(alpha=0.1, color="blue")
            self[CUBE_START_KEY] = cube_start
            cube_animated = Cube(alpha=0.1, color="grey", line_width=0.8, line_style="-.")
            self[CUBE_ANIMATED_KEY] = cube_animated

    animated_scene = TaskScene(
        coordinate_rect=(-8, -2, -2, 4, 6, 4),
        title="Завдання 15: Складна композиція та декомпозиція"
    )

    T1 = Mat4x4.translation(-1, -1, -1)
    S  = Mat4x4.scale(2, 2, 2)
    T2 = Mat4x4.translation(1, 1, 1)
    M_scale = T2 * S * T1

    R_loc = Mat4x4.rotation_z(90, is_radians=False)
    M_step2 = M_scale * R_loc

    T_ext = Mat4x4.translation(-3, 4, 2)
    M_final = T_ext * M_step2

    M_numpy = np.array([
        [0.0, -2.0, 0.0, -4.0],
        [2.0,  0.0, 0.0,  3.0],
        [0.0,  0.0, 2.0,  1.0],
        [0.0,  0.0, 0.0,  1.0]
    ])
    t, s, ang, ax = decompose_matrix(M_numpy)

    print("=== РЕЗУЛЬТАТИ ДЕКОМПОЗИЦІЇ ФІНАЛЬНОЇ МАТРИЦІ ===")
    print(f"Масштаб (Sx, Sy, Sz): ({s[0]:.2f}, {s[1]:.2f}, {s[2]:.2f})")
    print(f"Кут обертання:        {ang:.2f}°")
    print(f"Вісь обертання (U):   ({ax[0]:.2f}, {ax[1]:.2f}, {ax[2]:.2f})")
    print(f"Вектор перенесення:   ({t[0]:.2f}, {t[1]:.2f}, {t[2]:.2f})")

    animation_move = TrsTransformationAnimation(
        end=M_final,
        channel=CUBE_ANIMATED_KEY,
        frames=180,
        repeat=False
    )

    animated_scene.add_animations(animation_move)
    animated_scene.show()