import sys
i = 4
d = 4.0
s = "HackerRank"
# Declare second integer, double, and String variables.
integer = 0
double = 0.0
string = ""

# Read and save an integer, double, and String to your variables.
ipList = []
for each in sys.stdin:
    ipList.append(each.replace('\n', ''))

integer = int(ipList[0])
double = float(ipList[1])
string = ipList[2]

# Print the sum of both integer variables on a new line.
print(integer + i)

# Print the sum of the double variables on a new line.
print(double + d)

# Concatenate and print the String variables on a new line
# The 's' variable above should be printed first.
print(s + string)
