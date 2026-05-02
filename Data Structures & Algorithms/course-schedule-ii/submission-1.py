class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        
        adj = [[] for c in range(numCourses)]

        indegree = [0] * numCourses

        for course, prereq in prerequisites:
            adj[prereq].append(course)
            indegree[course] += 1 
        
        q = deque()

        for course in range(numCourses):
            if indegree[course] == 0:
                q.append(course)

        order = []

        while q:
            course = q.popleft()
            order.append(course)

            for next_course in adj[course]:
                indegree[next_course] -= 1

                if indegree[next_course] == 0:
                    q.append(next_course)
        
        return order if len(order) == numCourses else []