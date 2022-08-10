import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *

# 클래스 OOP
class qTemplate(QWidget):
    # 생성자 : 기본적으로 리턴값을 가지지 않아서 None 을 적음
    def __init__(self) -> None:
        super().__init__()
        self.initUI()

    def initUI(self) -> None:
        self.addControls()
        # 화면위치(x, y), size(x, y)
        self.setGeometry(300, 100, 640, 400)
        self.setWindowTitle('QPushbutton')
        self.show()

    def addControls(self) -> None:
        btn1 = QPushButton('Click', self)
        btn1.setGeometry(510, 350, 120, 40)



if __name__ == '__main__':
    app = QApplication(sys.argv)
    ins = qTemplate()
    app.exec_()
