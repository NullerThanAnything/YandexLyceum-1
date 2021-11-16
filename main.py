from sys import argv, exit
from PyQt5 import uic
from random import randint
from PyQt5.QtCore import QPointF, Qt
from PyQt5.QtGui import QPainter, QBrush, QPen
from PyQt5.QtWidgets import QApplication, QMainWindow


class Main(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('UI.ui', self)
        self.pushBtn.clicked.connect(self.paint)
        self.should_paint = False

    def paintEvent(self, event):
        if self.should_paint:
            qp = QPainter(self)
            qp.setPen(QPen(Qt.yellow, 8, Qt.SolidLine))
            qp.setBrush(QBrush(Qt.yellow, Qt.SolidPattern))
            a = randint(1, 100)
            x = randint(1, 500)
            y = randint(1, 500)
            qp.drawEllipse(x, y, a, a)

    def paint(self):
        self.should_paint = True
        self.update()


if __name__ == '__main__':
    app = QApplication(argv)
    ex = Main()
    ex.show()
    exit(app.exec())
