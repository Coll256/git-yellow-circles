import sys
from random import randrange as rr

from PyQt6.QtWidgets import QApplication, QMainWindow
from PyQt6.QtGui import QPainter, QColor

from ui import Ui_MainWindow


class UselessInterface():
    pass


class UselessApp(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        
        self.setupUi(self)

        self.shapeButton.clicked.connect(self.create_shape)

    def create_shape(self):
        self.update()

    def paintEvent(self, event):
        d = rr(100, 300)

        qp = QPainter()

        qp.begin(self)
        qp.setPen(QColor(rr(0, 256), rr(0, 256), rr(0, 256)))
        qp.drawEllipse(rr(0, 800 - d), rr(0, 800 - d), d, d)

        qp.end()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = UselessApp()
    ex.show()
    sys.exit(app.exec())
