

def test_func(input_data):
    haystack = input_data['haystack']
    needle = input_data['needle']

    # if haystack == needle:
    #     return 0

    len_haystack = len(haystack)
    len_needle = len(needle)

    if len_haystack < len_needle:
        return -1

    for i in range(len_haystack - len_needle + 1):
        # print('test info:', i, haystack[i: i + len_needle])
        if haystack[i: i + len_needle] == needle:
            return i
    return -1


# 测试数据
CASES = [{
    'input_data': {
        'haystack': "sadbutsad",
        'needle': "sad"},
    'output_data': 0
}, {
    'input_data': {
        'haystack': "leetcode",
        'needle': "leeto"},
    'output_data': -1
}, {
    'input_data': {
        'haystack': "a",
        'needle': "a"},
    'output_data': 0
}, {
    'input_data': {
        'haystack': "abc",
        'needle': "c"},
    'output_data': 2
}]


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
# test_case(3)
