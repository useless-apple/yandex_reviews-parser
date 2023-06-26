from dataclasses import dataclass
from typing import Union


@dataclass
class Review:
    name: str
    icon_href: Union[str, None]
    date: float
    text: str
    stars: float


@dataclass
class Info:
    name: str
    rating: float
    count_rating: int
    stars: float