from collections import deque
from random import choice

class Vertex(object):
    """
    Defines a single vertex and its neighbors.
    """

    def __init__(self, vertex_id):
        """
        Initialize a vertex and its neighbors dictionary.
        
        Parameters:
        vertex_id (string): A unique identifier to identify this vertex.
        """
        self.__id = vertex_id
        self.__neighbors_dict = {} # id -> object

    def add_neighbor(self, vertex_obj):
        """
        Add a neighbor by storing it in the neighbors dictionary.

        Parameters:
        vertex_obj (Vertex): An instance of Vertex to be stored as a neighbor.
        """
        self.__neighbors_dict[vertex_obj.__id] = vertex_obj

    def __str__(self):
        """Output the list of neighbors of this vertex."""
        neighbor_ids = list(self.__neighbors_dict.keys())
        return f'{self.__id} adjacent to {neighbor_ids}'

    def __repr__(self):
        """Output the list of neighbors of this vertex."""
        return self.__str__()

    def get_neighbors(self):
        """Return the neighbors of this vertex."""
        return list(self.__neighbors_dict.values())

    def get_id(self):
        """Return the id of this vertex."""
        return self.__id


class Graph:
    """ Graph Class
    Represents a directed or undirected graph.
    """
    def __init__(self, is_directed=True):
        """
        Initialize a graph object with an empty vertex dictionary.

        Parameters:
        is_directed (boolean): Whether the graph is directed (edges go in only one direction).
        """
        self.__vertex_dict = {} # id -> object
        self.__is_directed = is_directed

    def add_vertex(self, vertex_id):
        """
        Add a new vertex object to the graph with the given key and return the vertex.
        
        Parameters:
        vertex_id (string): The unique identifier for the new vertex.

        Returns:
        Vertex: The new vertex object.
        """
        self.__vertex_dict[vertex_id] = Vertex(vertex_id)
        return self.__vertex_dict.get(vertex_id)
        

    def get_vertex(self, vertex_id):
        """Return the vertex if it exists."""
        if vertex_id not in self.__vertex_dict:
            return None

        vertex_obj = self.__vertex_dict[vertex_id]
        return vertex_obj

    def add_edge(self, vertex_id1, vertex_id2):
        """
        Add an edge from vertex with id `vertex_id1` to vertex with id `vertex_id2`.

        Parameters:
        vertex_id1 (string): The unique identifier of the first vertex.
        vertex_id2 (string): The unique identifier of the second vertex.
        """
        if vertex_id1 not in self.__vertex_dict:
            self.add_vertex(vertex_id1)
        if vertex_id2 not in self.__vertex_dict:
            self.add_vertex(vertex_id2)

        # Add vertex_id2 as neighbor to vertex_id1 to make link/edge
        self.__vertex_dict[vertex_id1].add_neighbor(self.__vertex_dict[vertex_id2])

        if not self.__is_directed:
            self.__vertex_dict[vertex_id2].add_neighbor(self.__vertex_dict[vertex_id1])
        
    def get_vertices(self):
        """
        Return all vertices in the graph.
        
        Returns:
        List<Vertex>: The vertex objects contained in the graph.
        """
        return list(self.__vertex_dict.values())

    def contains_id(self, vertex_id):
        return vertex_id in self.__vertex_dict

    def __str__(self):
        """Return a string representation of the graph."""
        return f'Graph with vertices: {self.get_vertices()}'

    def __repr__(self):
        """Return a string representation of the graph."""
        return self.__str__()

    def bfs_traversal(self, start_id):
        """
        Traverse the graph using breadth-first search.
        """
        if not self.contains_id(start_id):
            raise KeyError("One or both vertices are not in the graph!")

        # Keep a set to denote which vertices we've seen before
        seen = set()
        seen.add(start_id)

        # Keep a queue so that we visit vertices in the appropriate order
        queue = deque()
        queue.append(self.get_vertex(start_id))

        while queue:
            current_vertex_obj = queue.pop()
            current_vertex_id = current_vertex_obj.get_id()

            # Process current node
            print('Processing vertex {}'.format(current_vertex_id))

            # Add its neighbors to the queue
            for neighbor in current_vertex_obj.get_neighbors():
                if neighbor.get_id() not in seen:
                    seen.add(neighbor.get_id())
                    queue.append(neighbor)

        return # everything has been processed

    def find_shortest_path(self, start_id, target_id):
        """
        Find and return the shortest path from start_id to target_id.

        Parameters:
        start_id (string): The id of the start vertex.
        target_id (string): The id of the target (end) vertex.

        Returns:
        list<string>: A list of all vertex ids in the shortest path, from start to end.
        """
        if not self.contains_id(start_id) or not self.contains_id(target_id):
            raise KeyError("One or both vertices are not in the graph!")

        # vertex keys we've seen before and their paths from the start vertex
        vertex_id_to_path = {
            start_id: [start_id] # only one thing in the path
        }

        # queue of vertices to visit next
        queue = deque() 
        queue.append(self.get_vertex(start_id))

        # while queue is not empty
        while queue:
            current_vertex_obj = queue.pop() # vertex obj to visit next
            current_vertex_id = current_vertex_obj.get_id()

            # found target, can stop the loop early
            if current_vertex_id == target_id:
                break

            neighbors = current_vertex_obj.get_neighbors()
            for neighbor in neighbors:
                if neighbor.get_id() not in vertex_id_to_path:
                    current_path = vertex_id_to_path[current_vertex_id]
                    # extend the path by 1 vertex
                    next_path = current_path + [neighbor.get_id()]
                    vertex_id_to_path[neighbor.get_id()] = next_path
                    queue.append(neighbor)
                    # print(vertex_id_to_path)

        if target_id not in vertex_id_to_path: # path not found
            return None

        return vertex_id_to_path[target_id]

    def find_vertices_n_away(self, start_id, target_distance):
        """
        Find and return all vertices n distance away.
        
        Arguments:
        start_id (string): The id of the start vertex.
        target_distance (integer): The distance from the start vertex we are looking for

        Returns:
        list<string>: All vertex ids that are `target_distance` away from the start vertex
        """
        # already seen
        visited = set()
        target_vertices = []
        
        queue = deque()
        # adds id and distance together
        queue.append((start_id, 0))
        visited.add(start_id)

        while queue:
            # removes vertex_obj from queue and return it
            current_vertex_obj = queue.popleft()

            current_vertex_id = current_vertex_obj[0]
            vertex_distance = current_vertex_obj[1]

            # if distances match, add to n_away_vertices
            if vertex_distance == target_distance:
                target_vertices.append(current_vertex_id)

            # get neighbors of current vertex
            neighbors = self.get_vertex(current_vertex_id).get_neighbors()

            for neighbor in neighbors:
                # print(neighbor)
                if neighbor.get_id() not in visited:
                    queue.append((neighbor.get_id(), vertex_distance + 1))
                    visited.add(neighbor.get_id())

            return target_vertices

    def is_bipartite(self):
        '''
        Return True if bipartite
        '''
        queue = deque()
        visited = {}

        current_color = 0

        current_vertex_id = choice(list(self.__vertex_dict.keys()))

        queue.append(current_vertex_id)
        visited[current_vertex_id] = current_color

        while queue:
            current_color ^= 1

            current_vertex_id = queue.popleft()

            neighbors = self.get_vertex(current_vertex_id).get_neighbors()

            for neighbor in neighbors:
                if neighbor.get_id() not in visited.keys():
                    visited[neighbor.get_id()] = current_color

                    queue.append(neighbor.get_id())
                else:
                    if visited[current_vertex_id] == visited[neighbor.get_id()]:
                        return False

        return True

    def find_connected_components(self):
        """
        Return a list of all connected components, with each connected component represented as a list of vertex ids.
        """
        connected = []
        visited = set()
        queue = deque()
        components = []

        current_vertex_id = choice(list(self.__vertex_dict.keys()))
        visited.add(current_vertex_id)
        queue.append(current_vertex_id)

        while queue:
            current_vertex_id = queue.popleft()
            components.append(current_vertex_id)

            neighbors = self.get_vertex(current_vertex_id).get_neighbors()

            for neighbor in neighbors:
                if neighbor.get_id() not in visited:
                    visited.add(neighbor.get_id())
                    components.append(neighbor.get_id())
            
            connected.append(components)
            components = []

            if len(visited) == len(list(self.__vertex_dict.keys())):
                break

            unvisited = [vertex for vertex in list(self.__vertex_dict.keys()) if vertex not in visited]

            current_vertex_id = choice(unvisited)

            visited.add(current_vertex_id)
            queue.append(current_vertex_id)

        return connected

    def find_path_dfs(self,start_id,target_id):
        """
        DFS using stacks
        """
        if not self.contains_id(start_id) or not self.contains_id(target_id):
            raise KeyError("One or both vertices are not in the graph!")

        # queue of vertices to visit next
        stack = deque()
        stack.append(self.get_vertex(start_id))
        
        # vertex keys we've seen before and their paths from the start vertex
        path_to_target = {
            start_id: [start_id]
        }

        while stack:
            current_vertex_obj = stack.pop() # vertex obj to visit next
            current_vertex_id = current_vertex_obj.get_id()

            # found target, can stop the loop early
            if current_vertex_id == target_id:
                break

            neighbors = current_vertex_obj.get_neighbors()
            for neighbor in neighbors:
                if neighbor.get_id() not in path_to_target:
                    stack.append(neighbor)
                    # print(vertex_id_to_path)

                    current_path = path_to_target[current_vertex_id]
                    # extend the path by 1 vertex
                    next_path = current_path + [neighbor.get_id()]
                    path_to_target[neighbor.get_id()] = next_path
                    
        if target_id not in path_to_target: # path not found
            return None

        return path_to_target[target_id]

    def dfs_traversal(self, start_id):
        visited = set()

        def dfs_traversal_recursive(start_vertex):
            print(f'Visiting vertex {start_vertex.get_id()}')

            # recurse for each vertex in neighbors
            for neighbor in start_vertex.get_neighbors():
                if neighbor.get_id() not in visited:
                    visited.add(neighbor.get_id())
                    dfs_traversal_recursive(neighbor)
            return

        visited.add(start_id)
        start_vertex = self.get_vertex(start_id)
        dfs_traversal_recursive(start_vertex)          
