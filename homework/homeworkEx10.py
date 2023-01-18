import pytest

phrase = input("Set a phrase: ")

class TestLen:
    def test_length(self):
        more_symbols = 16
        assert len(phrase) < more_symbols, f"Фраза более 15 символов"
