from collections import deque
from heapq import heappush, heappop 

def shortest_shortest_path(graph, source):
  """
  Params: 
    graph.....a graph represented as a dict where each key is a vertex
              and the value is a set of (vertex, weight) tuples (as in the test case)
    source....the source node

  Returns:
    a dict where each key is a vertex and the value is a tuple of
    (shortest path weight, shortest path number of edges). See test case for example.
  """
  ### TODO
  pass
  shortest_path = {}
  for node in graph:
      shortest_path[node] = (float('inf'), 0)
  shortest_path[source] = (0, 0)
  q = deque([source])
  while q:
      node = q.popleft()
      for neighbor, weight in graph[node]:
          if shortest_path[neighbor][0] > shortest_path[node][0] + weight:
              shortest_path[neighbor] = (shortest_path[node][0] + weight, shortest_path[node][1] + 1)
              q.append(neighbor)
  return shortest_path




def bfs_path(graph, source):
  """
  Returns:
    a dict where each key is a vertex and the value is the parent of 
    that vertex in the shortest path tree.
  """
  ###TODO
  pass
  parents = {}
  for node in graph:
      parents[node] = None
  parents[source] = source
  q = deque([source])
  while q:
      node = q.popleft()
      for neighbor in graph[node]:
          if parents[neighbor] is None:
              parents[neighbor] = node
              q.append(neighbor)
  return parents

def get_sample_graph():
   return {'s': {'a', 'b'},
          'a': {'b'},
          'b': {'c'},
          'c': {'a', 'd'},
          'd': {}
          }

def get_path(parents, destination):
  """
  Returns:
  The shortest path from the source node to this destination node 
  (excluding the destination node itself). See test_get_path for an     
  example.
  """
  path = []
  while destination in parents:
      path.append(destination)
      destination = parents[destination]
  return ''.join(path[::-1])

