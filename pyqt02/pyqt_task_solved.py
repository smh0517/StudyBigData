import sys
from PyQt5 import QtGui, uic
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
import time


# UI 스레드와 작업스레드 분리
class Worker(QThread):
    # QThread는 화면을 그릴 권한이 없음
    # 대신 통신 통해서 UI스레드가 그림을 그릴 수 있도록 통신수행
    valChangeSignal = pyqtSignal(int)
    def __init__(self, parent):
        super().__init__(parent)
        self.parent = parent
        self.working = True     # 클래스 내부변수 working을 지정
    
    def run(self):
        while self.working:
            for i in range(0,1000000):      # 응담없음 발생!!
                print(f'출력 : {i}')
                # self.qgbTask.setValue(i)
                # self.txbLog.append(f'출력 > {i}')
                self.valChangeSignal.emit(i)    #UI스레드야 화면은 니가 그려줘~
                time.sleep(0.0001)      # 1micro sec

        

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
         # Worker 클래스 생성
         self.worker = Worker(self)
         self.worker.valChangeSignal.connect(self.updateProgress)   # 스레드에서 받은 시그널은
         # updataeProgress함수에서 처리해줌

    @pyqtSlot(int)
    def updateProgress(self, val): # val이 Worker스레드에서 전달받은 반복값
        self.qgbTask.setValue(val)
        self.txbLog.append(f'출력 > {val}')
        if val == 999999:
            self.worker.working = False



    def btn1_clicked(self):
        self.txbLog.append('실행!!')
        self.qgbTask.setRange(0, 999999)
        self.worker.start()
        self.worker.working = True
        

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ins = qTemplate()
    app.exec_()
