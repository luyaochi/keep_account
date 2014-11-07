import bank

from account import Account

#bank
luyaochi_bank = bank.Account()
luyaochi_bank.set('lukelu','0021179-0664447',67619.00,'')
#cash
luyaochi = Account(1061)

luyaochi.add_expense(item='drink-tea',value=25, date='2014/11/04')
luyaochi.add_expense(item='drink-water',value=25, date='2014/11/04')
luyaochi.add_expense(item='dinner',value=200, date='2014/11/04')
luyaochi.add_income(item='a',value=6000, date='2014/11/04')
luyaochi.add_expense(item='drink',value=23, date='2014/11/05')

luyaochi.add_expense(item='breakfist',value=50, date='2014/11/05')
luyaochi.add_expense(item='drink',value=23, date='2014/11/05')
luyaochi.add_expense(item='dinner',value=100, date='2014/11/05')

luyaochi.add_expense(item='breakfist',value=50, date='2014/11/06')
luyaochi.add_expense(item='drink',value=45, date='2014/11/06')
luyaochi.add_expense(item='dinner',value=70, date='2014/11/06')

luyaochi.add_expense(item='breakfist',value=50, date='2014/11/07')
luyaochi.add_expense(item='dinner',value=89, date='2014/11/07')

#budget
from budget import Pre_expenditure

pre_expediture_list = Pre_expenditure()
pre_expediture_list.add_item(item_name='food', value=150, type1='day')
pre_expediture_list.add_item(item_name='drink', value=20, type1='day')
pre_expediture_list.add_item(item_name='trafic', value=1000, type1='month')
pre_expediture_list.add_item(item_name='other', value=5000, type1='month')
pre_expediture_list.del_item(item_name='other', value=5000, type1='month')



print('------------------------------------')
day_budget_total = 0
month_budget_total = 0
year_budget_total = 0

for item in pre_expediture_list.pre_expenditure_list:
	print(item)
	if item['type1'] == 'day':
		day_budget_total += item['value']
		month_budget_total += item['value']*30
		year_budget_total += item['value']*365

	if item['type1'] == 'month':
		month_budget_total += item['value']
		year_budget_total += item['value']*12

	if item['type1'] == 'year':
		year_budget_total += item['value']

		

print('day:' + str(day_budget_total))
print('month:' + str(month_budget_total))
print('season:' + str(4*month_budget_total))
print('year:' + str(year_budget_total))
print('------------------------------------')
print('cash:' + str(luyaochi.overcash))
print('bank:' + luyaochi_bank.__str__())
print('total:' + str(luyaochi.overcash + luyaochi_bank.balance))

