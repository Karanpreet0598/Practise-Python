from datetime import date

x = date.today()
curr_year = x.year

name = input(print("Enter your name:"))
age = int(input(print("Enter your age:")))
copy = int(input("How many copies do you want for the message:"))

diff: int = 100 - age

target_year = curr_year + diff - 1

i = 0
while(i<=copy):
    print("{}, you will become 100 in the year{}\n".format(name, target_year))
    i += 1