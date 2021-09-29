def is_year_leap(year):
    if year % 4 != 0:
        return False
    elif year % 100 != 0:
        return True
    elif year % 400 != 0:
        return False
    else:
        return True


def days_in_month(year, month):
    # year_result = is_year_leap(year)
    # print("Is", year, "a Leap Year?", year_result)
    if is_year_leap(year):
        if month == 2:
            return 29
        elif (month % 7) % 2 == 0:
            return 30
        else:
            return 31
    else:
        if month == 2:
            return 28
        elif (month % 7) % 2 == 0:
            return 30
        else:
            return 31


def day_of_year(year, month, day):

    if month == 1:
        year_num = year - 1
        m = 11
    elif month == 2:
        year_num = year - 1
        m = 12
    else:
        year_num = year
        m = (month - 2) % 12
    y = year_num % 100
    c = year_num // 100
    x = int(2.6 * m - 0.2)
    return (day + x + y + y//4 + c//4 - 2*c) % 7


def create_calender():
    week1 = []
    for i in range(number):
        week1.append('-')
    a = 1
    for i in range(number, 7):
        week1.append(a)
        a += 1
    print(week1)
    week2 = []
    for i in range(7):
        week2.append(a)
        a += 1
    print(week2)
    week3 = []
    for i in range(7):
        week3.append(a)
        a += 1
    print(week3)
    week4 = []
    for i in range(7):
        week4.append(a)
        a += 1
    print(week4)
    week5 = []
    for i in range(7):
        week5.append(a)
        a += 1
        if a == number_of_days + 1:
            break
    print(week5)


week = ['Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday']
number_of_days = days_in_month(1986, 6)
number = day_of_year(1986, 6, 1)
print(number)
print(number_of_days)
create_calender()

