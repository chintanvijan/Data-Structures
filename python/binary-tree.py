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

	def search_value(self,val):
		if val<self.data:
			if self.left == None:
				return str(val)+":Not Found"
			return self.left.search_value(val)
		elif val > self.data:
			if self.right == None:
				return str(val)+":Not Found"
			return self.right.search_value(val)
		else:
			return print(str(val)+":Found")

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
	print("Enter 3 to Search in tree")
	inp = int(input())
	if inp == 1:
		data = int(input("Enter data to be inserted:"))
		root.insert(data)
	if inp == 2:
		root.traverse()
	if inp == 3:
		val = int(input("Enter value to be searched:"))
		print(root.search_value(val))
	ch = input("Want to continue?(y/n)")










