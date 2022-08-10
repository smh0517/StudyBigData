import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QVBoxLayout, QHBoxLayout
from PyQt5.QtGui import QPainter, QColor, QFont, QIcon
# from PyQt5.QtCore import Qt

# 클래스 OOP
class qTemplate(QWidget):
    # 생성자 : 기본적으로 리턴값을 가지지 않아서 None 을 적음
    def __init__(self) -> None:
        super().__init__()
        self.initUI()

    # 화면정의를 위해 사용자 함수
    def initUI(self) -> None:
        self.addControls()
        # 화면위치(x, y), size(x, y)
        self.setGeometry(300, 100, 640, 400)
        self.setWindowTitle('QLabel')
        self.show()

    def addControls(self) -> None:
        self.setWindowIcon(QIcon('./pyqt01/image/image1.png'))
        label1 = QLabel('label1', self) 
        label2 = QLabel('label2', self)
        label1.setStyleSheet(
            'border-width: 3px;'
            'border-style: solid;'
            'border-color: blue;'
             # 경로 잘 확인!! 상대경로로 해야함
            'image: url(./pyqt01/image/image1.png)'
        )
        label2.setStyleSheet(
            'border-width: 3px;'
            'border-style: dot-dot-dash;'
            'border-color: red;'
             # 경로 잘 확인!! 상대경로로 해야함
            'image: url(./pyqt01/image/image2.png)'
        )

        # QV -> 세로 / QH -> 가로
        box = QHBoxLayout()
        box.addWidget(label1)
        box.addWidget(label2)
        self.setLayout(box)

    

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ins = qTemplate()
    app.exec_()
