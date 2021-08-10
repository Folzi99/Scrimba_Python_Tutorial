# You sell lemonade over two weeks, the lists show number of lemonades sold per week
# Profit for each lemonade is $1.5
### add another day to week 2 list by capturing a number as input - DONE
### combine the two lists into the list called 'sales' - DONE

### calculate/print how much you have earned on - DONE
####  best day, worst day, separately and in total
# Hint: 3 prints in total

sales_w1 = [7,3,42,19,15,35,9]
sales_w2 = [12,4,26,10,7,28]
sales = []

new_day = input('New Day:')
sales_w2.append(int(new_day))

#   sales.extend(sales_w1)
#   sales.extend(sales_w2)
sales = sales_w1 + sales_w2
sales.sort()

worst_day_prof = sales[0] * 1.5
#   worst_day_prof = min(sales) * 1.5
best_day_prof = sales[-1] * 1.5
#   best_day_prof = max(sales)* 1.5
print(f'Worst day of prof:$ {worst_day_prof}')
print(f'Best day of prof:$ {best_day_prof}')
print(f'Combined Profit:$ {worst_day_prof + best_day_prof}')
