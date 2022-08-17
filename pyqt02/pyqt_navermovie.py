from re import search
import sys
from PyQt5 import QtGui, uic
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from urllib.parse import quote
import urllib.request
import json
import webbrowser

# 클래스 OOP
class qTemplate(QWidget):
    # 생성자 : 기본적으로 리턴값을 가지지 않아서 None 을 적음
    def __init__(self) -> None:
        super().__init__()
        uic.loadUi('./pyqt02/navermovie.ui', self)
        self.initUI()

    def initUI(self) -> None:
        self.addControls()
        self.show()

    def addControls(self) -> None:  # 위젯 정의, 이벤트(시그널) 처리
        self.btnSearch.clicked.connect(self.btnSearchClicked)
        self.txtSearch.returnPressed.connect(self.btnSearchClicked)
        self.tblResult.itemSelectionChanged.connect(self.tblResultSeleccted)

    def tblResultSeleccted(self) -> None:
        selected = self.tblResult.currentRow()  # 현재 선택된 열의 인덱스
        link = self.tblResult.item(selected, 2).text()
        webbrowser.open(link)


    def btnSearchClicked(self) -> None:     # 슬롯(이벤트핸들러)
        jsonResult = []
        totalResult = []
        keyword = 'movie'
        search_word = self.txtSearch.text()
        display_count = 50

        # QMessageBox.information(self, '결과', search_word)
        jsonResult = self.getNaverSearch(keyword, search_word, 1, display_count)
        #print(jsonResult)
        
        
        for post in jsonResult['items']:
            totalResult.append(self.getPostData(post))

        # print(totalResult)
        self.makeTable(totalResult)
    
    # html 태그 없애주는 함수
    def strip_tag(self, title):
        ret = title.replace('&lt;', '<')
        ret = ret.replace('&gt;', '>')
        ret = ret.replace('&quot;', '"')
        ret = ret.replace('&apos;', "'")
        ret = ret.replace('&amp;', '&')
        ret = ret.replace('<b>', '')
        ret = ret.replace('</b>', '')

        return ret



    def makeTable(self, result):
        self.tblResult.setSelectionMode(QAbstractItemView.SingleSelection)
        self.tblResult.setColumnCount(3)    #from 2 -> 3
        self.tblResult.setRowCount(len(result))     # displayCount에 따라서 변경, 현재는 50
        self.tblResult.setHorizontalHeaderLabels(['영화제목','상영년도','뉴스링크'])
        self.tblResult.setColumnWidth(0, 250)
        self.tblResult.setColumnWidth(1, 100)
        self.tblResult.setColumnWidth(2, 100)   # 세번째컬럼 길이
        self.tblResult.setEditTriggers(QAbstractItemView.NoEditTriggers)    # readonly

        i = 0
        for item in result:
            title = self.strip_tag(item[0]['title'])
            subtitle = self.strip_tag(item[0]['subtitle'])
            pubDate = item[0]['pubDate']
            link = item[0]['link']
            self.tblResult.setItem(i, 0, QTableWidgetItem(f'{title} / {subtitle}'))
            self.tblResult.setItem(i, 1, QTableWidgetItem(pubDate))
            self.tblResult.setItem(i, 2, QTableWidgetItem(link))
            i += 1


    def getPostData(self, post):
        temp = []
        title = post['title']
        subtitle = post['subtitle']
        link = post['link']
        pubDate = post['pubDate']

        temp.append({'title':title, 
                     'subtitle':subtitle, 
                     'pubDate':pubDate, 
                     'link':link})
        
        return temp

    # 네이버API 크롤링 함수
    def getNaverSearch(self, keyword, search, start, display):
        url = f'https://openapi.naver.com/v1/search/{keyword}.json' \
              f'?query={quote(search)}&start={start}&display={display}'
        print(url)
        req = urllib.request.Request(url)
        # 네이버 인증 추가
        req.add_header('X-Naver-Client-Id', 'qgr0aJ4_qc2tNn7OMtBS')
        req.add_header('X-Naver-Client-Secret', 'KfwFcUvYVr')

        res = urllib.request.urlopen(req)
        if res.getcode() == 200:
            print('URL request succeed')
        else:
            print('URL request failed')

        ret = res.read().decode('utf-8')
        if ret == None:
            return None
        else:
            return json.loads(ret)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ins = qTemplate()
    app.exec_()
