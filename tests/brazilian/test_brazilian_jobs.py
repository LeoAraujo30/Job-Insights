from unittest.mock import mock_open, patch
from src.pre_built.brazilian_jobs import read_brazilian_file


def test_brazilian_jobs():
    file = "titulo,salario,tipo\nMaquinista,2000,trainee\nMotorista,3000,full"

    with patch("builtins.open", mock_open(read_data=file)):
        assert "title" in read_brazilian_file("dummy")[0]
        assert "salary" in read_brazilian_file("dummy")[1]
