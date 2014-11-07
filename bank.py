class Account:
	def __init__(self):
		self.name = ''
		self.number = ''
		self.balance = 0
		self.category = ''

	def set(self, name, number, balance, category):
		self.name = name
		self.number = number
		self.balance = balance
		self.category = category

	def deposit(self, amount):
		if amount <= 0:
			raise ValueError('amount must be postive')

	def withdraw(self, amount):
		if amount > self.balance:
			raise RuntimerError('balance not enough')
		self.balance -= amount

	def __str__(self):
		return 'Account({0},{1},{2})'.format(self.name, self.number, self.balance  )