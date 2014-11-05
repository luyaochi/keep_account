class Account:
	def __init__(self, cash):
		self.user_info = {'username':'', 'birthday':'', 'gender':''}
		self.cashflow_statement = {'incomes':[], 'expenses':[]}
		self.balance_sheet = {'asssets':[], 'liabilities':[]}

#expense add, delete, read
	def add_expense(self, **expense):
		self.cashflow_statement['expenses'].append(expense)

	def del_expense(self, **expense):
		for item in self.cashflow_statement['expenses']:
			if item['item'] in expense['item']:
				self.cashflow_statement['expenses'].remove(item)

	def show_expenses(self, **expense):
		print('Expenses:{0}'.format(self.cashflow_statement['expenses']))

#income add, delete, read
	def add_income(self, **income):
		self.cashflow_statement['incomes'].append(income)

	def del_income(self, **income):
		for item in self.cashflow_statement['incomes']:
			if item['item'] in income['item']:
				self.cashflow_statement['incomes'].remove(item)

	def show_incomes(self):
		print('Incomes:{0}'.format(self.cashflow_statement['incomes']))

# show cashflow_statement
	def show_cashflow_statement(self):
		print('Cashflow Statement:')
		incomes = self.cashflow_statement['incomes']
		expenses = self.cashflow_statement['expenses']
		print('Incomes:{0}'.format(incomes))
		print('Expenses:{0}'.format(expenses))
		
#assets add, delete, read
	def add_asset(self, **asset):
		self.balance_sheet['asssets'].append(asset)

	def del_asset(self, **asset):
		for item in self.balance_sheet['asssets']:
			if item['number'] in asset['number']:
				self.balance_sheet['asssets'].remove(item)

	def show_assets(self):
		print('Asssets:{0}'.format(self.balance_sheet['asssets']))
		

#liabilities add, delete, read
	def add_liability(self, **liability):
		self.balance_sheet['liabilities'].append(liability)

	def del_liability(self, **liability):
		for item in self.balance_sheet['liabilities']:
			if item['item'] in liability['item']:
				self.balance_sheet['liabilities'].remove(item)

	def show_liabilities(self):
		print('Asssets:{0}'.format(self.balance_sheet['liabilities']))
	