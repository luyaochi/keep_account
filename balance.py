class Balance:
	def __init__(self):
			self.balance = {'assets':[], 'liabilities':[]}
			self.sum_balance = {'asset':0, 'liability':0, 'over':0}
			self.over = 0

#assets add, delete, read
	def add_asset(self, **asset):
		self.balance['assets'].append(asset)

	def del_asset(self, **asset):
		for item in self.balance['assets']:
			if item['number'] in asset['number']:
				self.balance['assets'].remove(item)

	def show_assets(self):
		print('Asssets:{0}'.format(self.balance['assets']))
		

#liabilities add, delete, read
	def add_liability(self, **liability):
		self.balance['liabilities'].append(liability)

	def del_liability(self, **liability):
		for item in self.balance['liabilities']:
			if item['number'] in liability['number']:
				self.balance['liabilities'].remove(item)

	def show_liabilities(self):
		print('Liabilities:{0}'.format(self.balance['liabilities']))

# show balance_sheet
	def show_balance(self):
		print('Balance Sheet:')
		assets = self.balance['assets']
		liabilities = self.balance['liabilities']
		print('Asssets:{0}'.format(assets))
		print('Liabilites:{0}'.format(liabilities))

