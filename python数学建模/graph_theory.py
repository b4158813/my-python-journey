class DenseGraph:
    def __init__(self, n, directed=False):
        self.n = n  # number of vertex
        self.m = 0  # number of edge
        self.directed = directed
        self.matrix = [[0 for i in range(n)] for i in range(n)]

    def __str__(self):
        for line in self.matrix:
            print(str(line))
        return ''  # must return string

    def getNumberOfEdge(self):
        return self.m

    def getNumberOfVertex(self):
        return self.n

    def hasEdge(self, v, w):
        if 0 <= v <= self.n and 0 <= w <= self.n:
            return self.matrix[v][w]
        else:
            raise Exception("vertex not in the Graph")

    def addEdge(self, v, w):
        if 0 <= v <= self.n and 0 <= w <= self.n:
            if self.hasEdge(v, w):
                return
            self.matrix[v][w] = 1
            if self.directed is False:
                self.matrix[w][v] = 1
            self.m += 1
        else:
            raise Exception("vertex not in the Graph")
