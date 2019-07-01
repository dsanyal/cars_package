class bmw: 

    def __init__(self): 
        self.models = ['320d', '530d', '730ld','x1', 'x3', 'x5'] 
   
    def outModels(self): 
        print('These are the available models for BMW') 
        for model in self.models: 
            print('%s ' % model) 

	def prices(self,model):
		prices_of_models = {'320d':3800000,
							'530d': 6500000,
							'730ld': 13000000,
							'x1': 3000000,
							'x3': 6000000,
							'x5': 12000000}
		print('The price of {} is {} INR'.format(model, prices_of_models[model]))

	def hback_or_sedan_or_suv(self,model):
		if model in ['320d', '530d', '730ld']:
			print('{} is a sedan!'.format(model))
		elif model in ['x1', 'x3','x5']:
			print('{} is an SUV!'.format(model))
		else:
			print('Model not found!')



if (__name__ == '__main__'):
    print('Executing as standalone script:')  
    print('Ths module defines the class BMW')          