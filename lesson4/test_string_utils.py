import pytest
from string_utils import StringUtils

class TestStringUtils:

    @pytest.fixture
    def string_utils(self):
        return StringUtils()

    @pytest.mark.parametrize(
        "input_str, expected", [
            ("skypro", "Skypro"),
            ("sKYPRO", "Skypro"),
            ("sky pro", "Sky pro"),
            ("sky Pro", "Sky pro"),
            ("Sky Pro", "Sky pro")
        ])
    def test_capitalize_positive(self, string_utils, input_str, expected):
        assert string_utils.capitalize(input_str) == expected

    @pytest.mark.parametrize(
        "input_str, expected", [
            ("", ""),  # empty string
            ("    ", "    "),  # a string of spaces
            ("123abc", "123abc")  # a string of numbers
        ])
    def test_capitalize_negative(self, string_utils, input_str, expected):
        assert string_utils.capitalize(input_str) == expected

    @pytest.mark.parametrize(
        "input_str, expected", [
            (" SkyPro ", "SkyPro"),
            (" Sky Pro ", "Sky Pro"),
            (" Sky_Pro ", "Sky_Pro")
        ])
    def test_trim_positive(self, string_utils, input_str, expected):
        assert string_utils.trim(input_str) == expected

    @pytest.mark.parametrize(
        "input_str, expected", [
            ("", ""),
            ("    ", "")
        ])
    def test_trim_negative(self, string_utils, input_str, expected):
        assert string_utils.trim(input_str) == expected

    @pytest.mark.parametrize(
        "input_str, symbol, expected", [
            ("Skypro", "S", True),
            ("Skypro", "y", True),
            ("Skypro", "o", True),
            ("12345", "3", True),
            ("Skypro", "", True)
        ])
    def test_contains_positive(self, string_utils, input_str, symbol, expected):
        assert string_utils.contains(input_str, symbol) == expected

    @pytest.mark.parametrize(
        "input_str, symbol, expected", [
            ("", "r", False),
            ("12345", "6", False),
            ("Skypro", "s", False)
        ])
    def test_contains_negative(self, string_utils, input_str, symbol, expected):
        assert string_utils.contains(input_str, symbol) == expected

    @pytest.mark.parametrize(
        "input_str, symbol, expected", [
            ("Skypro", "S", "kypro"),
            ("Skypro", "pro", "Sky")
        ])
    def test_delete_symbol_positive(self, string_utils, input_str, symbol, expected):
        assert string_utils.delete_symbol(input_str, symbol) == expected

    @pytest.mark.parametrize(
        "input_str, symbol, expected", [
            ("", "S", ""),
            ("Skypro", "z", "Skypro")
        ])
    def test_delete_symbol_negative(self, string_utils, input_str, symbol, expected):
        assert string_utils.delete_symbol(input_str, symbol) == expected