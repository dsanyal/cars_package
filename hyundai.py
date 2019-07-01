class hyundai: 

	def __init__(self):  #constructor which instantiates the object
		self.models = ['i10', 'i20',  'Xcent',  'Santro',  'Verna', 'Tucson', 'Creta', 'Elantra'] 


	def outModels(self): 
		print('These are the available models for Hyundai')
		for model in self.models:
			print('%s ' %model) 

	def prices(self,model):
		prices_of_models = {'i10':750000,
							'Xcent': 1200000,
							'Santro': 3000000,
							'i20': 400000,
							'Verna': 1250000,
							'Tucson': 2400000}
		print('The price of {} is {} INR'.format(model, prices_of_models[model]))

	def hback_or_sedan_or_suv(self,model):
		if model in ['i10', 'i20', 'Santro']:
			print('{} is a hatchback!'.format(model))
		elif model in ['Xcent', 'Verna', 'Elantra']:
			print('{} is a sedan!'.format(model))
		elif model in ['Creta', 'Tucson']:
			print('{} is an SUV!'.format(model))
		else:
			print('Model not found!')



if (__name__ == '__main__'):
    print('Executing as standalone script:')  
    print('Ths module defines the class hyundai')  

