import pytest

from src.helpers import ParserHelper


def test_format_rating():
    data = [RatingElement("4")]
    assert ParserHelper.format_rating(data) == 4.0

    data = [RatingElement("3"), RatingElement("5")]
    assert ParserHelper.format_rating(data) == 35.0

    data = [RatingElement("1"), RatingElement("0"), RatingElement("0")]
    assert ParserHelper.format_rating(data) == 100.0

    data = [RatingElement("2"), RatingElement(","), RatingElement("5")]
    assert ParserHelper.format_rating(data) == 2.5

    data = [RatingElement("9"), RatingElement("9"), RatingElement("9"), RatingElement("9")]
    assert ParserHelper.format_rating(data) == 9999.0

    data = []
    assert ParserHelper.format_rating(data) == 0.0

    data = [RatingElement("0")]
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


class RatingElement:
    def __init__(self, text):
        self.text = text
