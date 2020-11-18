import sys
import random

from PyQt5 import QtCore
from Ui import Ui_yellowballs
from PyQt5.QtGui import QPainter, QColor
from PyQt5.QtWidgets import QApplication, QDialog, QAbstractItemView
from PyQt5.QtWidgets import QMainWindow, QTableWidgetItem, QWidget


class Example(QDialog, Ui_yellowballs):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.btn_draw.clicked.connect(self.Draw)

    def initUI(self):
        self.setGeometry(100, 100, 900, 900)
        self.slid.setFocusPolicy(Qt.NoFocus)
        self.setWindowTitle('yellow balls')

    def Draw(self):
        self.update()

    def paintEvent(self, event):
        x = int(random.random() * 500)
        y = int(random.random() * 300)
        r = int(random.random() * 300)
        qp = QPainter()
        qp.begin(self)
        a = int(random.random() * 250)
        b = int(random.random() * 250)
        c = int(random.random() * 250)
        qp.setPen(QColor(a, b, c))
        qp.drawEllipse(x, y, 10 + r, 10 + r)
        qp.end()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    ex.show()
    sys.exit(app.exec())
