import sys
from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton
from PyQt5.QtGui import QPainter, QColor
import random

class Example(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setGeometry(700, 200, 500, 500)
        uic.loadUi('Ui.ui', self)
        self.main()

    def main(self):
        self.flag = False
        self.setGeometry(300, 300, 600, 600)
        self.setWindowTitle('Моя программа')
        self.pushButton.clicked.connect(self.flag_change)

    def flag_change(self):
        self.flag = True
        self.update()

    def paintEvent(self, event):
        qp = QPainter()
        qp.begin(self)
        qp.setPen(QColor('yellow'))
        qp.setBrush(QColor('yellow'))
        self.drawCircle(qp)
        qp.end()

    def drawCircle(self, qp):
        rad = random.randint(10, 200)
        if self.flag:
            qp.drawEllipse(random.randint(0, 400), random.randint(100, 400), rad, rad)



app = QApplication(sys.argv)
ex = Example()
ex.show()
sys.exit(app.exec_())
