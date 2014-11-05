class Pre_expenditure:
	def __init__(self):
		self.pre_expenditure_list = []

	def add_item(self, **item):
		self.pre_expenditure_list.append(item)

	def del_item(self, **item):
		self.pre_expenditure_list.remove(item)

	def __repr__(self):
		return 'Account({0})'.format(self.pre_expenditure_list)
