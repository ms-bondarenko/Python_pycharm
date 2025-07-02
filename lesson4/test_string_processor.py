import pytest
from string_processor import StringProcessor

# def test_string_processor_positive():
#     assert StringProcessor.process("hello") == ("Hello.")
#     assert StringProcessor.process("Hello") == ("Hello.")
#     assert StringProcessor.process("hello_world.") == ("Hello_world.")
#
# def test_string_processor_negative():
#     assert StringProcessor.process("") == (".")
#     assert StringProcessor.process(my_pais) == expected_output
#
# if __name__ == "__main__":
#     pytest.main()

@ pytest.mark.parametrize(
    "input_text, expected_output", [
        ("hello","Hello."),
        ("Hello","Hello."),
        ("Hello world", "Hello world.")
    ]
)
def test_process_positive(input_text, expected_output):
    assert StringProcessor.process(input_text) ==expected_output

@ pytest.mark.parametrize(
    "input_text, expected_output",
    [("", "."), ("    ", "    .")]
)
def test_process_negative(input_text, expected_output):
    assert StringProcessor.process(input_text) == expected_output