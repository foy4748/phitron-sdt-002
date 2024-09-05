from lib.Hall import Hall
from lib.Star_Cinema import Star_Cinema

h1 = Hall(6, 6, "Hall-001")

h1.entry_show("Show-001", "Yes Man", "2024-09-05:20:30")

print(h1.seats["Show-001"])
