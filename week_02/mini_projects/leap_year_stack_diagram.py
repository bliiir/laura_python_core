'''
--------------------------------------------------------
                LEAP YEAR + STACK DIAGRAM
--------------------------------------------------------

Construct a function according to the following description,
then draw a stack diagram of an execution with ‘2000’ as input.

-- DESCRIPTION --
We add a Leap Day on February 29, almost every four years.
The leap day is an extra, or intercalary day and we add it to the
shortest month of the year, February. In the Gregorian calendar
three criteria must be taken into account to identify leap years:

- The year can be evenly divided by 4, is a leap year, unless:
  - The year can be evenly divided by 100, it is NOT a leap year, unless:
    - The year is also evenly divisible by 400. Then it is a leap year.

This means that in the Gregorian calendar, the years 2000 and 2400 are
leap years, while 1800, 1900, 2100, 2200, 2300 and 2500 are NOT leap years.

-- TASK --
You are given the year, and you have to write a function to check
if the year is leap or not.

Input Format:
Read y, the year that needs to be checked.

Constraints:
1900 <= y <= 10**5

Output Format:
Your function must return a boolean value (True/False)

-- STACK DIAGRAM --
You can use the viz mode here:
http://www.pythontutor.com/visualize.html#mode=edit
for better visual understanding and support in creating the stack diagram.

'''
print("Please enter a year to determine if it is a leap year:")
year_input = int(input())


def is_leap_year(y):
    if y >= 1900 and y <= 10**5:
        if y % 4 == 0:
            if y % 100 == 0 and y % 400 > 0:
                is_leap = False
            else:
                is_leap = True
        else:
            is_leap = False
    else:
        is_leap = None
        print("Please enter a year from 1900 up to 100,000.")
    return is_leap


print(is_leap_year(year_input))

''' Stack diagram below

              --------------------
<module>     | year_input -> 2000 |
              --------------------
             |     y      -> 2000 |
 is_leap_year|  is_leap   -> True |
             |return value -> True|
              --------------------

'''
