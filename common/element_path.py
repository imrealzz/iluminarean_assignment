#-*- coding: utf-8 -*-

from common import web_driver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

# 상위 path element로 이동
def par_path(path):    
    up_path =  path.find_element(By.XPATH, "..")

    return up_path

# 라벨로 path 찾기
def label_path(tag, label):
    global driver
    driver = web_driver.driver        
    element =  WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, f'{tag}[aria-label="{label}"]')))

    return element

# 텍스트로 path 찾기
def text_path(tag, text):
    global driver
    driver = web_driver.driver        
    element =  WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, f"//{tag}[text()='{text}']")))

    return element

# ID로 path 찾기
def id_path(tag, id):
    global driver
    driver = web_driver.driver        
    element =  WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, f'{tag}[id="{id}"]')))

    return element

# Class로 path 찾기
def class_path(tag, class_name):
    global driver
    driver = web_driver.driver        
    element =  WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, f'{tag}[class="{class_name}"]')))

    return element

# placeholder로 path 찾기
def placeholder_path(tag, text):
    global driver
    driver = web_driver.driver        
    element =  WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, f'{tag}[placeholder="{text}"]')))

    return element

# Class명을 통해 Item list 추출
def item_list(element, tag, item):
    driver = web_driver.driver    
    element = driver.find_elements(By.CSS_SELECTOR, f'{tag}[class$="{item}"]')
    button_dic = {}
    for i in element:
        button_dic[i.text] = i
    return button_dic