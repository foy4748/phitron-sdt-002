from lib.Hall import Hall

h1 = Hall(6, 6, "Hall-001")
h1.entry_show("S-001", "Yes Man", "2024-09-05:20:30")
h1.entry_show("S-002", "Full Metal Jacket", "2024-09-12:20:30")

keepRunning = True

while keepRunning:
    print(
        """
    ----------------
    1. VIEW ALL SHOW TODAY
    2. VIEW AVAILABLE SEATS
    3. BOOK TICKET
    4. EXIT
    ----------------
            """
    )
    option = int(input())
    print("----------------")
    match option:
        case 1:
            h1.view_show_list()
        case 2:
            # Selecting Show
            h1.view_show_list()
            show_number = int(input("\nEnter show number: "))
            print()
            id = h1.show_list[show_number - 1][0]
            # -------------------

            seats = h1.seats.get(id, None)
            if seats is None:
                print(f"There is no show for id {id}")
                continue
            print("Showing available seats. (Marked as 0)")
            h1.view_available_seats(id)
        case 3:
            # Selecting Show
            h1.view_show_list()
            show_number = int(input("\nEnter show number: "))
            print()
            id = h1.show_list[show_number - 1][0]
            # -------------------

            h1.view_available_seats(id)
            num_of_seats = int(input("\nEnter number of tickets needed: "))
            require_seats = []

            # Booking Seats
            i = 1
            while num_of_seats:
                row = int(input(f"For Seat {i} Input Row no: "))
                col = int(input(f"For Seat {i} Input Col no: "))

                isDuplicate = Hall.isDuplicate(row, col, require_seats)

                # Calling validators
                if isDuplicate:
                    print(f"Row {row} and Col {col} is already entered")
                    continue
                if h1.isSeatInHall(row, col) is False:
                    print(f"Row {row} and Col {col} is not within the hall")
                    continue
                if h1.isSeatBooked(id, row, col) is True:
                    print(f"Row {row} and Col {col} is already booked")
                    continue

                tup = (row - 1, col - 1)
                require_seats.append(tup)

                # Increamenting seat input prompt index
                i = i + 1
                num_of_seats = num_of_seats - 1

            # Booking seat if everything is OK
            h1.book_seats(id, require_seats)

        case 4:
            print("Exiting...")
            keepRunning = False
    print("----------------")
