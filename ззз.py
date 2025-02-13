import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from matplotlib.colors import LightSource

# Создаем координаты X, Y
X = np.linspace(-5, 5, 100)
Y = np.linspace(-5, 5, 100)
X_grid, Y_grid = np.meshgrid(X, Y)

# Функция рельефа (горы и холмы)
Z_grid = np.sin(np.sqrt(X_grid**22 + Y_grid**22)) * 22 + np.cos(Y_grid) * 15

# Добавляем источник света
ls = LightSource(azdeg=315, altdeg=45)

# Используем plt.cm.terrain вместо 'terrain'
shaded_Z = ls.shade(Z_grid, cmap=plt.cm.terrain, vert_exag=0.2, blend_mode='soft')

# Создаем 3D-график
fig = plt.figure(figsize=(8, 6))
ax = fig.add_subplot(111, projection='3d')

# Отображаем рельеф с тенью
ax.plot_surface(X_grid, Y_grid, Z_grid, facecolors=shaded_Z, rstride=1, cstride=1)

# Настройки осей
ax.set_xlabel("X координата")
ax.set_ylabel("Y координата")
ax.set_zlabel("Высота (Z)")

plt.show()








import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

def create_sphere(radius=1.0, num_points=100):
    # Создаем углы theta и phi
    theta = np.linspace(0, 2 * np.pi, num_points)  # Угол вокруг оси Z
    phi = np.linspace(0, np.pi, num_points)        # Угол от оси Z

    # Создаем сетку углов
    theta, phi = np.meshgrid(theta, phi)

    # Преобразуем сферические координаты в декартовы
    x = radius * np.sin(phi) * np.cos(theta)
    y = radius * np.sin(phi) * np.sin(theta)
    z = radius * np.cos(phi)

    return x, y, z

# Создаем сферу
x, y, z = create_sphere(radius=1.0, num_points=100)

# Визуализация
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# Отображаем поверхность сферы
ax.plot_surface(x, y, z, color='b', alpha=0.7)

# Настройка осей
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')

# Установим одинаковый масштаб для осей
ax.set_box_aspect([1, 1, 1])  # Это обеспечивает равный масштаб по всем осям

# Показать график
plt.show()
