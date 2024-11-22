'''
Selenium은 웹 애플리케이션을 자동화하는 데 사용되는 오픈 소스 도구
주로 웹 브라우저를 자동으로 제어하거나 테스트 환경에서 브라우저 동작을 시뮬레이션하는 데 사용
다양한 언어와 브라우저를 지원하며, 주로 웹 애플리케이션 테스트를 목적으로 사용되지만, 데이터 크롤링, 스크래핑, 반복적인 웹 작업 자동화에도 활용
'''
import selenium

#브라우저 자동 종료 방지 ('detach', TRUE)
from selenium.webdriver.chrome.options import Options
chrome_option = Options()
chrome_option.add_experimental_option('detach', True)


from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

#크롬 브라우저 객체 생성 
driver = webdriver.Chrome(options=chrome_option)
driver.get("https://www.python.org/")

#검색어에 'pycon'입력
#input_el = driver.find_element(by='id',value='id-search-field')
#input_el = driver.find_element(by='css selector',value='id-search-field')
#input_el = driver.find_element(by=By.ID,value='id-search-field')
input_el = driver.find_element(by=By.CSS_SELECTOR,value='#id-search-field')

input_el.send_keys('pycon') # 검색어 입력 
input_el.send_keys(Keys.RETURN) #자동으로 enter 침 

#검색 결과 추출 
input_el = driver.find_elements(by=By.CSS_SELECTOR, value="form li h3 > a")
for i_el in input_el:
    print(i_el.text)
