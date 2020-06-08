from graphs.graph import Graph
import re


def read_graph_from_file(filename):
    """
    Read in data from the specified filename, and create and return a graph
    object corresponding to that data.

    Arguments:
    filename (string): The relative path of the file to be processed

    Returns:
    Graph: A directed or undirected Graph object containing the specified
    vertices and edges
    """
    with open(filename) as f:
        line = f.readline().strip(' \n')
        # first line
        if line == 'G':
            g = graph(is_directed=False)
        elif line == 'D':
            g = Graph()
        else:
            raise ValueError(line)

        vertices = re.findall('[A-Z]|[0-9]', f.readline())
        for _, v in enumerate(vertices):
            g.add_vertex(v)

        line = f.readline()
        while line:
            vertex= re.findall('[A-Z]|[0-9]', line)
            g.add_edge(vertex[0], vertex[1])
            line = f.readline


if __name__ == '__main__':

    graph = read_graph_from_file('test.txt')

    print(graph)