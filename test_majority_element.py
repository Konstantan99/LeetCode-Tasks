from majority_element import Solution  # импортируем проверяемый класс с функцией
import pytest
import random

EPS = 1e-7


@pytest.mark.parametrize(
    'test_input, expected',
    [
        ([2, 2, 1, 1, 1, 2, 2], 2),
        ([1], 1),  # проверяем, если в списке будет один элемент
        ([3, 3, 3, 3, 3, 3, 3, 3], 3)
    ]
)
def test_majority_element(test_input, expected):
    solution = Solution()
    assert abs(solution.majorityElement(test_input) - expected) < EPS


@pytest.fixture(scope="module")
def large_random_input():

    # random.seed(42)
    n_input = 5   #количество проверок
    verify_dict = dict() #создадим словарь, в который будут сохраняться проверяемые списки, а их ключи - ожидаемые значения

    for i in range(n_input):
        list = []
        n_elements_in_list = random.randint(1,5 * 10 ** 4)  # случайным образом определяем, сколько элементов будет в списке
        expected_num = random.randint(-2 ** 31, (2 ** 31 -1))  # случайным образом определяем, число, которого будет больше половины (из условия)
        count_expected = round((1 - random.randint(0, 50) / 100) * n_elements_in_list) + 1 #определяем количество expected_num в списке, чтоб было больше половины

        list = [expected_num for _ in range(count_expected)]

        for _ in range(n_elements_in_list - count_expected):
            list.append(random.randint(-2 ** 31, (2 ** 31 - 1)))

        random.shuffle(list) #перемешаем список

        verify_dict[expected_num] = list #сохраним список, с "правильным ответом" в ключе

    return verify_dict


def test_stress_majority_element(large_random_input):
    for expected in large_random_input.keys():
        solution = Solution()
        assert abs(solution.majorityElement(large_random_input[expected]) - expected) < EPS
