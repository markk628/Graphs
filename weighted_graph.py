class WeightedVertex():
    
    def __init__(self, vertex_id):
        """
        Initialize a vertex and its neighbors dictionary.
        
        Parameters:
        vertex_id (string): A unique identifier to identify this vertex.
        """
        self.id = vertex_id
        self.neighbors_dict = {} # id -> (obj, weight)

    def add_neighbor(self, vertex_obj, weight):
        """
        Add a neighbor by storing it in the neighbors dictionary.

        Parameters:
        vertex_obj (Vertex): An instance of Vertex to be stored as a neighbor.
        weight (number): The weight of this edge.
        """
        if vertex_obj.get_id() in self.neighbors_dict.keys():
            return # it's already a neighbor

        self.neighbors_dict[vertex_obj.get_id()] = (vertex_obj, weight)

    def get_neighbors(self):
        """Return the neighbors of this vertex."""
        return [neighbor for (neighbor, weight) in self.neighbors_dict.values()]

    def get_neighbors_with_weights(self):
        """Return the neighbors of this vertex."""
        return list(self.neighbors_dict.values())

    def get_id(self):
        """Return the id of this vertex."""
        return self.id

    def __str__(self):
        """Output the list of neighbors of this vertex."""
        neighbor_ids = [neighbor.get_id() for neighbor in self.get_neighbors()]
        return f'{self.id} adjacent to {neighbor_ids}'

    def __repr__(self):
        """Output the list of neighbors of this vertex."""
        neighbor_ids = [neighbor.get_id() for neighbor in self.get_neighbors()]
        return f'{self.id} adjacent to {neighbor_ids}'


class WeightedGraph():

    INFINITY = float('inf')

    def __init__(self, is_directed=True):
        """
        Initialize a graph object with an empty vertex dictionary.

        Parameters:
        is_directed (boolean): Whether the graph is directed (edges go in only one direction).
        """
        self.vertex_dict = {} # id -> obj
        self.is_directed = is_directed

    def add_vertex(self, vertex_id):
        """
        Add a new vertex object to the graph with the given key and return the vertex.
        
        Parameters:
        vertex_id (string): The unique identifier for the new vertex.

        Returns:
        Vertex: The new vertex object.
        """
        if vertex_id in self.vertex_dict.keys():
            return False # it's already there
        vertex_obj = WeightedVertex(vertex_id)
        self.vertex_dict[vertex_id] = vertex_obj
        return True

    def get_vertex(self, vertex_id):
        """Return the vertex if it exists."""
        if vertex_id not in self.vertex_dict.keys():
            return None
        vertex_obj = self.vertex_dict[vertex_id]
        return vertex_obj
    
    def add_edge(self, vertex_id1, vertex_id2, weight):
        """
        Add an edge from vertex with id `vertex_id1` to vertex with id `vertex_id2`.

        Parameters:
        vertex_id1 (string): The unique identifier of the first vertex.
        vertex_id2 (string): The unique identifier of the second vertex.
        weight (number): The edge weight.
        """
        all_ids = self.vertex_dict.keys()
        if vertex_id1 not in all_ids or vertex_id2 not in all_ids:
            return False
        vertex_obj1 = self.get_vertex(vertex_id1)
        vertex_obj2 = self.get_vertex(vertex_id2)
        vertex_obj1.add_neighbor(vertex_obj2, weight)
        if not self.is_directed:
            vertex_obj2.add_neighbor(vertex_obj1, weight)

    def get_vertices(self):
        """Return all the vertices in the graph"""
        return list(self.vertex_dict.values())

    def __iter__(self):
        """Iterate over the vertex objects in the graph, to use sytax:
        for vertex in graph"""
        return iter(self.vertex_dict.values())

    def union(self, parent_map, vertex_id1, vertex_id2):
        """Combine vertex_id1 and vertex_id2 into the same group."""
        vertex1_root = self.find(parent_map, vertex_id1)
        vertex2_root = self.find(parent_map, vertex_id2)
        parent_map[vertex1_root] = vertex2_root


    def find(self, parent_map, vertex_id):
        """Get the root (or, group label) for vertex_id."""
        if(parent_map[vertex_id] == vertex_id):
            return vertex_id
        return self.find(parent_map, parent_map[vertex_id])

    def minimum_spanning_tree_kruskal(self):
        """
        Use Kruskal's Algorithm to return a list of edges, as tuples of 
        (start_id, dest_id, weight) in the graph's minimum spanning tree.

        make a variable sorted_edges equal to an empty list
        for vertex in self get vertices
            for neighbor2 in vertex get neighbors with weight
                append a tuple containing neighbor1, neighbor2, and the weight to sorted_edges
        
        sort sorted_edges by weight
    
        make a dictionary parent_map
        """
        # TODO: Create a list of all edges in the graph, sort them by weight 
        # from smallest to largest

        # TODO: Create a dictionary `parent_map` to map vertex -> its "parent". 
        # Initialize it so that each vertex is its own parent.

        # TODO: Create an empty list to hold the solution (i.e. all edges in the 
        # final spanning tree)

        # TODO: While the spanning tree holds < V-1 edges, get the smallest 
        # edge. If the two vertices connected by the edge are in different sets 
        # (i.e. calling `find()` gets two different roots), then it will not 
        # create a cycle, so add it to the solution set and call `union()` on 
        # the two vertices.

        # TODO: Return the solution list.

        edge_list = []
        for v in self.get_vertices():
            for (n, w) in v.get_neighbors_with_weights():
                edge_list.append((v.get_id(), n.get_id(), w))

        edge_list = sorted(edge_list, key=lambda e: e[2])

        parent_map = {}
        for edge in edge_list:
            parent_map[edge[0]] = edge[0]

        spanning_tree = []

        while len(spanning_tree) <= (len(edge_list) - 1):
            edge = edge_list.pop(0)
            start, end, w = edge

            if self.find(parent_map, start) != self.find(parent_map, end):
                spanning_tree.append(edge)
                self.union(parent_map, start, end)
        
        return spanning_tree

    def minimum_spanning_tree_prim(self):
        """
        Use Prim's Algorithm to return the total weight of all edges in the
        graph's spanning tree.

        Assume that the graph is connected.
        """
        # TODO: Create a dictionary `vertex_to_weight` and initialize all
        # vertices to INFINITY - hint: use `float('inf')`

        # TODO: Choose one vertex and set its weight to 0

        # TODO: While `vertex_to_weight` is not empty:
        # 1. Get the minimum-weighted remaining vertex, remove it from the
        #    dictionary, & add its weight to the total MST weight
        # 2. Update that vertex's neighbors, if edge weights are smaller than
        #    previous weights

        # TODO: Return total weight of MST
        
        mst_weight = 0
        vertex_to_weight = {}
        for v in self.get_vertices():
            vertex_to_weight[v] = float('inf')
        
        vertex_to_weight[self.get_vertices()[0]] = 0

        while vertex_to_weight:
            minimum_weighted_v = min(vertex_to_weight.items(), key=lambda v: v[1])
            v = minimum_weighted_v[0]
            vertex_to_weight.pop(v, None)
            mst_weight += minimum_weighted_v[1]

            for (n, w) in v.get_neighbors_with_weights():
                if n in vertex_to_weight and w < vertex_to_weight[n]:
                    vertex_to_weight[n] = w
        
        return mst_weight

    def find_shortest_path(self, start_id, target_id):
        """
        Use Dijkstra's Algorithm to return the total weight of the shortest path
        from a start vertex to a destination.
        """
        # TODO: Create a dictionary `vertex_to_distance` and initialize all
        # vertices to INFINITY - hint: use `float('inf')`

        # TODO: While `vertex_to_distance` is not empty:
        # 1. Get the minimum-distance remaining vertex, remove it from the
        #    dictionary. If it is the target vertex, return its distance.
        # 2. Update that vertex's neighbors by adding the edge weight to the
        #    vertex's distance, if it is lower than previous.

        # TODO: Return None if target vertex not found.

        vertex_to_distance = {}
        for v in self.get_vertices():
            vertex_to_distance[v] = float('inf')

        vertex_to_distance[self.get_vertices()[0]] = 0

        while vertex_to_distance:
            minimum_distance = min(vertex_to_distance.items(), key=lambda d: d[1])
            v = minimum_distance[0]
            vertex_to_distance.pop(v, None)

            if v.get_id() == target_id:
                return minimum_distance[1]
            else:
                for (n, w) in v.get_neighbors_with_weights():
                    if n in vertex_to_distance and w < vertex_to_distance[n]:
                        vertex_to_distance[n] = w + minimum_distance[1]