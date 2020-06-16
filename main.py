from graphs.graph import Graph
from util.file_reader import read_graph_from_file
# from graphs.weighted_graph import WeightedGraph


# Driver code
if __name__ == '__main__':

    # Create the graph

    # graph = Graph(is_directed=True)

    # # Add some vertices
    # graph.add_vertex('A')
    # graph.add_vertex('E')
    # graph.add_vertex('B')
    # graph.add_vertex('C')
    # graph.add_vertex('D')
    # graph.add_vertex('F')
    # graph.add_vertex('G')

    # # Add connections
    # graph.add_edge('A', 'B')
    # graph.add_edge('B', 'C')
    # graph.add_edge('B', 'D')
    # graph.add_edge('D', 'E')
    # graph.add_edge('F', 'G')

    # Or, read a graph in from a file
    # graph = read_graph_from_file('test_files/graph_small_directed.txt')

    # Output the vertices & edges
    # Print vertices
    # print(f'The vertices are: {graph.get_vertices()} \n')

    # # Print edges
    # print('The edges are:')
    # for vertex_obj in graph.get_vertices():
    #     for neighbor_obj in vertex_obj.get_neighbors():
    #         print(f'({vertex_obj.get_id()} , {neighbor_obj.get_id()})')

    # # Search the graph
    # print('Performing BFS traversal...')
    # graph.bfs_traversal('A')

    # # Find shortest path
    # print('Finding shortest path from vertex A to vertex E...')
    # shortest_path = graph.find_shortest_path('A', 'E')
    # print(shortest_path)

    # # Find all vertices N distance away
    # print('Finding all vertices distance 2 away...')
    # vertices_2_away = graph.find_vertices_n_away('A', 2)
    # print(vertices_2_away)

    # graph = read_graph_from_file('test_files/graph_small_directed.txt')

    # print(graph)

    # # Is bipartite?

    # graph = Graph(is_directed=False)
    # graph.add_vertex('A')
    # graph.add_vertex('B')
    # graph.add_vertex('C')
    # graph.add_edge('A','B')
    # graph.add_edge('A','C')
    # graph.add_edge('B','C')

    # print('\nBipartite?')
    # bipartite = graph.is_bipartite()
    # print(bipartite)


    # Connected components
    # graph = Graph(is_directed=False)

    # vertex_a = graph.add_vertex('A')
    # vertex_b = graph.add_vertex('B')
    # vertex_c = graph.add_vertex('C')
    # vertex_d = graph.add_vertex('D')
    # vertex_d = graph.add_vertex('E')
    # vertex_d = graph.add_vertex('F')
    # graph.add_edge('A','B')
    # graph.add_edge('A','C')
    # graph.add_edge('B','C')
    # graph.add_edge('D', 'E')

    # print('\nConnected')
    # print(graph.find_connected_components())


    # Iterative DFS
    graph = Graph(is_directed=True)
    graph.add_vertex('A')
    graph.add_vertex('B')
    graph.add_vertex('C')
    graph.add_edge('A','B')
    graph.add_edge('B','C')
    graph.add_edge('C','A')

    print('\nIter DFS')
    print(graph.find_path_dfs('A', 'C'))