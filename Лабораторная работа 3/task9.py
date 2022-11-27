salary = 5000  # зарплата
spend = 6000  # траты
months = 10  # количество месяцев
increase = 0.03  # рост цен

money_capital = 0  # количество денег, чтобы прожить 10 месяцев

period = range(months) # задаем кол-во месяцев ( на весь период)
for month in period:
    if month == 0: # установили условие неповышения трат в первый месяц
        money_capital += (spend-salary)
    else:
        spend *= 1 + increase # условие повышения цен на все остальные месяца
        money_capital += (spend-salary)
print(round(money_capital))
