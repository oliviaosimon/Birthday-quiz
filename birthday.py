"""
birthday.py
Author: Olivia Simon
Credit: None
Assignment:

Your program will ask the user the following questions, in this order:

1. Their name.
2. The name of the month they were born in (e.g. "September").
3. The year they were born in (e.g. "1962").
4. The day they were born on (e.g. "11").

If the user's birthday fell on October 31, then respond with:

  You were born on Halloween!

If the user's birthday fell on today's date, then respond with:

  Happy birthday!

Otherwise respond with a statement like this:

  Peter, you are a winter baby of the nineties.

Example Session

  Hello, what is your name? Eric
  Hi Eric, what was the name of the month you were born in? September
  And what year were you born in, Eric? 1972
  And the day? 11
  Eric, you are a fall baby of the stone age.
"""
from datetime import datetime
from calendar import month_name
todayMonth = datetime.today().month

name = input("Hello, what is your name? ")

#MONTH OF BIRTH
birthMonth = input("Hi "+name+", what was the name of the month you were born in? ")
if birthMonth == "December" or birthMonth== "January" or birthMonth== "February":
    season = "winter baby"
elif birthMonth == "March" or birthMonth== "April" or birthMonth== "May":
    season = "spring baby"
elif birthMonth == "June" or birthMonth== "July" or birthMonth== "August":
    season = "summer baby"

#YEAR OF BIRTH
birthYear = input("And what year were you born in, "+name+"? ")
if birthYear < 1980:
    period = "stone age"
elif birthYear == range(1980,1989,1):
    period = "eighties"
elif birthYear == range(1990,1999,1):
    period = "nineties"
elif birthYear >= 2000:
    period = "two thousands"

#DAY OF BIRTH
birthDay = input("And the day? ")
if int(birthDay) == datetime.today().day and birthMonth == month_name[todayMonth]:
    print("Happy Birthday!")
elif int(birthDay) == 31 and birthMonth == "October":
    print("You were born on Halloween!")
elif int(birthDay) == 25 and birthMonth == "December":
    print("You were born on Christmas!")
else:
    print(name+", you are a "+season+" of the "+period+".")

