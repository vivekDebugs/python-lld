from typing import TYPE_CHECKING, List

if TYPE_CHECKING:
    from show import Show

class Movie:
    def __init__(self, name: str, duration: int):
        self.name = name
        self.duration = duration
        self.shows: List['Show'] = []

    def addShow(self, show: 'Show'):
        self.shows.append(show)