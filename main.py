import io
import sys
from random import randrange as rr

from PyQt6 import uic
from PyQt6.QtCore import Qt, QRectF, QPointF
from PyQt6.QtWidgets import QApplication, QMainWindow
from PyQt6.QtGui import QPainter, QColor, QPolygonF


class UselessApp(QMainWindow):
    def __init__(self):
        super().__init__()
        
        uic.loadUi('UI.ui', self)

        self.shapeButton.clicked.connect(self.create_shape)

    def create_shape(self):
        self.update()

    def paintEvent(self, event):
        d = rr(100, 300)

        qp = QPainter()

        qp.begin(self)
        qp.setPen(QColor(255, 255, 0))
        qp.drawEllipse(rr(0, 800 - d), rr(0, 800 - d), d, d)

        qp.end()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = UselessApp()
    ex.show()
    sys.exit(app.exec())
