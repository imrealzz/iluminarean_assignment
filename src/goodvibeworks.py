import sys
import os
import time
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common import element_path, web_driver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

# 무료 체험 신청 클릭
def click_free_trial(menu):
    result_dic = {}
    try:
        free_trial_button = element_path.text_path("button", menu)
        free_trial_button.click()

        result_dic["result"] = "Success"
        result_dic["message"] = f"{menu} Click"
        
    except Exception as ex:
        result_dic["result"] = "Fail"
        result_dic["message"] = f'{menu} Click {ex}'
    
    return result_dic

# 아이템 입력
def input_item(id, text):
    result_dic = {}
    try:
        free_trial_button = element_path.id_path("input", id)
        free_trial_button.send_keys(text)

        result_dic["result"] = "Success"
        result_dic["message"] = f"Input {text}"
        
    except Exception as ex:
        result_dic["result"] = "Fail"
        result_dic["message"] = f'Input {text} {ex}'
    
    return result_dic

# 드롭다운 선택
def select_drop_menu(id, menu):
    result_dic = {}
    driver = web_driver.driver
    action = web_driver.action
    try:
        drop_menu = element_path.id_path("div", id)
        drop_menu.click()
        
        action.move_to_element(drop_menu).perform()
        sub_menu = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, f"//div[text()='{menu}']")))
        sub_menu.click()

        result_dic["result"] = "Success"
        result_dic["message"] = f"{menu} Click"
        
    except Exception as ex:
        result_dic["result"] = "Fail"
        result_dic["message"] = f'{menu} Click {ex}'

    return result_dic

# 담당 업무 선택
def choose_work_menu(choose_text, input_text):
    result_dic = {}
    try:
        action = web_driver.action
        driver = web_driver.driver

        choose_work_element = element_path.class_path('dl', 'duties')
        choose_work_button = choose_work_element.find_element(By.CSS_SELECTOR, 'button')
        action.move_to_element(choose_work_button).perform()
        choose_work_button.click()

        button_dic = element_path.item_list(choose_work_button, 'button', 'el0tj996')
        for item, element in button_dic.items():
            if choose_text == item:
                element.click()

        time.sleep(2)
        input_text_element = element_path.placeholder_path('input', '업무명 검색')
        action.move_to_element(input_text_element).perform()
        input_text_element.send_keys(input_text)

        button_dic[input_text].click()
        
        # 등록
        registration = element_path.text_path('button', '등록')
        action.move_to_element(registration).perform()
        if registration.is_enabled():
            registration.click()

            result_dic["result"] = "Success"
            result_dic["message"] = f"Input {choose_text}, {input_text}"
        else:
            result_dic["result"] = "Fail"
            result_dic["message"] = f"등록 버튼 비활성화"
            
            return result_dic
        
    except Exception as ex:
        result_dic["result"] = "Fail"
        result_dic["message"] = f'Input {choose_text}, {input_text} {ex}'
    
    return result_dic

# 체크박스 선택
def click_check_box(item):
    result_dic = {}
    try:
        free_trial_button = element_path.id_path("input", item)
        free_trial_button.click()

        result_dic["result"] = "Success"
        result_dic["message"] = f"Click {item}"
        
    except Exception as ex:
        result_dic["result"] = "Fail"
        result_dic["message"] = f'Click {item} {ex}'
    
    return result_dic

# 신청 취소
def exit_button():
    result_dic = {}
    try:
        element = element_path.text_path('span', '신청 취소')
        x_button = element_path.par_path(element)
        x_button.click()

        confirm_button = element_path.text_path('button', '확인')
        confirm_button.click()

        result_dic["result"] = "Success"
        result_dic["message"] = f"Click X Button"
    
    except Exception as ex:
        result_dic["result"] = "Fail"
        result_dic["message"] = f'Click X Button {ex}'
    
    return result_dic