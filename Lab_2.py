import matplotlib.pyplot as plt
import numpy as np
from PyQt5 import QtWidgets
import uifile  # В этом модуле находится класс в котором отображается класс со всеми виджетами
import sys  # Нужен для выхода из приложения


class MyWindow(QtWidgets.QMainWindow):  # Дефолтное наследование от класса QtWidgets, который рисует окна (и нетолько)
    def __init__(self, parent=None):
        super().__init__()
        self.ui = uifile.Ui_MainWindow()
        self.ui.setupUi(
            self)  # Создание объекта класса Ui_MainWindow и вызов функции setupUi для отображения всего добра
        self.ui.pushButton.clicked.connect(self.show_picture1)  # Думаю шаришь, что это значит

    def show_picture1(self):
        # Эту часть я думаю ты шаришь
        try:
            A = int(self.ui.lineEdit.text())
            B = int(self.ui.lineEdit_2.text())
            D = int(self.ui.lineEdit_3.text())
            N = int(self.ui.lineEdit_4.text())
        except ValueError:
            A, B, D, N = 2, 3, 1, 10

        fig5 = plt.figure(figsize=(8, 7))
        plt.title("Шукана фігура")
        step = 0.1

        ax = plt.subplot()
        ax.set_xbound(-10, 11)
        ax.set_ybound(-10, 11)
        ax.axis("on")

        x = (A - B) * np.cos(np.arange(0, N * (np.pi) + step, step)) + D * np.cos(
            A / B * np.arange(0, N * (np.pi) + step, step))
        y = (A - B) * np.sin(np.arange(0, N * (np.pi) + step, step)) - D * np.sin(
            A / B * np.arange(0, N * (np.pi) + step, step))
        ax.plot(x, y, "r")

        plt.show()


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)  # Запуск всего приложения
    window = MyWindow()
    window.show()  # И только сейчас создание и отображение окна
    sys.exit(app.exec_())  # Выход из приложения

# Попытки смоделировать нашу фигуру:

# for A in range(1, 10):
#     for B in range(1, 10):
#         for D in range(1, 10):
#             for N in range(1, 10):
#                 ax = plt.subplot(111)
#                 ax.set_xbound(-6, 11)
#                 ax.set_ybound(-6, 11)
#                 ax.axis("on")
#
#                 x = (A - B) * np.cos(np.arange(0, N * (np.pi) + step, step)) + D * np.cos(
#                     A / B * np.arange(0, N * (np.pi) + step, step))
#                 y = (A - B) * np.sin(np.arange(0, N * (np.pi) + step, step)) - D * np.sin(
#                     A / B * np.arange(0, N * (np.pi) + step, step))
#                 print(A, B, D, N)
#                 ax.plot(x, y)
#
#                 plt.show()
