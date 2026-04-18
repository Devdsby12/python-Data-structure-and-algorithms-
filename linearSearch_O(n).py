# find which home in the city have theif
houses_in_city = [{"house number": "1" , "has_thief": False}, {"house number": "2", "has_thief": True, "phoneip": "134.00.4.5"}, {"house number": "3", "has_thief": False}]
for house in houses_in_city:
    if house.get("phoneip") == "134.00.4.5":
        print("The thief is in house number " + house.get("house number"))
