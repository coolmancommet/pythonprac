from collections import defaultdict

class graph:
	def __init__(self):
		self.graph=defaultdict(list)

	def addnode(self,u,v):
		self.graph[u].append(v)
	def printBFS(self,t):
		visited =[False]*(len(self.graph))
		queue=[]
		visited[t]=True
		queue.append(t)
		while queue:
			s=queue.pop(0)
			print(s,end="")
			for i in self.graph[s]:
				if visited[i]==False:
					queue.append(i)
					visited[i]=True 
if __name__=="__main__":
	gg=graph()
	gg.addnode(0,1)
	gg.addnode(0,2)
	gg.addnode(1,2)
	gg.addnode(2,0)
	gg.addnode(2,3)
	gg.addnode(3,3)
	gg.printBFS(2)
