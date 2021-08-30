month_31d = {"jan", "mar", "may", "jul", "aug", "sep",  "oct", "dec"}
month_30d = {"apr", "jun", "sep", "nov"}
month_28d = {"feb"}

def num_days(month):

    if month in month_31d:
        print('number of days in ', month, ' is', 31)
    elif month in month_30d:
        print('number of days in ', month, 'is', 30)
    elif month:
        print('number of days in ', month, 'is', 28)
    else:
        print("that is not a month")

user = input("enter a month: ")

num_days(user)
# optimize/shorten the code in the function
# try to reduce the number of conditionals

# SOLUTION

def num_days(month):
    days = 31
    if month in {'apr', 'jun', 'sep', 'nov'}:
        # if month == 'apr' or month =='jun' or month =='sep' or month =='nov':
        days = 30
    elif month == 'feb':
        days = 28
    print('number of days in', month, 'is', days)


num_days('jan')