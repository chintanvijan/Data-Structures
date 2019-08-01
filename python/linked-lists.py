class node:
	def __init__(self,dataval):
		self.dataval = dataval
		self.nextval = None

class linkedlist:
	def __init__(self):
		self.headval=None

	def traverse(self):
		val = self.headval
		while val is not None:
			print(val.dataval)
			val = val.nextval

	def insbeg(self,dataval):
		if self.headval == None:
			self.headval = node(dataval)
		else:
			t = self.headval
			self.headval = node(dataval)
			self.headval.nextval = t

	def insend(self,dataval):
		val = self.headval
		if val == None:
			val = node(dataval)
			val.nextval = None 
		else:
			while val is not None:
				prev = val
				val = val.nextval
			t = node(dataval)
			prev.nextval = t

	def delbeg(self):
		self.headval = self.headval.nextval

ch='y'
llist = linkedlist()
while ch=='y':
	print("Enter 1 to insert a at beginning node into linked list")
	print("Enter 2 to insert a node at last into linked list")
	print("Enter 3 to delete a node from linked list")
	print("Enter 4 to traverse the linked list")
	inp = int(input())
	if inp == 1:
		dataval = input("Enter data value to be inserted")
		llist.insbeg(dataval)
		print("Successfully inserted node")
	if inp ==2:
		dataval = input("Enter data value to be inserted")
		llist.insend(dataval)
		print("Successfully inserted node")
	if inp ==3:
		llist.delbeg()
		print("Successfully deleted node")
	if inp == 4:
		llist.traverse()
	ch = input("Want to continue?(y/n)")



