import sys
from PyQt5 import QtGui, uic
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *

# 클래스 OOP
class qTemplate(QWidget):
    # 생성자 : 기본적으로 리턴값을 가지지 않아서 None 을 적음
    def __init__(self) -> None:
        super().__init__()
        uic.loadUi('./pyqt02/ttask.ui', self)
        self.initUI()

    def initUI(self) -> None:
        self.addControls()
        self.show()

    def addControls(self) -> None:
         self.btnStart.clicked.connect(self.btn1_clicked)    # 시그널 연결

    # click -> 클릭하는 순간
    # clicked -> 클릭을 하고 손을 떼는 순간
    # event = signal (python)

    def btn1_clicked(self):
        self.txbLog.append('실행!!')
        self.qgbTask.setRange(0, 999999)
        for i in range(0,1000000):      # 응담없음 발생!!
            print(f'출력 : {i}')
            self.qgbTask.setValue(i)
            self.txbLog.append(f'출력 > {i}')


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ins = qTemplate()
    app.exec_()
