import pytest
from string_utils import StringUtils


string_utils = StringUtils()


@pytest.mark.positive
@pytest.mark.parametrize("input, res", [
    ("", ""),
    ("skypro", "Skypro"),
    ("hello world", "Hello world"),
    ("ПРИВЕТ", "Привет"), 
    ("строка с символами $%&", "Строка с символами $%&"),
    ("строка с цифрами 23435436", "Строка с цифрами 23435436"),
])
def test_capitalize_positive(input, res):
    assert string_utils.capitalize(input) == res

#capitalize
@pytest.mark.xfail()
@pytest.mark.negative
@pytest.mark.parametrize("input, res", [
    (12121212, "12121212"), 
    (None, "None"), 
])
def test_capitalize_negative(input, res):
    assert string_utils.capitalize(input) == res

#trim
@pytest.mark.positive
@pytest.mark.parametrize("input, res", [
    ("test", "test"), 
    (" test", "test"), 
    (" Удаление пробелов только в начале ", "Удаление пробелов только в начале "), 
])
def test_trim_positive(input, res):
    assert string_utils.trim(input) == res


@pytest.mark.xfail()
@pytest.mark.negative
@pytest.mark.parametrize("input, res", [
    ([ ], ""), 
    ( False, "False"), 
])
def test_trim_negative(input, res):
    assert string_utils.trim(input) == res


#contains
@pytest.mark.positive
@pytest.mark.parametrize("string, symbol, result", [
    ("test", "s", True), 
    ("1232143", "2", True), 
    ("test string", "m", False), 
    ("", "a", False), 
])
def test_contains_positive(string, symbol, result):
    result = symbol in string
    assert string_utils.contains(string, symbol) == result


@pytest.mark.xfail()
@pytest.mark.negative
@pytest.mark.parametrize("string, symbol, result", [
    (123, "3", True), 
])
def test_contains_negative(string, symbol, result):
    result = symbol in string
    assert string_utils.contains(string, symbol) == result


#delete_symbol
@pytest.mark.positive
@pytest.mark.parametrize("string, symbol, result", [
    ("test", "e", "tst"), 
    ("SkyPro", "Pro", "Sky"),
    ("Строка с пробелами", "т", "Срока с пробелами"),
])
def test_delete_symbol_positive(string, symbol, result):
    assert string_utils.delete_symbol(string, symbol) == result

@pytest.mark.xfail()
@pytest.mark.negative
@pytest.mark.parametrize("string, symbol, result", [
    (123456, "2", "13456"), 
    (["test"], "s", "tet"),
])
def test_delete_symbol_negative(string, symbol, result):
    assert string_utils.delete_symbol(string, symbol) == result