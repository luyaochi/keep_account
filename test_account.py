from account import Account

#old

myaccount = Account(1000)
print(myaccount)
myaccount.add_item(item='food',value=100, type1='cost', date='2014/02/26')
print(myaccount)
myaccount.add_item(item='letto',value=100, type1='income', date='2014/02/26')
print(myaccount)
myaccount.del_item(item='letto', value=100, type1='income')
print(myaccount)
myaccount.del_item(item='food', value=100, type1='cost')
print(myaccount)
myaccount.del_item(item='food', value=100, type1='cost')


#new update
#rename and rewrite method
myaccount.add_expense(item='food',value=100, date='2014/02/26')
myaccount.add_expense(item='letto',value=100, date='2014/02/26')
myaccount.del_expense(item='letto', value=100)
myaccount.show_expenses()


myaccount.add_income(item='food',value=100, date='2014/02/26')
myaccount.add_income(item='letto',value=100, date='2014/02/26')
myaccount.del_income(item='letto', value=100)
myaccount.show_incomes()

myaccount.show_cashflow_statement()

myaccount.add_asset(type1='bank',name='lukelu',number='0021179-0664447',balance=67619.00)
myaccount.add_asset(type1='bank',name='lukelu',number='0021179-0664448',balance=67619.00)
myaccount.del_asset(type1='bank',name='lukelu',number='0021179-0664448',balance=67619.00)
myaccount.show_assets()


myaccount.add_liability(type1='bank',name='lukelu',number='0021179-0664447',balance=67619.00)
myaccount.add_liability(type1='bank',name='lukelu',number='0021179-0664448',balance=67619.00)
myaccount.del_liability(type1='bank',name='lukelu',number='0021179-0664448',balance=67619.00)
myaccount.show_liabilities()