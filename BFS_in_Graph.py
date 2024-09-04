class Graph:
    def __init__(self,num):
        self.num = num
        self.adjacent = [[]*num for i in range(num)]

    def create_edge(self,n1,n2):
        self.adjacent[n1-1].append(n2-1) # Node 1 and node 2
        self.adjacent[n2-1].append(n1-1)

    def BFS(self,start): # Breadth First Search
        visited = [False]*self.num
        result = []
        queue = []
        queue.append(start)
        visited[start] = True
        
        while len(queue) > 0:
            x = queue.pop(0)
            result.append(x)
            for y in self.adjacent[x]:
                if visited[y] == False:
                    queue.append(y)
                    visited[y] = True
        
        return result
    





g = Graph(11)

'''g.create_edge(1,2)
g.create_edge(2,3)
g.create_edge(2,4)
g.create_edge(4,5)
g.create_edge(3,6)
g.create_edge(3,7)'''

g.create_edge(1,4)
g.create_edge(4,5)
g.create_edge(5,11)
g.create_edge(5,8)
g.create_edge(11,2)
g.create_edge(5,2)
g.create_edge(5,3)


print(g.BFS(4))

