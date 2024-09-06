from lib.Hall import Hall

h1 = Hall(6, 6, "Hall-001")
h1.entry_show("S-001", "Yes Man", "2024-09-05:20:30")
h1.entry_show("S-002", "Full Metal Jacket", "2024-09-12:20:30")

keepRunning = True
rememberLast = False
option = -1

while keepRunning:

    if rememberLast is False:
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
            rememberLast = False
            h1.view_show_list()
        case 2:
            # Selecting Show
            if rememberLast is False:
                h1.view_show_list()

            rememberLast = False

            show_number = -1
            show_count = h1.show_count()
            try:
                show_number = int(input("\nEnter show number: "))
            except:
                if show_count == 1:
                    print("There is only one show. Please, Enter 1")
                else:
                    print(f"Enter between 1 and {show_count}")
                rememberLast = True
            if show_number < 1 or show_number > show_count:
                print(f"Enter between 1 and {show_count}")
                rememberLast = True
                continue

            print()

            id = h1.get_show_id(show_number - 1)
            # -------------------

            if id is None:
                print("\nInvalid show number")
                rememberLast = True
                continue

            seats = h1.get_seats(id)
            if seats is None:
                print(f"There is no show for id {id}")
                continue
            print("\nShowing available seats. (Marked as 0)")
            h1.view_available_seats(id)
        case 3:
            # Selecting Show
            if rememberLast is False:
                h1.view_show_list()

            rememberLast = False

            show_number = -1
            show_count = h1.show_count()
            try:
                show_number = int(input("\nEnter show number: "))
            except:
                if show_count == 1:
                    print("There is only one show. Please, Enter 1")
                else:
                    print(f"Enter between 1 and {show_count}")
                rememberLast = True
            if show_number < 1 or show_number > show_count:
                print(f"Enter between 1 and {show_count}")
                rememberLast = True
                continue

            print()
            id = h1.get_show_id(show_number - 1)
            # -------------------

            if id is None:
                print("\nInvalid show number")
                rememberLast = True
                continue

            h1.view_available_seats(id)
            num_of_seats = 0

            try:
                num_of_seats = int(input("\nEnter number of tickets needed: "))
            except:
                print("\nEnter a valid number of seats")
                rememberLast = True
                continue

            # Checking whether given number of
            # seats available or not
            remaining_seat_count = h1.remaining_seat_count(id)

            if remaining_seat_count is None:
                print("\n Invalid Show.")
                rememberLast = True
                continue

            if num_of_seats > remaining_seat_count:
                print(f"\n{num_of_seats} seats are not available right now.")
                print(f"\n{remaining_seat_count} seats remaining")
                rememberLast = True
                continue

            require_seats = []

            # Booking Seats
            i = 1
            while num_of_seats:
                row = -1
                col = -1
                try:
                    row = int(input(f"\nFor Seat {i} Input Row no: "))
                    col = int(input(f"For Seat {i} Input Col no: "))
                except:
                    print("\nEnter valid input, Please")
                    continue

                # Duplicate entry validation
                isDuplicated = Hall.isDuplicate(row, col, require_seats)

                if isDuplicated is True:
                    print(f"\nRow {row} and Col {col} is already Entered")
                    continue

                if h1.isSeatInHall(row, col) is False:
                    print(f"\nRow {row} and Col {col} is not within the hall")
                    continue
                if h1.isSeatBooked(id, row, col) is True:
                    print(f"\nRow {row} and Col {col} is already booked")
                    continue

                # Doing validation before allowing
                # append new seat
                tup = (row - 1, col - 1)
                require_seats.append(tup)

                # Increamenting seat input prompt index
                i = i + 1
                num_of_seats = num_of_seats - 1

            # Booking seat if everything is OK
            h1.book_seats(id, require_seats)

        case 4:
            rememberLast = False
            print("Exiting...")
            keepRunning = False

    print("----------------")
