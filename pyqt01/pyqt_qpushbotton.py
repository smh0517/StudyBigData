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
        self.setWindowTitle('QPushbutton 예제')
        self.show()

    def addControls(self) -> None:
        self.label = QLabel('메시지:', self)
        self.label.setGeometry(10, 10, 600, 40)
        self.btn1 = QPushButton('클릭', self)
        self.btn1.setGeometry(510, 350, 120, 40)
        self.btn1.clicked.connect(self.btn1_clicked)    # 시그널 연결

    # click -> 클릭하는 순간
    # clicked -> 클릭을 하고 손을 떼는 순간
    # event = signal (python)

    def btn1_clicked(self):
        # QMessageBox.information(self, 'slgnal', 'btn1_clicked')   # 일반정보창
        # QMessageBox.warning(self, 'slgnal', 'btn1_clicked')       # 경고창
        self.label.setText('메시지: btn1 버튼 클릭!!!!')
        QMessageBox.critical(self, 'slgnal', 'btn1_clicked')        # 에러창


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ins = qTemplate()
    app.exec_()
