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
        # Creating 2D array for seat structure
        two_d_array = []
        for _ in range(self.rows):
            single_row = [0] * self.cols
            two_d_array.append(single_row)
        # Attatching the Seat 2D array
        # To the show id in the seats dict()
        self.seats[id] = two_d_array

        # ------------------------------------------
        # Didn't work due to
        # all the rows are holding
        # the same reference
        # self.seats[id] = [[0] * self.cols] * self.rows
        # ------------------------------------------

    def book_seats(self, id: str, seat_numbers: List[Tuple]):
        seats = self.seats.get(id, None)
        if seats is None:
            return f"Given Movie id: {id} is wrong"
        for seat_num in seat_numbers:
            row, col = seat_num
            seats[row][col] = 1

    def view_show_list(self):
        print(self.show_list)

    def view_available_seats(self, id: str):
        seats = self.seats.get(id, None)
        if seats is None:
            return f"Given Movie id: {id} is wrong"
        print(seats)

    def __repr__(self) -> str:
        return f"This is hall : {self.hall_no}"
