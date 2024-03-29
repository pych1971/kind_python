year = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
month, day = map(int, input().split())
if day == 1:
    month_previous = month - 1
    day_previous = year[month_previous - 1]
    month_next = month
    day_next = 2
elif day == year[month - 1]:
    month_previous = month
    day_previous = day - 1
    month_next = month + 1
    day_next = 1
else:
    month_previous = month
    day_previous = day - 1
    month_next = month
    day_next = day + 1
print(
    f"{str(month_previous).rjust(2, '0')}.{str(day_previous).rjust(2, '0')} {str(month_next).rjust(2, '0')}.{str(day_next).rjust(2, '0')}")
