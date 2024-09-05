from lib.Hall import Hall

h1 = Hall(6, 6, "Hall-001")

h1.entry_show("Show-001", "Yes Man", "2024-09-05:20:30")

h1.book_seats("Show-001", [(0, 0), (0, 1)])

h1.view_available_seats("Show-001")
