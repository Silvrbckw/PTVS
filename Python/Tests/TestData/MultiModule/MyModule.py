class SchoolMember:
	'''Representsany school member.'''
	def __init__(self,name,age):
		self.name = name
		self.age = age
		print(f'Initialized Schoolmember: {self.name}')

	def tell(self):
		'''Tell my detail.'''
		print(f'Name: "{self.name}" Age: "{self.age}"')
            
def sayHi():
	print ('Hi, this is mymodule speaking.')

version='0.1'