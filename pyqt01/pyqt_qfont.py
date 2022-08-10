import sys
from PyQt5.QtWidgets import QApplication, QWidget
from PyQt5.QtGui import QPainter, QColor, QFont
from PyQt5.QtCore import Qt

# 클래스 OOP
class qTemplate(QWidget):
    # 생성자 : 기본적으로 리턴값을 가지지 않아서 None 을 적음
    def __init__(self) -> None:
        super().__init__()
        self.initUI()

    # 화면정의를 위해 사용자 함수
    def initUI(self) -> None:
        # 화면위치(x, y), size(x, y)
        self.setGeometry(300, 100, 640, 400)
        self.setWindowTitle('QTemplate!!!')
        self.text = 'What a wonderful world~~'
        self.show()

    def paintEvent(self, event) -> None:
        paint = QPainter()
        paint.begin(self)
        # 그리는 함수 추가
        self.drawText(event, paint)
        paint.end()

    # 텍스트 그리기 위한 사용자함수
    def drawText(self, event, paint):
        paint.setPen(QColor(50,50,50))
        paint.setFont(QFont('NanumGothic', 20))
        paint.drawText(105, 100, 'HELL WORLD~~~~')
        paint.setPen(QColor(0,0,250))
        paint.setFont(QFont('Impact', 20))
        #새창의 중심에 글자표시
        paint.drawText(event.rect(), Qt.AlignCenter, self.text)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ins = qTemplate()
    app.exec_()
