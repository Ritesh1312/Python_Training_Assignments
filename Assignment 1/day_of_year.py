def get_week_day_name(index):
    if index == 0:
        print("Sunday")
    elif index == 1:
        print("Monday")
    elif index == 2:
        print("Tuesday")
    elif index == 3:
        print("Wednesday")
    elif index == 4:
        print("Thursday")
    elif index == 5:
        print("Friday")
    elif index == 6:
        print("Saturday")


def is_leap_year(year):
        return (year%100!=0 and year%4==0) or year%400==0


def days_in_month(month, year=1990):
    if month == 2:
        return 28 + int(is_leap_year(year))
    elif (month<8 and month%2!=0) or (month>=8 and month%2==0):
        return 31
    else:
        return 30 
    

def date_value(day, month, year):
    value = 0
    y = year - 1
    value = y * 365 + y//4 - y//100 + y//400
    m = 1
    while m < month :
        value += days_in_month(m, year)
        m+=1

    value+=day

    return value


def week_day_name(date, month, year):
    ref_date = date_value(1,1,2006)
    input_date = date_value(date, month, year)
    diff = (input_date- ref_date) % 7
    get_week_day_name(diff)

week_day_name(30,1,1948)
week_day_name(21,9,2023)