class Cashflow:
	def __init__(self, overcash):
			self.cashflow = {'incomes':[], 'expenses':[]}
			self.sum_cashflow = {'income':0, 'expense':0, 'overcash':overcash}
			self.overcash = 0

#expense add, delete, read
	def add_expense(self, **expense):
		self.cashflow['expenses'].append(expense)
		self.add_cashflow('expense', expense)
		self.calculte_cash()

	def del_expense(self, **expense):
		for item in self.cashflow['expenses']:
			if item['item'] in expense['item']:
				self.cashflow['expenses'].remove(item)
				self.del_cashflow('expense', item)
				self.calculte_cash()

	def show_expenses(self, **expense):
		print('Expenses:{0}'.format(self.cashflow['expenses']))

#income add, delete, read
	def add_income(self, **income):
		self.cashflow['incomes'].append(income)
		self.add_cashflow('income', income)
		self.calculte_cash()

	def del_income(self, **income):
		for item in self.cashflow['incomes']:
			if item['item'] in income['item']:
				self.cashflow['incomes'].remove(item)
				self.del_cashflow('income', item)
				self.calculte_cash()

	def show_incomes(self):
		print('Incomes:{0}'.format(self.cashflow['incomes']))

#calculate income or expense
	def add_cashflow(self, type1, item):
		self.sum_cashflow[type1] += item['value']

	def del_cashflow(self,type1, item):
		self.sum_cashflow[type1] -= item['value']


#calculate cash
	def calculte_cash(self):
		sum_cashflow = self.sum_cashflow
		self.overcash = sum_cashflow['income'] - sum_cashflow['expense'] + sum_cashflow['overcash']

# show cashflow_statement
	def show_cashflow(self):
		print('Cashflow Statement:')
		incomes = self.cashflow['incomes']
		expenses = self.cashflow['expenses']
		print('Incomes:{0}'.format(incomes))
		print('Expenses:{0}'.format(expenses))







class Cashflow_Factory:
	def __init__(self, type):
		self.type = type

	def add(self):
		return lambda y : y+1
	def delete(self):
		pass
	def show(self):
		pass

	def add_income(self, **income):
		self.cashflow['incomes'].append(income)
		self.add_cashflow('income', income)

	def del_income(self, **income):
		for item in self.cashflow['incomes']:
			if item['item'] in income['item']:
				self.cashflow['incomes'].remove(item)
				self.del_cashflow('income', item)

	def show_incomes(self):
		print('Incomes:{0}'.format(self.cashflow['incomes']))

#calculate income or expense
	def add_cashflow(self, type1, item):
			self.sum_cashflow[type1] += item['value']

	def del_cashflow(self,type1, item):
			self.sum_cashflow[type1] -= item['value']


#calculate cash
	def calculte_cash(self):
		sum_cashflow = self.sum_cashflow
		self.cash = sum_cashflow['income'] - sum_cashflow['expense'] + sum_cashflow['overcash']


