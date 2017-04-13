'''Simple Undirected Graph implmented using a dictionary as an adjaceny list.
'''

class UndirectedGraph:
    
    def __init__(self, g=None):
        # hold {node: [target nodes]}
        if g:
            self.g = g
        else:
            self.g = dict()
         
    def adjacent(self, x, y):
        assert x in self.g
        assert y in self.g
        return y in self.g[x] # O(1)

    def neighbors(self, x):
        assert x in self.g
        return self.g[x] # O(1)

    def add_vertex(self, x):
        assert x not in self.g
        self.g[x] = set() # O(1)
        
    def add_vertices(self, lst):
        for x in lst:
            self.add_vertex(x)

    def remove_vertex(self, x):
        assert x in self.g
        for vert in self.g[x]: # O(deg(v))
            assert x in self.g[vert]
            self.g[vert].remove(x)
        self.g.pop(x, None)

    def add_edge(self, x, y):
        assert x in self.g
        assert y in self.g
        assert x not in self.g[y]
        assert y not in self.g[x]
        self.g[x].add(y)
        self.g[y].add(x)
        
    def add_edges(self, lst):
        for x, y in lst:
            self.add_edge(x, y)
        
    def remove_edge(self, x, y):
        assert x in self.g
        assert y in self.g
        assert x in self.g[y]
        assert y in self.g[x]
        self.g[x].remove(y)
        self.g[y].remove(x)

    def __repr__(self):
        return 'UndirectedGraph()'

    def __str__(self):
        s = 'UndirectedGraph()\n'
        for key, val in sorted(self.g.items()):
            if val:
                s += '{0} : {1}\n'.format(key, val)
            else:
                s += key + ' : {}\n'
        return s
