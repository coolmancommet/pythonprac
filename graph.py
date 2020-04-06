class node:
	def __init__(self,data):
		self.vertex=data
		self.next=None
class graph:
	def __init__(self,vertex):
		self.graph=[None]*vertex
	def addnode(self,scr,dest):
		nod=node(dest)
		nod.next=self.graph[scr]
		self.graph[scr]=nod

		nodd=node(scr)
		nodd.next=self.graph[dest]
		self.graph[dest]=nodd
	def printgr(self):
		for x in self.graph:
			t=x
			while t:
				print("-> {}".format(t.vertex), end=" ")
				t=t.next
			print("/n")
if __name__=="__main__":
	graph=graph(5)
	graph.addnode(0,1) 
	graph.addnode(0,4)
	graph.addnode(1,2)
	graph.addnode(1,3)
	graph.addnode(1,4)
	graph.addnode(2,3)
	graph.addnode(3,4)
	graph.printgr()
