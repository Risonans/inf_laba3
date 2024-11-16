from my_lib import *
import pytest

#Тестируем корректный ввод и вывод
@pytest.mark.parametrize("a, b, expected_result", [([3, 2, 1, 7], 1, [1, 2, 3, 7]), 
                                                   ([3, 2, 1, 7], 2, [7, 3, 2, 1])])
    
def test_on_correct_bubble(a, b, expected_result):
    assert bubble(a, b) == expected_result