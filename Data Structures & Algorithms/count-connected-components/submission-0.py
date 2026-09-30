class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        # construct a hashmap/adj list
        # 0: [1, 2]   0-1
        # 1: [0]      |
        # 2: [0]      2
        adj_list = {}
        for i in range(n):
            adj_list[i] = []
        
        for src, dest in edges:
            adj_list[src].append(dest)
            adj_list[dest].append(src)
        

        # run dfs
        visited = set()
        def dfs(node):
            for neigh in adj_list[node]:
                if neigh not in visited:
                    visited.add(neigh)
                    dfs(neigh)


        # count number of times dfs ran
        res = 0
        for i in range(n):
            if i not in visited:
                res += 1
                visited.add(i)
                dfs(i)
                
        return res