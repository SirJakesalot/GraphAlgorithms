
class Graph:
    g = dict()
   
    def __init__(self, g=None):
        if g:
            self.g = g
         
    def adjacent(self, x, y):
        return y in self.g[x]

    def neighbors(self, x):
        assert x in self.g
        return self.g[x]

    def add_vertex(self, x):
        assert x not in self.g
        self.g[x] = set()

    def remove_vertex(self, x):
        assert x in self.g
        self.g.pop(x, None)

    def add_edge(self, x, y):
        assert x in self.g
        assert y not in self.g[x]
        self.g[x].add(y)
        
    def remove_edge(self, x, y):
        assert x in self.g
        assert y in self.g[x]
        self.g[x].remove(y)

    def __repr__(self):
        return 'Graph()'

    def __str__(self):
        s = ''
        for key, val in self.g.items():
            if val:
                s += '{0} : {1}\n'.format(key, val)
            else:
                s += key + ' : {}\n'
        return s

g = Graph()
g.add_vertex('A')
g.add_vertex('B')
g.add_vertex('C')
g.add_vertex('D')
g.add_vertex('E')
g.add_vertex('F')
g.add_vertex('G')

g.add_edge('A', 'B')
g.add_edge('A', 'C')
g.add_edge('B', 'C')
g.add_edge('B', 'D')
g.add_edge('C', 'D')
g.add_edge('D', 'C')
g.add_edge('E', 'B')
g.add_edge('F', 'C')

print(g)
g.remove_vertex('G')
print(g)
