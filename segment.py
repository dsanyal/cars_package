# Python module to find the segment of a car
class car_segment: 

	segments = {'i10': 'A1', 'Xcent': 'A2',  'Santro': 'A2', 'i20': 'A2',
	 'Verna': 'A3', 'Tucson': 'SUV', 'creta' : 'compact SUV', 
	 'Amaze': 'A2', 'City': 'A3', 'Accord': 'A5', 'Brio': 'A1', 
	 'Jazz': 'A2', 'Elantra': 'A4', 'CRV': 'SUV', 'WRV': 'compact SUV',
	 '320d': 'A4', '530d': 'A5', '730ld': 'A6', 'x1': 'SUV', 'x3': 'SUV', 'x5': 'SUV'
	} #class variable
	def __init__(self, car_model): 
		self.car_model = car_model
		print('You have selected the  model: {}'.format(self.car_model))
  
	def find_segment(self):      
		segment = self.segments[self.car_model] 
		print('{} belongs to {} segment according to Society of Indian Automobile Manufacturers'.format(self.car_model, segment)) 
		