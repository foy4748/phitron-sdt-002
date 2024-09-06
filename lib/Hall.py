from typing import List, Tuple
from lib.Star_Cinema import Star_Cinema


# == Task 2 ==
class Hall(Star_Cinema):
    def __init__(self, rows: int, cols: int, hall_no: str) -> None:
        # == Task 9 ==
        self.__rows = rows
        self.__cols = cols
        self.__hall_no = hall_no
        self.__seats = dict()
        self.__remaining_seats_number = dict()
        self.__show_list: List[Tuple] = list()
        super()._entry_hall(self)

    # == Task 3 ==
    def entry_show(self, id: str, movie_name: str, time: str):
        self.__show_list.append((id, movie_name, time))
        # Creating 2D array for seat structure
        two_d_array = []
        for _ in range(self.__rows):
            single_row = [0] * self.__cols
            two_d_array.append(single_row)
        # Attatching the Seat 2D array
        # To the show id in the seats dict()
        self.__seats[id] = two_d_array
        self.__remaining_seats_number[id] = self.__rows * self.__cols
        # ------------------------------------------
        # Didn't work due to
        # all the rows are holding
        # the same reference
        # self.seats[id] = [[0] * self.cols] * self.rows
        # ------------------------------------------

    # == Task 4 ==
    def book_seats(self, id: str, seat_numbers: List[Tuple]):
        seats = self.__seats.get(id, None)
        if seats is None:
            return f"Given Movie id: {id} is wrong"
        for seat_num in seat_numbers:
            row, col = seat_num
            seats[row][col] = 1
        # Reducing remaining seat number
        self.__remaining_seats_number[id] = self.__remaining_seats_number[id] - len(
            seat_numbers
        )

    # == Task 5 ==
    def view_show_list(self):
        print("Show List\n")
        print("#  id\t\tTime\t\t\tMovie")
        for i, show in enumerate(self.__show_list):
            id, movie, _time = show
            print(f"{i+1}) {id}\t{_time}\t{movie}")

    # == Task 6 ==
    def view_available_seats(self, id: str):
        seats = self.__seats.get(id, None)
        if seats is None:
            return f"Given Movie id: {id} is wrong"
        for row in seats:
            print(row)
        print(f"\n{self.remaining_seat_count(id)} seats remaining")

    # Getter methods ---------------------

    def get_seats(self, id: str):
        return self.__seats.get(id, None)

    def get_show_id(self, idx: int):
        try:
            return self.__show_list[idx][0]
        except:
            return None

    def show_count(self):
        return len(self.__show_list)

    def remaining_seat_count(self, id: str):
        return self.__remaining_seats_number.get(id, None)

    # Validator methods ------------------

    def isSeatInHall(self, row: int, col: int):
        # User input:
        # 1 based idx
        if row < 1 or row > self.__rows or col < 1 or col > self.__cols:
            return False
        return True

    def isSeatBooked(self, id: str, row: int, col: int):
        # User input:
        # 1 based idx
        row = row - 1
        col = col - 1
        if self.__seats[id][row][col] == 1:
            return True
        return False

    # Static Methods ---------------------

    @staticmethod
    def isDuplicate(row: int, col: int, seat_numbers: List[Tuple]):
        # User input:
        # 1 based idx
        row = row - 1
        col = col - 1
        for item in seat_numbers:
            row_ = item[0]
            col_ = item[1]
            if row == row_ and col == col_:
                return True
        return False

    # -----------------------------------
    def __repr__(self) -> str:
        return f"This is hall : {self.__hall_no}"
