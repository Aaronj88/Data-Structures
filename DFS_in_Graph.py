class Graph:
    def __init__(self,num_nodes):
        self.num_nodes = num_nodes
        self.adjacent = [[] for i in range(num_nodes)]
    
    def create_edge(self,n1,n2):
        self.adjacent[n1-1].append(n2-1)
        self.adjacent[n2-1].append(n1-1)

    def DFS(self,start):
        visited = [False]*self.num_nodes
        result = []
        self.DFS_util(start,visited,result)

        return result
    
    def DFS_util(self,start,visited,result):
        result.append(start)
        visited[start] = True

        for i in self.adjacent[start]:
            if visited[i] == False:
                self.DFS_util(i,visited,result)


g = Graph(10)

g.create_edge(1,2)
g.create_edge(1,3)
g.create_edge(1,4)
g.create_edge(2,5)
g.create_edge(2,6)
g.create_edge(4,7)

print(g.DFS(3))




        


