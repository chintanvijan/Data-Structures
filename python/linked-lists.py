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
		while val is not None:
			prev = val
			val = val.nextval
		t = node(dataval)
		prev.nextval = t

	def delbeg(self):
		self.headval = self.headval.nextval

		
llist = linkedlist()
llist.headval = node("Sunday")
v1 = node("Monday")
llist.headval.nextval = v1
v2 = node("Tuesday")
v1.nextval = v2 
#llist.traverse()
llist.insbeg("Saturday")
#llist.traverse()
llist.insend("Wednesday")
#llist.traverse()
llist.delbeg()
#llist.traverse()
llist.delend()
llist.traverse()



