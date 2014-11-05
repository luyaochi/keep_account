import bank

from account import Account

#bank
bank_acct = bank.Account('lukelu','0021179-0664447',67619.00)

#cash
cash_acct = Account(1061)
cash_acct.add_item(item='drink-tea',value=25, type1='cost', date='2014/11/04')
cash_acct.add_item(item='drink-water',value=25, type1='cost', date='2014/11/04')
cash_acct.add_item(item='dinner',value=200, type1='cost', date='2014/11/04')
cash_acct.add_item(item='a',value=6000, type1='income', date='2014/11/04')
cash_acct.add_item(item='drink',value=23, type1='cost', date='2014/11/05')

cash_acct.add_item(item='breakfist',value=50, type1='cost', date='2014/11/05')
cash_acct.add_item(item='drink',value=23, type1='cost', date='2014/11/05')
cash_acct.add_item(item='dinner',value=100, type1='cost', date='2014/11/05')

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

		

print('month:' + str(day_budget_total))
print('season:' + str(month_budget_total))
print('year:' + str(year_budget_total))

print('------------------------------------')
print('cash:' + str(cash_acct.acct['cash']))
print('bank:' + bank_acct.__str__())
print('total:' + str(cash_acct.acct['cash'] + bank_acct.balance))