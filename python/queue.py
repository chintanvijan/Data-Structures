class node:
	def __init__(self,dataval):
		self.dataval = dataval
		self.nextval = None

class queue:
	def __init__(self):
		self.headval = None

	def push(self,dataval):
		if self.headval == None:
			self.headval = node(dataval)
		else:
			val = self.headval
			while val is not None:
				prev = val
				val = val.nextval
			prev.nextval=node(dataval)

	def pop(self):
		if self.headval == None:
			print("Can't pop! Queue is empty.")
		else:
			self.headval = self.headval.nextval
	def trav(self):
		val = self.headval
		while val is not None:
			print(val.dataval)
			val = val.nextval

qu = queue()
ch = "y"
while ch=="y":
	print("Enter 1 to push elements into queue")
	print("Enter 2 to pop elements from queue")
	print("Enter 3 to traverse queue")
	inp = int(input())
	if inp == 1:
		dataval = input("Enter element to pushed into queue:")
		qu.push(dataval)
		print("Push Successfull!")
	if inp == 2:
		qu.pop()
		print("Pop Successfull!")
	if inp ==3:
		qu.trav()
	ch = input("Want to continue?(y/n)")










