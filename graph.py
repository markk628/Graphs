from collections import deque

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
        self.vertex_dict = {} # id -> list of neighbor ids
        self.is_directed = is_directed

    def add_vertex(self, vertex_id):
        """
        Add a new vertex object to the graph with the given key.
        
        Parameters:
        vertex_id (string): The unique identifier for the new vertex.
        """
        if self.contains_vertex(vertex_id):
            return
        
        # self.vertex_dict[vertex_id] = Vertex(vertex_id).get_neighbors_ids()
        self.vertex_dict[vertex_id] = []

    def add_edge(self, start_id, end_id):
        """
        Add an edge from vertex with id `start_id` to vertex with id `end_id`.

        Parameters:
        start_id (string): The unique identifier of the first vertex.
        end_id (string): The unique identifier of the second vertex.
        """
        self.add_vertex(start_id)
        self.add_vertex(end_id)

        self.vertex_dict[start_id].append(end_id)
        if not self.is_directed:
            self.vertex_dict[end_id].append(start_id)

    def contains_vertex(self, vertex_id):
        """Return True if the vertex is contained in the graph."""
        if vertex_id in self.vertex_dict:
            return True
        return False

    def contains_edge(self, start_id, end_id):
        """
        Return True if the edge is contained in the graph from vertex `start_id`
        to vertex `end_id`.

        Parameters:
        start_id (string): The unique identifier of the first vertex.
        end_id (string): The unique identifier of the second vertex."""
        if not self.contains_vertex(start_id):
            return False
        for neighbor_id in self.vertex_dict[start_id]:
            if neighbor_id == end_id:
                return True
        return False

    def get_vertices(self):
        """
        Return all vertices in the graph.
        
        Returns:
        list<string>: The vertex ids contained in the graph.
        """
        return list(self.vertex_dict.keys())

    def get_neighbors(self, start_id):
        """
        Return a list of neighbors to the vertex `start_id`.

        Returns:
        list<string>: The neigbors of the start vertex.
        """
        return self.vertex_dict[start_id]

    def __str__(self):
        """Return a string representation of the graph."""
        graph_repr = [f'{vertex} -> {self.vertex_dict[vertex]}' 
            for vertex in self.vertex_dict.keys()]
        return f'Graph with vertices: \n' +'\n'.join(graph_repr)

    def __repr__(self):
        """Return a string representation of the graph."""
        return self.__str__()

    def bfs_traversal(self, start_id):
        """
        Traverse the graph using breadth-first search.
        """
        if start_id not in self.vertex_dict:
            raise KeyError("The start vertex is not in the graph!")

        # Keep a set to denote which vertices we've seen before
        seen = set()
        seen.add(start_id)

        # Keep a queue so that we visit vertices in the appropriate order
        queue = deque()
        queue.append(start_id)

        path = []

        while queue:
            current_vertex_id = queue.popleft()
            path.append(current_vertex_id)

            # Process current node
            print('Processing vertex {}'.format(current_vertex_id))

            # Add its neighbors to the queue
            for neighbor_id in self.get_neighbors(current_vertex_id):
                if neighbor_id not in seen:
                    seen.add(neighbor_id)
                    queue.append(neighbor_id)

        return path

    def find_shortest_path(self, start_id, target_id):
        """
        Find and return the shortest path from start_id to target_id.

        Parameters:
        start_id (string): The id of the start vertex.
        target_id (string): The id of the target (end) vertex.

        Returns:
        list<string>: A list of all vertex ids in the shortest path, from start to end.
        """
        if not self.contains_vertex(start_id) and not self.contains_vertex(target_id):
            raise KeyError("The start and/or target vertex is not in the graph!")

        vertex_id_to_path = {start_id: [start_id]} #keeps track of the vertices we’ve seen so far, and stores their shortest paths
        queue = deque()
        queue.append(start_id)

        while queue:
            current_vertex_id = queue.popleft()

            if current_vertex_id == target_id:
                break
            
            for neighbor_id in self.get_neighbors(current_vertex_id):
                if neighbor_id not in vertex_id_to_path:
                    vertex_id_to_path[neighbor_id] = vertex_id_to_path[current_vertex_id] + [neighbor_id]
                    queue.append(neighbor_id)
        
        if target_id not in vertex_id_to_path:
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

        Psedocode
        make an empty list called n_distance_vertices
        make a dictionary vertices key start_id vertex:  value distance away from start_id vertex
        make a queue
        add start_id to queue

        while queue is not empthy
            make variable current vertex equal to queue popped

            if value for curreent vertex in vertices is equal to target distance
            append it to n_distance_vertices

            for neighbor in neighbors of current vertex
                if neighbor is not in vertices
                    add neighbor to vertices equal to current vertex of vertices plus 1
                    add neighbor to queue
        
        return n_distance_vertices
        """

        n_distance_vertices = []
        vertices = {start_id: 0}
        queue = deque()
        queue.append(start_id)

        while queue:
            current_vertex_id = queue.popleft()

            if vertices[current_vertex_id] == target_distance:
                n_distance_vertices.append(current_vertex_id)

            for neighbor_id in self.get_neighbors(current_vertex_id):
                if neighbor_id not in vertices:
                    vertices[neighbor_id] = vertices[current_vertex_id] + 1
                    queue.append(neighbor_id)
        
        return n_distance_vertices

    def is_bipartite(self):
        """
        Return True if the graph is bipartite, and False otherwise

        Psedocode
        make a variable v1 equal to the item at index 0 of get_vertices()
        make a dictionary vertex_id_group with v1 as key and 0 as value
        make a queue and append v1 to it

        while queue is not empty
            set a variable current_vertex_id equal to queue popped

            for neighbor in current_vertex_id's neighbors
                if neighbor is not in vertex_id_group
                    add neighbor to vertex_id_group with current_vertex_id's key plus 1
                    append the neighbor to queue

        for vertex in vertex_id_group
            for neighbor in vertex's neighbors
                if the value of vertex in vertex_id_group is even
                    if value of neighbor in vertex_id_group is even
                        return false
                if the value of vertex in vertex_id_group is odd
                    if value of neighbor in vertex_id_group is odd
                        return false
        
        return true
        """

        # if len(self.get_vertices()) == 3:
        #     raise KeyError("naw mate")

        v1 = self.get_vertices()[0]

        vertex_id_group = {v1: 0}
        queue = deque()
        queue.append(v1)

        while queue:
            current_vertex_id = queue.popleft()

            for neighbor_id in self.get_neighbors(current_vertex_id):
                if neighbor_id not in vertex_id_group:
                    vertex_id_group[neighbor_id] = vertex_id_group[current_vertex_id] + 1
                    queue.append(neighbor_id)

        for v in vertex_id_group:
            for neighbor in self.get_neighbors(v):
                if vertex_id_group[v] % 2 == 0:
                    if vertex_id_group[neighbor] % 2 == 0:
                        return False
                # if vertex_id_group[v] % 2 != 0:
                else:
                    if vertex_id_group[neighbor] % 2 != 0:
                        return False
        return True

    def get_connected(self, start_id, visit):
        visited = set()
        queue = deque()
        queue.append(start_id)
        visited.add(start_id)

        while queue:
            v = queue.popleft()

            for vertex in self.get_neighbors(v):
                if vertex not in visited:
                    queue.append(vertex)
                    visited.add(vertex)
                    visit(vertex)
        
        return list(visited)

    def find_connected_components(self):
        """
        Return a list of all connected components, with each connected component
        represented as a list of vertex ids.
        """
        visited = set()
        connected_components = []

        for vertex in self.get_vertices():
            if vertex not in visited:
                visited.add(vertex)
                connected_components.append(self.get_connected(vertex, visited.add))

        return connected_components

    def find_path_dfs_iter(self, start_id, target_id):
        """
        Use DFS with a stack to find a path from start_id to target_id.
        """
        if not self.contains_vertex(start_id) and not self.contains_vertex(target_id):
            raise KeyError("The start vertex and/or target vertex are/is not in the graph!")
        
        seen = set()
        seen.add(start_id)
        stack = [start_id]
        path = []

        while stack:
            current_vertex = stack.pop()

            path.append(current_vertex)

            if target_id == current_vertex:
                return path
            
            for neighbor in self.get_neighbors(current_vertex):
                stack.append(neighbor)

        raise KeyError("Path does not exist")
        
    def dfs_traversal(self, start_id):
        """Visit each vertex, starting with start_id, in DFS order."""

        visited = set() # set of vertices we've visited so far
        path = []

        def dfs_traversal_recursive(start_vertex):
            print(f'Visiting vertex {start_vertex}')

            # recurse for each vertex in neighbors
            for neighbor in self.get_neighbors(start_vertex):
                if neighbor not in visited:
                    visited.add(neighbor)
                    path.append(neighbor)
                    dfs_traversal_recursive(neighbor)
            return path

        visited.add(start_id)
        path.append(start_id)
        return dfs_traversal_recursive(start_id)

    def contains_cycle(self):
        """
        Return True if the directed graph contains a cycle, False otherwise.
        """
        current_path = set()

        def contains_cycle_dfs(start_id, path):

            for neighbor in self.get_neighbors(start_id):
                if neighbor in path:
                    return True
                path.add(neighbor)
                return contains_cycle_dfs(neighbor, path)

            return False
        
        start_id = self.get_vertices()[0]
        current_path.add(start_id)
        return contains_cycle_dfs(start_id, current_path)

    def topological_sort_dfs(self, start_id, visited):
        for neighbor in self.get_neighbors(start_id):
            if neighbor not in visited:
                visited.add(neighbor)
                self.topological_sort_dfs(neighbor, visited)

    def topological_sort(self):
        """
        Return a valid ordering of vertices in a directed acyclic graph.
        If the graph contains a cycle, throw a ValueError.
        """
        # TODO: Create a stack to hold the vertex ordering.
        # TODO: For each unvisited vertex, execute a DFS from that vertex.
        # TODO: On the way back up the recursion tree (that is, after visiting a 
        # vertex's neighbors), add the vertex to the stack.
        # TODO: Reverse the contents of the stack and return it as a valid ordering.
        
        if self.contains_cycle():
            raise ValueError('graph contains a cycle')

        visited = set()
        stack = []

        for vertex in self.get_vertices():
            visited.add(vertex)
            self.topological_sort_dfs(vertex, visited)

            stack.append(vertex)

        v = stack.pop()
        stack.insert(0, v)
        return stack

