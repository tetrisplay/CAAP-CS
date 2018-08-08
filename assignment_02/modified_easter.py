def easter():
    year = int(input("Enter a year between 1982 and 2048"))

    while year < 1900 or year > 2099:
        print("Invalid Year")
        year = int(input("Enter a year between 1982 and 2048"))

    a = year % 19
    b = year % 4
    c = year % 7
    d = (19*a + 24) % 30
    e = (2*b + 4*c + 6*d + 5) % 7

    day = 22 + d + e

    if year == 1954 or year == 1981 or year == 2049 or year == 2076:
        day -= 7

    if day > 31:
        print("Easter occurs on April", day - 31 "in the year" year)
    else:
        print("Easter falls on March", day "in the year" year)

easter()
