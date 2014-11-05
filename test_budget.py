from budget import Pre_expenditure

pre_expediture_list = Pre_expenditure()
pre_expediture_list.add_item(item_name='food', value=150, type1='day')
pre_expediture_list.add_item(item_name='drink', value=20, type1='day')
pre_expediture_list.add_item(item_name='trafic', value=1000, type1='month')
pre_expediture_list.add_item(item_name='other', value=5000, type1='month')


pre_expediture_list.del_item(item_name='other', value=5000, type1='month')


for item in pre_expediture_list.pre_expenditure_list:
	print(item)