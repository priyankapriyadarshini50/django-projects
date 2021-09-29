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
    week = ['Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday']
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
    number = (day + x + y + y//4 + c//4 - 2*c) % 7

    return week[number]


test_years = [1900, 2000, 2016, 1987, 2021]
test_months = [2, 1, 3, 11, 4]
test_days = [6, 1, 4, 18, 10]
test_results = ['Tuesday', 'Saturday', 'Friday', 'Wednesday', 'Saturday']
for i in range(len(test_years)):
    yr = test_years[i]
    mo = test_months[i]
    dt = test_days[i]
    print("Year:", yr, "," "Month:", mo, ",", "Date:", dt, end=' ')
    number_of_days = days_in_month(yr, mo)
    print("Number of Days:", number_of_days, "->", end='')
    result_day = day_of_year(yr, mo, dt)
    print(result_day)
    if result_day == test_results[i]:
        print("OK")
    else:
        print("Failed")

