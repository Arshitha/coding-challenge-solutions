import sys

dates = []

for line in sys.stdin:
    dates.append(line.strip())

actual_date = dates[0].split(" ")
expected_date = dates[1].split(" ")

actual_day = int(actual_date[0])
actual_month = int(actual_date[1])
actual_year = int(actual_date[2])

expected_day = int(expected_date[0])
expected_month = int(expected_date[1])
expected_year = int(expected_date[2])

fine = 0
if (actual_day < expected_day or actual_day == expected_day) and actual_month == expected_month and actual_year == expected_year:
    fine = 0
elif actual_day > expected_day and actual_month == expected_month and actual_year == expected_year:
    fine = 15 * (actual_day - expected_day)
elif actual_month > expected_month and actual_year == expected_year:
    fine = 500 * (actual_month - expected_month)
elif actual_year > expected_year:
    fine = 10000
    
print (fine)
