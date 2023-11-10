import sys
import os
import time
from common import web_driver, env
from src import iluminarean, goodvibeworks

is_print = env.is_print
url = env.url

# 과정을 보여드리기 위해 각 1~2초 정도의 딜레이를 줬습니다.
# is_print를 통해 Print 활성화 비 활성화 적용

# 무료 체험 작성 후 취소 과정
def cancel_case():
    case_result_dic = {}

    # 일루미나리안 URL 오픈
    web_driver.open_webdriver(url)
    time.sleep(1)
    close_modal = iluminarean.close_modal()
    if is_print:
        print(close_modal['message'])

    case_result_dic['모달 팝업 종료'] = close_modal['result']

    time.sleep(1)

    click_work = iluminarean.click_menu('Work')
    if is_print:
        print(click_work['message'])

    case_result_dic['Work 진입'] = click_work['result']

    time.sleep(2)

    click_gvw = iluminarean.click_work_menu('GOODVIBE WORKS 바로가기')
    if is_print:
        print(click_gvw['message'])

    case_result_dic['GOODVIBE WORKS 진입'] = click_gvw['result']

    time.sleep(2)

    # Goodvibe Works로 핸들 변경
    if web_driver.driver.current_window_handle == web_driver.driver.window_handles[0]:
        web_driver.driver.switch_to.window(web_driver.driver.window_handles[1])

    click_trial = goodvibeworks.click_free_trial("무료 체험 신청")
    if is_print:
        print(click_trial['message'])

    case_result_dic['무료 체험 신청 진입'] = click_trial['result']

    time.sleep(1)

    input_company_name = goodvibeworks.input_item('companyName', 'SILIN')
    if is_print:
        print(input_company_name['message'])
    
    case_result_dic['회사명 입력'] = input_company_name['result']

    time.sleep(1)

    input_ceo_name = goodvibeworks.input_item('ceoName', 'naslin')
    if is_print:
        print(input_ceo_name['message'])

    case_result_dic['대표자 입력'] = input_ceo_name['result']
    
    time.sleep(1)

    select_business_type = goodvibeworks.select_drop_menu('businessType', '개인')
    if is_print:
        print(select_business_type['message'])

    case_result_dic['사업자 유형 입력'] = select_business_type['result']
    
    time.sleep(1)

    select_scale_type = goodvibeworks.select_drop_menu('scale', '101-200 명')
    if is_print:
        print(select_scale_type['message'])

    case_result_dic['직원수 선택'] = select_scale_type['result']

    time.sleep(1)

    input_name = goodvibeworks.input_item('name', 'naslin')
    if is_print:
        print(input_name['message'])

    case_result_dic['담당자 입력'] = input_name['result']

    time.sleep(1)

    input_email = goodvibeworks.input_item('email', 'sksktlfdls@gmail.com')
    if is_print:
        print(input_email['message'])

    case_result_dic['이메일 입력'] = input_email['result']

    time.sleep(1)

    input_mobile = goodvibeworks.input_item('mobile', '01011111111')
    if is_print:
        print(input_mobile['message'])

    case_result_dic['휴대폰 번호 입력'] = input_mobile['result']

    time.sleep(3)

    choose_work = goodvibeworks.choose_work_menu('경영관리', '재무')
    if is_print:
        print(choose_work['message'])

    case_result_dic['담당 업무 선택'] = choose_work['result']

    time.sleep(1)

    agreeTermsOfUse = goodvibeworks.click_check_box('agreeTermsOfUse')
    if is_print:
        print(agreeTermsOfUse['message'])

    case_result_dic['서비스 이용약관 선택'] = agreeTermsOfUse['result']

    time.sleep(1)

    agreePrivacyStatement = goodvibeworks.click_check_box('agreePrivacyStatement')
    if is_print:
        print(agreePrivacyStatement['message'])

    case_result_dic['개인정보 취급동의 선택'] = agreePrivacyStatement['result']

    time.sleep(1)

    exit_button = goodvibeworks.exit_button()
    if is_print:
        print(exit_button['message'])

    case_result_dic['신청 취소 선택'] = exit_button['result']
    
    time.sleep(1)

    return case_result_dic