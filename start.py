from case import test_case
import inquirer

# 테스트 리스트를 선택 할 수 있게 적용
test_list = [
    inquirer.List('testType',
                message="Choose an option:",
                choices=["CancelCase", "SuccessCase"],
                ),
]
test = inquirer.prompt(test_list)
test_type = test["testType"]

if test_type == "CancelCase":
    test_result_dic = test_case.cancel_case()
    result_li = []
    print("--------Case Result------------")
    for item, result in test_result_dic.items():
        result_li.append(result)
        print(f'{item} : {result}')

    print("--------Total Result------------")
    print(f"Total : {len(result_li)}")
    print(f"Pass  : {result_li.count('Success')}")
    print(f"Fail : {result_li.count('Fail')}")

elif test_type == "SuccessCase":
    print("죄송합니다 아직 이런 케이스는 없습니다.")