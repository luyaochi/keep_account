from balance import Balance



myaccount = Balance()
#asset
myaccount.add_asset(type1='bank',name='lukelu',number='0021179-0664447',balance=67619.00)
myaccount.add_asset(type1='bank',name='lukelu',number='0021179-0664448',balance=67619.00)
myaccount.del_asset(type1='bank',name='lukelu',number='0021179-0664448',balance=67619.00)
myaccount.show_assets()
#liability
myaccount.add_liability(type1='bank',name='lukelu',number='0021179-0664447',balance=67619.00)
myaccount.add_liability(type1='bank',name='lukelu',number='0021179-0664448',balance=67619.00)
myaccount.del_liability(type1='bank',name='lukelu',number='0021179-0664448',balance=67619.00)
myaccount.show_liabilities()

myaccount.show_balance()
