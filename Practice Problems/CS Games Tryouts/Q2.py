import sys
from collections import deque

def tree_search(n, edges, start):
  graph = {}
  n = int(n)
  # populate graph
  for n1, n2 in edges:
    if n1 in graph:
      graph[n1].append(n2)
    else:
      graph[n1] = [n2]
    if n2 in graph:
      graph[n2].append(n1)
    else:
      graph[n2] = [n1]
  
  # BFS
  q, seen = deque([(start, 0)]), set([start])
  distances = [-1 for _ in range(n)]
  while q:
    node, dist = q.popleft()
    for neighbor in graph[node]:
      if neighbor not in seen:
        q.append((neighbor, dist+4))
      seen.add(neighbor)
    distances[int(node)-1] = dist

  # Construct output string
  ans = ''
  for dist in distances:
    if dist != 0:
      ans += ' ' + str(dist)

  return ans

if __name__ == "__main__":
  file_name = sys.argv[1]
  f, inputs = open(file_name, 'r'), []
  num_queries = int(f.readline().rstrip())
  for _ in range(num_queries):
    num_nodes, num_edges = f.readline().rstrip().split()
    edges = []
    for _ in range(int(num_edges)):
      edges.append(f.readline().rstrip().split())
    start = f.readline().rstrip()
    print(tree_search(int(num_nodes), edges, start))
  f.close()