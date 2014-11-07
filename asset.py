class Asset:
	def __init__(self):
		self.category = ''
		self.name = ''
		self.value = {'begin':0, 'now':0, 'end':0}
	
	def set(self, name, begin, now, end):
		self.name = name
		self.value['begin'] = begin
		self.value['now'] = now
		self.value['end'] = end

	def __repr__(self):
		return 'Asset:{0},{1},{2},{3},{4}'.format(self.category, self.name, self.value['now'], self.value['begin'], self.value['end'])


class Current_Asset(Asset):
	def __init__(self):
		Asset.__init__(self)
		self.category = 'current asset'

class Fixed_Asset(Asset):
	def __init__(self):
		Asset.__init__(self)
		self.category = 'fixed asset'



Current = Current_Asset()
Current.set('stock', 10000, 20000, 15000)
print(Current)
Fixed = Fixed_Asset()
Fixed.set('stock', 10000, 20000, 15000)
print(Fixed)
