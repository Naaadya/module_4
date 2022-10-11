import queue

graph = {'A': ['B','C'],
'B' : ['D','E'],
'C' : [],
'D' : [],
'E' : []}


def bfs(graph, start, goal):
   if start == goal:
      return True
   q = queue.Queue()
   visited = []
   visited.append(start)
   q.put(start)
   while not q.empty():
      s = q.get()
      print(s, end = ' ')
      if s == goal:
         return True
      for v in graph[s]:
         if v not in visited:
            visited.append(v)
            q.put(v)
   return False


result = bfs(graph, 'A', 'Y')
print(result)
