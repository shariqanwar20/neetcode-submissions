class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        """
        valid tree: connected and no cycle
        """
        adj_list = {}
        for i in range(n):
            adj_list[i] = []
        
        for parent, child in edges:
            adj_list[parent].append(child)
            adj_list[child].append(parent)

        queue = deque()
        visited = set()
        queue.append((0, None))
        visited.add(0)

        while queue:
            node, parent = queue.popleft()
            for neigh in adj_list[node]:
                if neigh == parent: continue
                if neigh in visited: return False
                
                visited.add(neigh)
                queue.append((neigh, node))
        
        return True if len(visited) == n else False




