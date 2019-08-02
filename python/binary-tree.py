class node:
	def __init__(self,data):
		self.data = data
		self.left = None
		self.right = None

	def insert(self,data):
		if self.data:
			if data < self.data:
				if self.left is None:
					self.left = node(data)
				else:
					self.left.insert(data)
			elif data > self.data:
				if self.right is None:
					self.right = node(data)
				else:
					self.right.insert(data)
		else:
			self.data = data

	def traverse(self):
		
		if self.left:
			self.left.traverse()
		print(self.data)
		if self.right:
			self.right.traverse()

root = node(12)
ch = 'y'
while ch == 'y':
	print("Enter 1 to insert node")
	print("Enter 2 to traverse")
	inp = int(input())
	if inp == 1:
		data = int(input("Enter data to be inserted:"))
		root.insert(data)
	if inp == 2:
		root.traverse()
	ch = input("Want to continue?(y/n)")