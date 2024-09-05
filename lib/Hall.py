from typing import List, Tuple
from lib.Star_Cinema import Star_Cinema


class Hall(Star_Cinema):
    def __init__(self, rows: int, cols: int, hall_no: str) -> None:
        self.rows = rows
        self.cols = cols
        self.hall_no = hall_no
        self.seats = dict()
        self.show_list: List[Tuple] = list()
        super()._entry_hall(self)

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
        print("Show List\n")
        print("#  id\t\tTime\t\t\tMovie")
        for i, show in enumerate(self.show_list):
            id, movie, _time = show
            print(f"{i+1}) {id}\t{_time}\t{movie}")

    def view_available_seats(self, id: str):
        seats = self.seats.get(id, None)
        if seats is None:
            return f"Given Movie id: {id} is wrong"
        for row in seats:
            print(row)

    # Validator methods
    def isSeatInHall(self, row: int, col: int):
        # User input:
        # 1 based idx
        if row < 1 or row > self.rows or col < 1 or col > self.cols:
            return False
        return True

    def isSeatBooked(self, id: str, row: int, col: int):
        # User input:
        # 1 based idx
        row = row - 1
        col = col - 1
        if self.seats[id][row][col] == 1:
            return True
        return False

    @staticmethod
    def isDuplicate(row: int, col: int, seat_numbers: List[Tuple]):
        for seat in seat_numbers:
            _row, _col = seat
            row = row - 1
            col = col - 1
            if _row == row and _col == col:
                return True
        return False

    def __repr__(self) -> str:
        return f"This is hall : {self.hall_no}"
