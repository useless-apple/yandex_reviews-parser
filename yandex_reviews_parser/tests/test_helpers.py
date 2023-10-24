import pytest

from src.helpers import ParserHelper


def test_format_rating():
    data = ["4"]
    assert ParserHelper.format_rating(data) == 4.0

    data = ["3", "5"]
    assert ParserHelper.format_rating(data) == 35.0

    data = ["1", "0", "0"]
    assert ParserHelper.format_rating(data) == 100.0

    data = ["2", ",", "5"]
    assert ParserHelper.format_rating(data) == 2.5

    data = ["9", "9", "9", "9"]
    assert ParserHelper.format_rating(data) == 9999.0

    data = []
    assert ParserHelper.format_rating(data) == 0.0

    data = ["0"]
    assert ParserHelper.format_rating(data) == 0.0


def test_list_to_num():
    l = ["123"]
    assert ParserHelper.list_to_num(l) == 123

    l = ["-456"]
    assert ParserHelper.list_to_num(l) == -456

    l = ["3.14"]
    assert ParserHelper.list_to_num(l) == 3

    l = ["-2.5"]
    assert ParserHelper.list_to_num(l) == -2

    l = ["0"]
    assert ParserHelper.list_to_num(l) == 0

    l = ["abc", "123", "def"]
    assert ParserHelper.list_to_num(l) == 123

    l = []
    with pytest.raises(IndexError):
        ParserHelper.list_to_num(l)

    l = ["abc", "def"]
    with pytest.raises(ValueError):
        ParserHelper.list_to_num(l)


def test_form_date():
    date = "2022-01-01T00:00:00.000Z"
    assert ParserHelper.form_date(date) == 1640977200.0

    date = "2023-06-26T12:34:56.789Z"
    assert ParserHelper.form_date(date) == 1687764896.789

    date = "2021-09-15T23:59:59.999Z"
    assert ParserHelper.form_date(date) == 1631732399.999

