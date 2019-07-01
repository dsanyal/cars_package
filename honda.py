class honda: 

	def __init__(self): 
		self.models = ['Amaze', 'City', 'Accord', 'Brio', 'Jazz', 'WRV','CRV'] 
   
	def outModels(self): 
		print('These are the available models for Honda: ') 
		for model in self.models: 
			print('%s ' % model)

	def prices(self,model):
		prices_of_models = {'amaze':750000,
							'city': 1200000,
							'accord': 3000000,
							'brio': 400000,
							'jazz': 500000}
		print('The price of {} is {} INR'.format(model, prices_of_models[model]))

	def hback_or_sedan_or_suv(self,model):
		if model in ['Brio', 'Jazz']:
			print('{} is a hatchback!'.format(model))
		elif model in ['City', 'Amaze','Accord']:
			print('{} is a sedan!'.format(model))
					elif model in ['CRV', 'WRV']:
			print('{} is an SUV!'.format(model))
		else:
			print('Model not found!')
					



if (__name__ == '__main__'):
    print('Executing as standalone script:')  
    print('Ths module defines the class honda')    			