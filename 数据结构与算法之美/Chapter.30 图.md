
- 图(Graph)中的元素就叫做顶点(vertex)。
- 图中一个顶点可以与任意其他顶点建立连接关系，这种连接关系叫做边(edge)。
- 顶点之间向连结的边的条数叫做顶点的度(degree)
- 边有方向的图叫做有向图，边没有方向的叫做无向图
- 在有向图中，度可以被分为入度(in-degree)和出度(out-degree)，顶点的入度表示有多少条边指向这个顶点，出度表示有多少条边以这个顶点为起点指向其他顶点
- 带权图(weighted graph)，每条边都有一个权重(weight)

### 邻接矩阵存储方法
图最直观的一种存储方法就是**邻接矩阵(Adjacency Matrix)**。
![邻接矩阵存储法](https://static001.geekbang.org/resource/image/62/d2/625e7493b5470e774b5aa91fb4fdb9d2.jpg)
邻接矩阵的底层依赖一个二维数组。对于无向图来说，如果顶点i与顶点j之间有边，就将A\[i\]\[j\]和A\[j\]\[i\]标记为1；对于有向图来说，如果顶点i到顶点j之间，有一个箭头从顶点i指向顶点j的边，那就将A\[i\]\[j\]标记为1。同理，对于带权图，数组中就存储相应的权重。
- 缺点：浪费空间
- 优点：简单直接，高效。方便计算

### 邻接表存储法(Adjacency List)
每个顶点对应一条链表，链表中存储的是与这个顶点相连接的其他顶点。
![有向图邻接表存储法](https://static001.geekbang.org/resource/image/03/94/039bc254b97bd11670cdc4bf2a8e1394.jpg)
- 优点：节省空间
- 缺点：运算耗时


```python
class Undigraph:
    def __init__(self, vertex_num):
        self.v_num = vertex_num
        self.adj_tbl = []
        for i in range(self.v_num + 1):
            self.adj_tbl.append([])
            
    def add_edge(self, s, t):
        if s > self.v_num or t > self.v_num:
            return False
        self.adj_tbl[s].append(t)
        self.adj_tbl[t].append(s)
        return True
    
    def __len__(self):
        return self.v_num
    
    def __getitem__(self, ind):
        if ind > self.v_num:
            raise IndexError('No Such Vertex')
        return self.adj_tbl[ind]
    
    def __repr__(self):
        return str(self.adj_tbl)
    
    def __str__(self):
        return str(self.adj_tbl)
```


```python
ug = Undigraph(10)
ug.add_edge(1, 9)
ug.add_edge(1, 3)
ug.add_edge(3, 2)
print(ug.adj_tbl)
```

    [[], [9, 3], [3], [1, 2], [], [], [], [], [], [1], []]
    


```python
class Digraph:
    def __init__(self, vertex_num):
        self.v_num = vertex_num
        self.adj_tbl = []
        for i in range(self.v_num + 1):
            self.adj_tbl.append([])
            
    def add_edge(self, frm, to):
        if frm > self.v_num or to > self.v_num:
            return False
        self.adj_tbl[frm].append(to)
        
    def __len__(self):
        return self.v_num
    
    def __getitem__(self, ind):
        if ind > self.v_num:
            raise IndexError("No such vertex!")
        return self.adj_tbl[ind]
    
    def __repr__(self):
        return str(self.adj_tbl)
    
    def __str__(self):
        return str(self.adj_tbl)
```


```python
dg = Digraph(10)
dg.add_edge(1, 9)
dg.add_edge(1, 3)
dg.add_edge(3, 4)
print(dg.adj_tbl)
```

    [[], [9, 3], [], [4], [], [], [], [], [], [], []]
    

### 广度优先搜索(BFS)
它其实是一种地毯式层层推进的搜索策略，即先查找离起始顶点最近的，然后是次近的，依次往外搜索。
![](https://static001.geekbang.org/resource/image/00/ea/002e9e54fb0d4dbf5462226d946fa1ea.jpg)
- visited：用来记录已经被访问的顶点，用来避免顶点被重复访问
- queue：用来存储已经被访问的、但连接的顶点还没有被访问的顶点
- prev：用来记录搜索路径
![](https://static001.geekbang.org/resource/image/4f/3a/4fea8c4505b342cfaf8cb0a93a65503a.jpg)
- 时间复杂度是O(V+E)，V表示顶点的个数，E表示边的个数。也可以简写为O(E)
- 空间复杂度是O(V)

### 深度优先搜索(DFS)
![](https://static001.geekbang.org/resource/image/87/85/8778201ce6ff7037c0b3f26b83efba85.jpg)
- 深度优先搜索代码也用到了prev、visited变量。除此之外，还用到了特殊变量found()，用来检测是否找到终点
- 时间复杂度是O(E)
- 空间复杂度是O(V)


```python
from typing import List, Optional, Generator, IO
from collections import deque

class Graph:
    """Undirected graph."""
    def __init__(self, num_vertices: int):
        self._num_vertices = num_vertices
        self._adjacency = [[] for _ in range(num_vertices)]

    def add_edge(self, s: int, t: int) -> None:
        self._adjacency[s].append(t)
        self._adjacency[t].append(s)

    def _generate_path(self, s: int, t: int, prev: List[Optional[int]]) -> Generator[str, None, None]:
        if prev[t] or s != t:
            yield from self._generate_path(s, prev[t], prev)
        yield str(t)

    def bfs(self, s: int, t: int) -> IO[str]:
        """Print out the path from Vertex s to Vertex t
        using bfs.
        """
        if s == t: return

        visited = [False] * self._num_vertices
        visited[s] = True
        q = deque()
        q.append(s)
        prev = [None] * self._num_vertices

        while q:
            v = q.popleft()
            for neighbour in self._adjacency[v]:
                if not visited[neighbour]:
                    prev[neighbour] = v
                    if neighbour == t:
                        print("->".join(self._generate_path(s, t, prev)))
                        return
                    visited[neighbour] = True
                    q.append(neighbour)

    def dfs(self, s: int, t: int) -> IO[str]:
        """Print out a path from Vertex s to Vertex t
        using dfs.
        """
        found = False
        visited = [False] * self._num_vertices
        prev = [None] * self._num_vertices

        def _dfs(from_vertex: int) -> None:
            nonlocal found
            if found: return
            visited[from_vertex] = True
            if from_vertex == t:
                found = True
                return
            for neighbour in self._adjacency[from_vertex]:
                if not visited[neighbour]:
                    prev[neighbour] = from_vertex
                    _dfs(neighbour)
        
        _dfs(s)
        print("->".join(self._generate_path(s, t, prev)))
```


```python
graph = Graph(8)

graph.add_edge(0, 1)
graph.add_edge(0, 3)
graph.add_edge(1, 2)
graph.add_edge(1, 4)
graph.add_edge(2, 5)
graph.add_edge(3, 4)
graph.add_edge(4, 5)
graph.add_edge(4, 6)
graph.add_edge(5, 7)
graph.add_edge(6, 7)

graph.bfs(0, 7)
graph.dfs(0, 7)
```

    0->1->2->5->7
    0->1->2->5->4->6->7
    


```python
def find_vertex_by_degree(graph, s, degree):
    if len(graph) <= 1:
        return []
    if degree == 0:
        return [s]
    d_vertices = []
    queue = deque()
    prev = [-1] * len(graph)
    visited = [False] * len(graph)
    visited[s] = True
    queue.append(s)
    while len(queue) > 0:
        sz = len(queue)
        for i in range(sz):
            v = queue.popleft()
            for adj_v in graph[v]:
                if not visited[adj_v]:
                    prev[adj_v] = v
                    visited[adj_v] = True
                    queue.append(adj_v)
        degree -= 1
        if degree == 0 and len(queue) != 0:
            return queue 
```


```python
g = Undigraph(8)
g.add_edge(0, 1)
g.add_edge(0, 3)
g.add_edge(1, 2)
g.add_edge(1, 4)
g.add_edge(2, 5)
g.add_edge(3, 4)
g.add_edge(4, 5)
g.add_edge(4, 6)
g.add_edge(5, 7)
g.add_edge(6, 7)
print(find_vertex_by_degree(g, 0, 4))
```

    deque([7])
    
