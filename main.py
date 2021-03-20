#Юлия – предприниматель. Она рационально распределяет свой доход и следит за всеми расходами.
#Для этого она планирует свои траты на каждый месяц в конце предыдущего,
#опираясь на свой средний доход за последние два месяца, который находится в пределах 80.000 – 200.000 р.
#При составлении плана расходов Юлия придерживается следующих правил:
#1.	Каждый месяц Юлия инвестирует 35% заработка, если доход меньше 85.000, и 40%, если больше
#2.	Расходы на коммунальные услуги должны укладываться в 12% от дохода при заработке менее 85.000 и 7%
#при заработке более 85.000
#3.	Транспортные услуги – 5% заработка
#4.	На супермаркеты уходит от 8000 до 20.000 в зависимости от дохода
#5.	Если доход меньше 85.000, расходы на одежду составляют 10% от дохода, если больше, то 15%
#6.	На поддержание здоровья 10% от общего заработка
#7.	Если в месяце есть праздники, то на подарки уходит 10%, если нет, то проценты уходят на инвестиции
#8.	На прочее траты составляют в среднем 8%, если доход меньше 85.000 и 3%, если больше
#Для удобства расчетов, создана программа, планирующая траты.
#Юлии нужно ввести свой предполагаемый доход, название месяца и уточнить, есть в этом месяце праздники,
#после чего выводится таблица всех средних расходов за данный период.


month = input('Enter the name of the month: ')
while True:
    try:
        income = int(input('Enter your estimated income: '))
        celebration = input('Are there any holidays this month? ')
    except ValueError:
        print('Enter an integer')
    else:
        break


def exp_yes(income):
    investment = round(float(income * 0.35), 1)
    utility_bills = round(float(income * 0.12), 1)
    transport = round(float(income * 0.05), 1)
    supermarkets = round(float(income * 0.1), 1)
    clothes = round(float(income * 0.1), 1)
    health_and_beauty = round(float(income * 0.1), 1)
    gifts = round(float(income * 0.1), 1)
    other_expenses = round(float(income * 0.08), 1)
    print('________________________________________________')
    print('|', month.upper(), '                     ')
    print('________________________________________________')
    print('| investment            |', investment)
    print('| utility bills         |', utility_bills)
    print('| transport             |', transport)
    print('| supermarkets          |', supermarkets)
    print('| clothes               |', clothes)
    print('| health and beauty     |', health_and_beauty)
    print('| gifts                 |', gifts)
    print('| other expenses        |', other_expenses)
    print('________________________________________________')


def exp_no(income):
    investment = round(float(income * 0.35), 1)
    utility_bills = round(float(income * 0.12), 1)
    transport = round(float(income * 0.05), 1)
    supermarkets = round(float(income * 0.1), 1)
    clothes = round(float(income * 0.1), 1)
    health_and_beauty = round(float(income * 0.1), 1)
    other_expenses = round(float(income * 0.08), 1)
    print('________________________________________________')
    print('|', month.upper(), '                     ')
    print('________________________________________________')
    print('| investment            |', investment)
    print('| utility bills         |', utility_bills)
    print('| transport             |', transport)
    print('| supermarkets          |', supermarkets)
    print('| clothes               |', clothes)
    print('| health and beauty     |', health_and_beauty)
    print('| other expenses        |', other_expenses)
    print('________________________________________________')


def exp_b_yes(income):
    investment = round(float(income * 0.4), 1)
    utility_bills = round(float(income * 0.07), 1)
    transport = round(float(income * 0.05), 1)
    supermarkets = round(float(income * 0.1), 1)
    clothes = round(float(income * 0.1), 1)
    health_and_beauty = round(float(income * 0.1), 1)
    gifts = round(float(income * 0.1), 1)
    other_expenses = round(float(income * 0.03), 1)
    print('________________________________________________')
    print('|', month.upper(), '                     ')
    print('________________________________________________')
    print('| investment            |', investment)
    print('| utility bills         |', utility_bills)
    print('| transport             |', transport)
    print('| supermarkets          |', supermarkets)
    print('| clothes               |', clothes)
    print('| health and beauty     |', health_and_beauty)
    print('| gifts                 |', gifts)
    print('| other expenses        |', other_expenses)
    print('________________________________________________')


def exp_b_no(income):
    investment = round(float(income * 0.4), 1)
    utility_bills = round(float(income * 0.07), 1)
    transport = round(float(income * 0.05), 1)
    supermarkets = round(float(income * 0.1), 1)
    clothes = round(float(income * 0.1), 1)
    health_and_beauty = round(float(income * 0.1), 1)
    other_expenses = round(float(income * 0.03), 1)
    print('________________________________________________')
    print('|', month.upper(), '                     ')
    print('________________________________________________')
    print('| investment            |', investment)
    print('| utility bills         |', utility_bills)
    print('| transport             |', transport)
    print('| supermarkets          |', supermarkets)
    print('| clothes               |', clothes)
    print('| health and beauty     |', health_and_beauty)
    print('| other expenses        |', other_expenses)
    print('________________________________________________')

if 80000 <= income < 85000 and celebration.lower() == 'yes':
    exp_yes(income)
elif 80000 <= income < 85000 and celebration.lower() == 'no':
    exp_no(income)
elif 85000 <= income < 200000 and celebration.lower() == 'yes':
    exp_b_yes(income)
elif 85000 <= income < 200000 and celebration.lower() == 'no':
    exp_b_no(income)
else:
    print('Check the correctness of the entered data')
