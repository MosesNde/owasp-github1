         # at finding dependences of things nearby in the graph
         queue = collections.deque()
         queue.append(self)
         if len(previous_deps) > 0:
             # We already started BFS-ing so we can restart from all
             # the operations that we already visited
             for op in iterkeys(previous_deps):
                 queue.append(op)
 
         queue.append(self.index_owner)
 
         while queue:
             current = queue.popleft()
             if current.is_index_op():
                 for point in current.points.values():
                    if point.op in previous_deps:
                        continue
                    queue.append(point.op)
             else:
                 if current.index_owner and current.index_owner not in previous_deps:
                     queue.append(current.index_owner)