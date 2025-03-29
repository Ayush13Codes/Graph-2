class Solution:
    def criticalConnections(
        self, n: int, connections: List[List[int]]
    ) -> List[List[int]]:
        # T: O(m + n), S: O(m + n)
        def dfs(node, parent, time):
            nonlocal timer
            disc[node] = low[node] = timer
            timer += 1

            for neighbor in graph[node]:
                if neighbor == parent:
                    continue  # Ignore the edge leading to parent

                if disc[neighbor] == -1:  # If neighbor is unvisited
                    dfs(neighbor, node, time)
                    low[node] = min(low[node], low[neighbor])

                    # If no back edge, it's a critical connection
                    if low[neighbor] > disc[node]:
                        bridges.append([node, neighbor])
                else:
                    # Update low-link value
                    low[node] = min(low[node], disc[neighbor])

        # Step 1: Build the adjacency list
        graph = defaultdict(list)
        for u, v in connections:
            graph[u].append(v)
            graph[v].append(u)

        # Step 2: Initialize arrays
        disc = [-1] * n  # Discovery time of nodes
        low = [-1] * n  # Lowest discovery time reachable
        bridges = []
        timer = 0

        # Step 3: DFS from any unvisited node
        for i in range(n):
            if disc[i] == -1:
                dfs(i, -1, timer)

        return bridges
