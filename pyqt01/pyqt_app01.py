# 가장 심플한 PyQt 실행방법
from PyQt5 import QtWidgets as qw

def run():
    app = qw.QApplication([])
    wnd = qw.QMainWindow()
    label = qw.QLabel('Helllo Qt!')
    wnd.setCentralWidget(label)         # 중앙에 보이겠다
    wnd.show()
    app.exec_()

if __name__ == '__main__':
    run()
