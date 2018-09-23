import matplotlib.pyplot as plt
import numpy as np

A, B, D, N = 2, 3, 1, 10               # Константы


def make_ornament(period, radius):     # Функция, создающая орнамент, вращая осн. рисунок по кругу с радиусом radius
    fig5 = plt.figure(figsize=(8, 7))  # и периодом period, при этом изменяя его форму.
    plt.title("Шукана фігура")
    step = 0.1
    ax = fig5.add_subplot(1, 1, 1, label="test")
    ax.axis('off')
    for phi in range(0, 360, period):
        x = ((A - B) * np.cos(np.arange(0, N * np.pi + step, step)) + D * np.cos(
            A / B * np.arange(0, N * np.pi + step, step))) * np.cos(np.deg2rad(phi)) + radius * np.cos(np.deg2rad(phi))
        y = ((A - B) * np.sin(np.arange(0, N * np.pi + step, step)) - D * np.sin(
            A / B * np.arange(0, N * np.pi + step, step))) * np.sin(np.deg2rad(phi)) + radius * np.sin(np.deg2rad(phi))
        ax.plot(x, y, "r")
    plt.show()


def make_effect(period, radius):       # Функция, создающая муар, вращая осню рисунок по кругу с радиусом radius
    fig5 = plt.figure(figsize=(8, 7))  # и периодом period.
    plt.title("Шукана фігура")
    step = 0.1
    ax = fig5.add_subplot(1, 1, 1, label="test")
    ax.axis('off')
    for i in range(0, 360, period):
        x = ((A - B) * np.cos(np.arange(0, N * np.pi + step, step)) + D * np.cos(
            A / B * np.arange(0, N * np.pi + step, step))) + radius * np.cos(np.deg2rad(i))
        y = ((A - B) * np.sin(np.arange(0, N * np.pi + step, step)) - D * np.sin(
            A / B * np.arange(0, N * np.pi + step, step))) + radius * np.sin(np.deg2rad(i))
        ax.plot(x, y, "r")
    plt.show()


make_ornament(5, 3)  # В скобках основные параметры(дефолтные) для орнамента
make_effect(3, 3)    # Аналогично для муара
