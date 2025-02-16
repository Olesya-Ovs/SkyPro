from typing import Any

from src.decorators import division, log


def test_log_1(capsys: Any) -> None:
    division(2, 0)
    captured = capsys.readouterr()
    assert 'Функция division завершила работу с ошибкой division by zero Inputs:(2, 0), {}' in captured.out


def test_log_2(capsys: Any) -> None:
    @log(filename=None)
    def division(x: int, y: int) -> float:
        return x / y

    division(2, 1)
    captured = capsys.readouterr()
    assert captured.out == 'Функция division завершила работу с результатом 2.0\n'
