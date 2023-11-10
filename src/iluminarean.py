import sys
import os

sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common import element_path

# 초기 모달 팝업 닫기
def close_modal():
    result_dic = {}
    try:
        modal_x_button = element_path.label_path("button", "company:close_modal")
        modal_x_button.click()

        result_dic["result"] = "Success"
        result_dic["message"] = "Modal X Button Click"
        
    except Exception as ex:
        result_dic["result"] = "Fail"
        result_dic["message"] = f'Modal X Button {ex}'

    return result_dic

# work 클릭
def click_menu(menu):
    result_dic = {}
    try:
        menu_button = element_path.text_path("span", menu)
        menu_button.click()

        result_dic["result"] = "Success"
        result_dic["message"] = f"{menu} Click"
        
    except Exception as ex:
        result_dic["result"] = "Fail"
        result_dic["message"] = f'{menu} Click {ex}'
    
    return result_dic

# work 메뉴 클릭
def click_work_menu(menu):
    result_dic = {}
    try:
        goodVibe_works_button = element_path.text_path("a", menu)
        goodVibe_works_button.click()

        result_dic["result"] = "Success"
        result_dic["message"] = f"{menu} Click"
        
    except Exception as ex:
        result_dic["result"] = "Fail"
        result_dic["message"] = f'{menu} Click {ex}'
    
    return result_dic