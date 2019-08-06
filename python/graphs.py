class graph:
	def __init__(self,gdict):
		if gdict is None:
			gdict = {}
		self.gdict = gdict

	def listallvertices(self):
		return list(self.gdict.keys())

graph_elements = { "a" : ["b","c"],
          "b" : ["a", "d"],
          "c" : ["a", "d"],
          "d" : ["e"],
          "e" : ["d"]
         }
g = graph(graph_elements)
print(g.listallvertices())
