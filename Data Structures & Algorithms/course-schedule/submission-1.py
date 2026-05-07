from heapq import *
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        courses = {course for pair in prerequisites for course in pair}
        indegrees = defaultdict(int)
        edges = defaultdict(list)
        for course, prereq in prerequisites:
            indegrees[course] += 1
            edges[prereq].append(course)
        for course in courses:
            if course not in indegrees:
                indegrees[course] = 0
        # print(edges)
        indegrees_list = [(val, key) for key, val in indegrees.items()]
        heapify(indegrees_list)
        if len(indegrees) == 0:
            return True
        # print(indegrees_list)
        # print(indegrees)
        # print(edges)
        while len(indegrees_list) > 0:
            ind, course = heappop(indegrees_list)
            # print(ind, course)
            # print(indegrees)
            if ind == 0:
                del indegrees[course]
                for c in edges[course]:
                    indegrees[c] -= 1
                    # if indegrees[c] == 0:
                    #     del indegrees[c]
            else:
                # print(ind)
                return False
            indegrees_list = [(val, key) for key, val in indegrees.items()]
            heapify(indegrees_list)
        # print(indegrees)
        return True