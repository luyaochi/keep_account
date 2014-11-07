from cashflow import Cashflow
from balance import Balance

class Account(Cashflow,Balance):
	def __init__(self, cash):
		Cashflow.__init__(self, cash)
		Balance.__init__(self)
		self.user_info = {'username':'', 'birthday':'', 'gender':''}





