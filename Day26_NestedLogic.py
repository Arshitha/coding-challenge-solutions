import sys

dates = []

for line in sys.stdin:
    dates.append(line.strip())

actual_date = dates[0].split(" ")
expected_date = dates[1].split(" ")

if actual_date[0] != expected_date[0] and actual_date[1] == expected_date[1] and actual_date[2]==expected_date[2]:
    fine = 15 * (int(actual_date[0]) - int(expected_date[0]))
elif actual_date[1] != expected_date[1] and actual_date[2]==expected_date[2]:
    fine = 500 * (int(actual_date[1]) - int(expected_date[1]))
elif actual_date[2]!=expected_date[2]:
    fine = 10000
elif actual_date[0] == expected_date[0] and actual_date[1] == expected_date[1] and actual_date[2]==expected_date[2]:
    fine = 0
    
print(fine)
