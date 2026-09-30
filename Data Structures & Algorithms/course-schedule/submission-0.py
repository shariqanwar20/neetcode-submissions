class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        visited = set()

        nodes = {}

        for node_id in range(numCourses):
            nodes[node_id] = {'in': 0, 'out': set()}
        
        for node_id, pre_id in prerequisites:
            nodes[node_id]['in'] += 1
            nodes[pre_id]['out'].add(node_id)
        
        queue = deque()
        for node_id in nodes:
            if nodes[node_id]['in'] == 0:
                queue.append(node_id)
                visited.add(node_id)
        
        # bfs
        while queue:
            node_id = queue.popleft()
            for neigh in nodes[node_id]['out']:
                nodes[neigh]['in'] -= 1
                if nodes[neigh]['in'] == 0:
                    visited.add(neigh)
                    queue.append(neigh)


        if len(visited) == numCourses:
            return True
        return False