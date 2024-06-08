
def test_func(s):

    return True


# 测试数据
CASES = [
    {
        'input_data': ["flower", "flow", "flight"],
        'output_data':"fl"
    }, {
        'input_data': ["dog", "racecar", "car"],
        'output_data':""
    }, ]


# 测试所有用例
def test_cases():
    is_pass = True
    for i in range(len(CASES)):
        is_pass = test_case(i) and is_pass
    return is_pass


# 测试指定用例
def test_case(case_num):
    is_pass = run_test_func(case_num)
    return is_pass


def run_test_func(case_num):
    input_data = CASES[case_num]["input_data"]
    output_data = CASES[case_num]["output_data"]

    print(f'>>> 开始测试用例{case_num}: ')
    print(f'测试数据：{input_data}')

    result = test_func(input_data)
    is_pass = result == output_data

    print(f'执行结果：{result}')
    print(f'期待结果：{output_data}, 是否通过： {is_pass}')


test_cases()
# test_case(0)
