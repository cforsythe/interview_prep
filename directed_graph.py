
class Vertice:
    def __init__(self, val):
        self.val = val
        self.visited = False


class Graph:

    vertices = {}

    def __init__(self, vertice):
        self.add_vertice(vertice)

    def vertice_exist(self, vertice):
        if vertice in self.vertices:
            return True
        return False

    def add_vertice(self, vertice):
        self.vertices[vertice] = []

    def add_edge(self, start, target):
        if not self.vertice_exist(start):
            self.add_vertice(start)
        if  not self.vertice_exist(target):
            self.add_vertice(target)
        self.vertices[start].append(target)

    def BFS(self, node):
        pass
    
    def is_path(self, start, target):
        if not self.vertice_exist(start) or not self.vertice_exist(target):
            return False
        queue = []
        queue.append(start)

        while(len(queue) > 0):
            node = queue[0]
            del queue[0]
            node.visited = True
            for adj_node in self.vertices[node]:
                if adj_node.val == target.val:
                    return True
                if not adj_node.visited:
                    queue.append(adj_node)
        return False


def main():
    s = Vertice("a")
    b = Vertice("b")
    c = Vertice("c")
    d = Vertice("d")
    e = Vertice("e")
    t = Vertice("z")
    graph = Graph(s)
    graph.add_edge(s, b)
    graph.add_edge(s, e)
    graph.add_edge(b, c)
    graph.add_edge(c, e)
    graph.add_edge(e, d)
    graph.add_edge(c, t)
    print(graph.is_path(s, t))

main()



        