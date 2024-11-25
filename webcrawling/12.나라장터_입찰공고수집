import selenium
import requests
from bs4 import BeautifulSoup

#브라우저 자동 종료 방지 ('detach', TRUE)
from selenium.webdriver.chrome.options import Options
chrome_option = Options()
# chrome_option.add_experimental_option('detach', True)


from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select

#크롬 브라우저 객체 생성 
driver = webdriver.Chrome(options=chrome_option)
driver.get("https://www.g2b.go.kr/index.jsp")


업무구분 = Select(driver.find_element(by=By.ID, value='taskClCds'))
업무구분.select_by_value('5') #5번 용역선택 

공고명 = driver.find_element(by=By.ID, value='bidNm')
공고명.send_keys('예측모델')

공고일최대1개월 = driver.find_element(by=By.ID, value='setMonth1_1')
공고일최대1개월.click()

#검색버튼 클릭
검색 = driver.find_element(by=By.CSS_SELECTOR, value= 'dd.fr > a > strong')
검색.click()

#공고상세 화면 출력
#resultForm > div.results > table > tbody > tr:nth-child(1) > td:nth-child(2) > div > a
하단프레임 = driver.find_element(by=By.CSS_SELECTOR, value='frameset frame#sub')
# print(하단프레임)
driver.switch_to.frame(하단프레임)

콘텐츠프레임 = driver.find_element(by=By.CSS_SELECTOR, value='frame[name=main]')
# print(콘텐츠프레임)
driver.switch_to.frame(콘텐츠프레임)

입찰공고목록 = driver.find_elements(by=By.CSS_SELECTOR, value='#resultForm table tbody tr')
# print(len(입찰공고목록))

#공고내용 추출 및 추정가격 출력 
for 입찰공고 in 입찰공고목록:
    공고정보 = 입찰공고.find_elements(by=By.TAG_NAME, value='td')
    공고명 = 공고정보[3].text
    공고주소 = 공고정보[3].find_element(by=By.TAG_NAME, value='a').get_property('href')
    print(공고명, 공고주소)
    공고내역 = requests.get(공고주소)
    공고내역_soup = BeautifulSoup(공고내역.text,'html.parser')
    #print(공고내역_soup)
    print(공고내역_soup.select('#container > div:nth-child(12) > table > tbody > tr > td'))
    

    