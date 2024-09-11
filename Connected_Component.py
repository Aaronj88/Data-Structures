class Graph:
    def __init__(self,num):
        self.num = num
        self.adjacent = [[] for i in range(num)]

    def add_edge(self,n1,n2):
        self.adjacent[n1].append(n2)
        self.adjacent[n2].append(n1)

    def DFS_util(self,visited,start,stack):
        visited[start] = True
        stack.append(start)
        for i in self.adjacent[start]:
            if visited[i] == False:
                stack = self.DFS_util(visited,i,stack)
        return stack
    
    def connected_components(self):
        visited = []
        cc = []
        for i in range(self.num):
            visited.append(False)
        
        for j in range(self.num):
            if visited[j] == False:
                stack = []
                cc.append(self.DFS_util(visited,j,stack))

        return cc
    


g1 = Graph(8)

g1.add_edge(1,3)
g1.add_edge(3,5)
g1.add_edge(2,4)
'''g1.add_edge(2,4)
g1.add_edge(2,5)
g1.add_edge(4,6)'''

print(g1)
cc = g1.connected_components()
print(cc)

