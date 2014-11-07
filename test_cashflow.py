from cashflow import Cashflow

test_cashflow = Cashflow(1000)

test_cashflow.add_expense(item='drink-tea',value=25, date='2014/11/04')
test_cashflow.add_expense(item='drink-water',value=25, date='2014/11/04')
test_cashflow.add_expense(item='dinner',value=200, date='2014/11/04')
test_cashflow.del_expense(item='dinner',value=200, date='2014/11/04')
test_cashflow.add_income(item='drink-tea',value=25, date='2014/11/04')
test_cashflow.del_income(item='drink-tea',value=25, date='2014/11/04')
test_cashflow.show_expenses()
test_cashflow.show_incomes()
test_cashflow.show_cashflow()