from unittest.mock import mock_open, patch
from src.pre_built.counter import count_ocurrences


def test_counter():
    file = "Python Javascript python javascript Python Javascript python"

    with patch("builtins.open", mock_open(read_data=file)):
        assert count_ocurrences("dummy", "Javascript") == 3
        assert count_ocurrences("dummy", "Python") == 4
