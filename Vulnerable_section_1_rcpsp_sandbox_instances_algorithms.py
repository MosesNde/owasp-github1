     :param graph: The graph in which to traverse the paths.
     :return: A collection of paths using all graph nodes. All the paths are vertex-disjoint.
     """
    successors: dict[Job, list[Job]] = {node: list(graph.successors(node)) for node in graph.nodes if len(list(graph.successors(node))) > 0}
     in_degrees = {node: d for node, d in graph.in_degree if d > 0}
     no_in = deque()
     for node, d in graph.in_degree:
         if d == 0:
             no_in.append(node)
 
     paths = []
     while no_in:
         node = no_in.popleft()

         path = [node]
         while node in successors:  # while there are successors for node...
            old_node, node = node, successors[node].pop(random.randrange(0, len(successors[node])))
            for successor in successors[old_node]:
                 in_degrees[successor] -= 1
                 if in_degrees[successor] == 0:
                     del in_degrees[successor]
                     no_in.append(successor)
             del successors[old_node]
             path.append(node)  # add this new node to the path
 
         paths.append(path)
 
    # TODO new algorithm: paths are not disjoint

     return paths
 
 