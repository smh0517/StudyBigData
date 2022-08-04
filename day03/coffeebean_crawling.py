# Selenium사용 웹페이지 크롤링
# 패키지 로드
from bs4 import BeautifulSoup
import pandas as pd
import time
from selenium import webdriver

def getCoffeBeanStoreInfo(result):
    #USB: usb_device_handle_win.cc:1048 Failed to read descriptor from node connection: 시스템에 부착된 장치가 작동하지 않습니다. (0x1F)
    #오류 해결 방법
    options = webdriver.ChromeOptions()
    options.add_experimental_option("excludeSwitches", ["enable-logging"])
    wd = webdriver.Chrome('./day03/chromedriver.exe', options=options)
    
    # Chrome webdriver 객체 생성
    # wd = webdriver.Chrome('./day03/chromedriver.exe')       # 경로 조심!   

    for i in range(1, 20+1):
        wd.get('https://www.coffeebeankorea.com/store/store.asp')
        time.sleep(1)

        try:
            wd.execute_script(f"storePop2('{i}')")
            # 팝업표시후에 크롤링이 안돼서 브라우저가 닫히는 것을 방지
            time.sleep(0.5)       
            # 웹드라이버로 읽어온 페이지를 html로 할당
            html = wd.page_source
            soup = BeautifulSoup(html, 'html.parser')
            store_name = soup.select('div.store_txt > h2')[0].string
            print(store_name)
            store_info = soup.select('table.store_table > tbody > tr > td')
            store_address_list = list(store_info[2])
            store_address = store_address_list[0].strip()
            store_contact = store_info[3].string
            result.append([store_name]+[store_address]+[store_contact])
        
        except Exception as e:
            print(e)
            continue

def main():
    result = []
    print('커피빈 매장 크롤링 >>>')
    getCoffeBeanStoreInfo(result)

    # 판다스 데이터프레임 생성
    columns = ['store', 'address', 'phone']
    coffebean_df = pd.DataFrame(result, columns=columns)

    # csv 저장
    coffebean_df.to_csv('./coffebean_shop_info.csv', index=True, encoding='utf-8')
    print('저장완료!')

    del result[:]

if __name__ == '__main__':
    main()
