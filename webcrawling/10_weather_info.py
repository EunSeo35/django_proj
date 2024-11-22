import requests
from bs4 import BeautifulSoup
url = 'https://www.weather.go.kr/w/index.do'
# response = requests.get(url)
# soup = BeautifulSoup(response.text, 'html.parser')
# weather = soup.select('span.tmp')
# print(weather)
import selenium

#브라우저 자동 종료 방지 ('detach', TRUE)
from selenium.webdriver.chrome.options import Options
chrome_option = Options()
chrome_option.add_experimental_option('detach', True)


from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


driver = webdriver.Chrome(options=chrome_option)
driver.get(url)

wait = WebDriverWait(driver,10)
tmp_element = wait.until(
    EC.presence_of_element_located((By.CSS_SELECTOR, 'span.tmp'))
)
#tmp_element = driver.find_element(by=By.CSS_SELECTOR, value='span.tmp')
print(tmp_element.text)