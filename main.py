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
        self.paintEvent(1)

    def draw_circles(self):
        for i in range(randint(5, 15)):
            self.draw_circle()

    def paintEvent(self, event):
        if self.do_paint:
            self.painters.append(QPainter())
            self.painters[-1].begin(self)
            self.draw_circles()
            self.painters[-1].end()
            self.do_paint = False
    
    def draw_circle(self):
        
        self.painters[-1].setBrush(QColor('yellow'))
        xc, yc = randint(50, 550), randint(50, 650)
        try:
            d = randint(5, min(min(xc, 570 - xc), min(yc, 650 - yc)))
        except ValueError:
            d = 1
        self.painters[-1].drawEllipse(QPoint(xc, yc), d, d)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    p = Program()
    p.show()
    sys.exit(app.exec())