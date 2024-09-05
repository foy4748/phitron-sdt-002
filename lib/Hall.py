from typing import List, Tuple
from lib.Star_Cinema import Star_Cinema


class Hall(Star_Cinema):
    def __init__(self, rows: int, cols: int, hall_no: str) -> None:
        self.rows = rows
        self.cols = cols
        self.hall_no = hall_no
        self.seats = dict()
        self.show_list: List[Tuple] = list()
        super().entry_hall(self)

    def entry_show(self, id: str, movie_name: str, time: str):
        self.show_list.append((id, movie_name, time))
        # Thans to GeeksForGeeks
        # https://www.geeksforgeeks.org/python-using-2d-arrays-lists-the-right-way/
        self.seats[id] = [[0] * self.cols] * self.rows

    def __repr__(self) -> str:
        return f"This is hall : {self.hall_no}"
