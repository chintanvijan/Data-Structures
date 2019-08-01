class node:
	def __init__(self,dataval):
		self.dataval=dataval
		self.nextval = None

class stack:
	def __init__(self):
		self.headval = None

	def push(self,dataval):
		if self.headval == None:
			self.headval = node(dataval)
		else :
			t = self.headval
			self.headval = node(dataval)
			self.headval.nextval = t

	def pop(self):
		if self.headval==None:
			print("Stack is Empty! Can't pop")
		else:
			self.headval = self.headval.nextval

	def traverse(self):
		val = self.headval
		while val is not None:
			print(val.dataval)
			val = val.nextval

st = stack()
ch = 'y'
while ch=='y':
	print("Enter 1 to push elements into stack")
	print("Enter 2 to pop elements from stack")
	print("Enter 3 to traverse stack")
	inp = int(input())
	if inp == 1:
		dataval = input("Enter data to be inserted into stack:")
		st.push(dataval)
		print("Push Successfull!")
	if inp == 2:
		st.pop()
		print("Pop Successfull!")
	if inp == 3:
		st.traverse()
	ch = input("Want to continue?(y/n)")
