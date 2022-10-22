workdays = int(input())
daily_profit = float(input())
currency_rate = float(input())

month_salary = (workdays * daily_profit)
annual_bonus = 2.5 * month_salary
annual_salary = month_salary * 12 + annual_bonus
taxes = 0.25 * annual_salary
total_salary = annual_salary - taxes
average_daily_profit = (total_salary / 365) * currency_rate
print(round(average_daily_profit, 2))
