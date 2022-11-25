from PyQt5.QtWidgets import QApplication, QWidget
from PyQt5 import uic
import sys
from random import randint
from PyQt5.QtGui import QPainter, QColor
from PyQt5.QtCore import QPoint


class Program(QWidget):

    def __init__(self):

        super().__init__()
        uic.loadUi('UI.ui', self)

        self.do_paint = True
        self.pushButton.clicked.connect(self.start_paint)
        self.painters = []

    def start_paint(self):
        self.do_paint = True
        self.repaint(self.rect())

    def draw_circles(self, qp):
        for i in range(randint(5, 15)):
            self.draw_circle(qp)

    def paintEvent(self, event):
        if self.do_paint:
            qp = QPainter()
            qp.begin(self)
            self.draw_circles(qp)
            qp.end()
            self.do_paint = False
    
    def draw_circle(self, qp):
        
        qp.setBrush(QColor('yellow'))
        a, b = self.geometry().getRect()[2:4]
        xc, yc = randint(50, a - 30), randint(50, b - 30)
        try:
            d = randint(5, min(min(xc, a - xc), min(yc, b - yc)))
        except ValueError:
            d = 1
        qp.drawEllipse(QPoint(xc, yc), d, d)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    p = Program()
    p.show()
    sys.exit(app.exec())