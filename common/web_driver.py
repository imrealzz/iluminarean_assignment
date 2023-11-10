# webdriver 정의

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
import sys
import os
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from driver import chromedriver
from common import env

def open_webdriver(url):
    global driver         
    global action
    
    chrome_options = Options()
    # size 최대 및 창 꺼짐 방지용
    chrome_options.add_argument("--start-maximized")
    chrome_options.add_experimental_option("detach", True)
    _chromedriver = env.driver_path
    service = Service(executable_path=_chromedriver)

    try:
        driver = webdriver.Chrome(service=service, options=chrome_options)
    except:
        #크롬 드라이버 재 설치 (개인 프로젝트 활용)
        chromedriver.chromedriver_download()
        driver = webdriver.Chrome(service=service, options=chrome_options)

    driver.get(url)

    action = ActionChains(driver)
    
    return driver

if __name__ == "__main__":    
    open_webdriver("https://illuminarean.com")
