'''冒泡排序算法
    请用Python语言实现冒泡排序算法，把较大的数字放在后面。注意：默认所有的偶数都比奇数大
    >>> numbers = [23, 32, 1, 3, 4, 19, 20, 2, 4]
    >>> magic_bubble_sort(numbers)
    [1, 3, 19, 23, 2, 4, 4, 20, 32]
'''


def magic_bubble_sort(numbers):
    """冒泡排序，较大数在后，默认偶数比奇数大
    :param numbers: [int]
    """

    stop_position = len(numbers) - 1
    while stop_position > 0:

        for i in range(stop_position):

            current, next_ = numbers[i], numbers[i + 1]
            current_is_even, next_is_even = current % 2 == 0, next_ % 2 == 0
            should_swap = False

            # 交换位置的两条件：
            # - 前面偶数，后面奇数
            # - 前面和后面同为奇数或偶数，且前面大于后面
            if current_is_even and not next_is_even:
                should_swap = True
            elif current_is_even == next_is_even and current > next_:
                should_swap = True

            if should_swap:
                numbers[i], numbers[i + 1] = numbers[i + 1], numbers[i]

        stop_position -= 1


if __name__ == '__main__':
    numbers = [23, 32, 1, 3, 4, 19, 20, 2, 4]
    magic_bubble_sort(numbers)
    print(numbers)
