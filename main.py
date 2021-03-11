from graph import Graph

# Driver code
if __name__ == '__main__':

    # Create the graph

    graph = Graph(is_directed=True)

    graph.add_vertex('A')
    graph.add_vertex('B')
    graph.add_vertex('C')
    graph.add_vertex('D')
    graph.add_vertex('E')
    # graph.add_vertex('F')

    graph.add_edge('A', 'B')
    graph.add_edge('B', 'C')
    graph.add_edge('B', 'D')
    graph.add_edge('C', 'F')
    graph.add_edge('D', 'E')
    graph.add_edge('E', 'C')
    graph.add_edge('E', 'F')

    # # Add some vertices
    # graph.add_vertex('A')
    # graph.add_vertex('E')
    # graph.add_vertex('B')
    # graph.add_vertex('C')
    # graph.add_vertex('D')
    # graph.add_vertex('F')
    # graph.add_vertex('G')

    # graph.add_vertex('H')
    # graph.add_vertex('I')

    # Add connections
    # graph.add_edge('A', 'B')
    # graph.add_edge('B', 'C')
    # graph.add_edge('B', 'D')
    # graph.add_edge('C', 'E')
    # graph.add_edge('D', 'E')
    # graph.add_edge('F', 'G')

    # graph.add_edge('B', 'I')
    # graph.add_edge('C', 'I')
    # graph.add_edge('C', 'H')

    # graph.add_vertex('A')
    # graph.add_vertex('B')
    # graph.add_vertex('C')
    # graph.add_vertex('D')

    # graph.add_edge('A', 'B')
    # graph.add_edge('A', 'C')
    # graph.add_edge('B', 'D')
    # graph.add_edge('C', 'D')




    # Or, read a graph in from a file
    # graph = read_graph_from_file('test_files/graph_small_directed.txt')

    # Output the vertices & edges
    # print(graph)

    # # Search the graph
    # print('Performing BFS traversal...')
    # bfs = graph.bfs_traversal('D')
    # print(bfs)

    # # Find shortest path
    # print('Finding shortest path from vertex A to vertex E...')
    # shortest_path = graph.find_shortest_path('B', 'H')
    # print(shortest_path)

    # # Find all vertices N distance away
    # print('Finding all vertices distance 2 away...')
    # vertices_2_away = graph.find_vertices_n_away('A', 2)
    # print(vertices_2_away)

    # # Check if graph is barpartite
    # print('Checking if it is bipartite...')
    # isbipartite = graph.is_bipartite()
    # print(isbipartite)

    # Find Connected Components
    # print('Finding connected components...')
    # connected_components = graph.find_connected_components()
    # print(connected_components)

    # Find Path DFS Traversal
    # print('Performing DFS Traversal...')
    # dfs = graph.find_path_dfs_iter('G', 'D')
    # print(dfs)

    # Check if graph contains a cycle
    # print('Performing cycle detection...')
    # contains_cycle = graph.contains_cycle()
    # print(contains_cycle)

    # Perform Topological Sort
    # print('Performing Topological Sort')
    # t_sort = graph.topological_sort()
    # print(t_sort)

    # graph = WeightedGraph(is_directed=False)
    # vertex_a = graph.add_vertex('A')
    # vertex_b = graph.add_vertex('B')
    # vertex_c = graph.add_vertex('C')
    # vertex_c = graph.add_vertex('D')
    # vertex_c = graph.add_vertex('E')
    # vertex_c = graph.add_vertex('F')
    # vertex_c = graph.add_vertex('G')
    # vertex_c = graph.add_vertex('H')
    # vertex_c = graph.add_vertex('J')

    # graph.add_edge('A','B', 2)
    # graph.add_edge('A','C', 7)
    # graph.add_edge('A','E', 5)
    # graph.add_edge('B','E', 4)
    # graph.add_edge('B','D', 8)
    # graph.add_edge('C','E', 3)
    # graph.add_edge('C','D', 8)
    # graph.add_edge('D','E', 6)


    # print(graph.minimum_spanning_tree_kruskal())
    print(graph.topological_sort())

    
