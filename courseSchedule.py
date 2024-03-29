import collections

class Solution(object):
    def canFinish(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: bool
        """
        # Constant defined for course state
        # NOT_CHECKED, CHECKING, COMPLETED = 0, 1, 2
        #
        # # -------------------------------
        #
        # def has_deadlock( course ):
        #
        #     if course_state[course] == CHECKING:
        #         # There is a cycle(i.e., deadlock ) in prerequisites
        #         return True
        #
        #     elif course_state[course] == COMPLETED:
        #         # current course has been checked and marked as completed
        #         return False
        #
        #
        #
        #     # update current course as checking
        #     course_state[course] = CHECKING
        #
        #     # check pre_course in DFS and detect whether there is deadlock
        #     for pre_course in requirement[course]:
        #
        #         if has_deadlock( pre_course ):
        #             # deadlock is found, impossible to finish all courses
        #             return True
        #
        #
        #     # update current course as completed
        #     course_state[course] = COMPLETED
        #
        #     return False
        #
        # # -------------------------------
        #
        # # each course maintain a list of its own prerequisites
        # requirement = collections.defaultdict( list )
        #
        # for course, pre_course in prerequisites:
        #     requirement[course].append( pre_course )
        #
        #
        # # each course maintain a state among {NOT_CHECKED, CHECKING, COMPLETED}
        # # Initial state is NOT_CHECKED
        # course_state = [ NOT_CHECKED for _ in range(numCourses) ]
        #
        # # Launch cycle (i.e., deadlock ) detection in DFS
        # for course_idx in range(0, numCourses):
        #
        #     if has_deadlock(course_idx):
        #         # deadlock is found, impossible to finish all courses
        #         return False
        #
        # # we can finish all course with required order
        # return True

        self.graph = collections.defaultdict(list)

        for pre in prerequisites:
            self.graph[pre[0]].append(pre[1])

        self.visited = [0] * numCourses
        self.FoundCyle = False

        for idx in range(numCourses):
            if self.FoundCyle == True:
                break
            if self.visited[idx] == 0:
                self.helper(idx)

        return self.FoundCyle

    def helper(self, node):

        self.visited[node] = 1

        for nei in self.graph[node]:
            if self.visited[nei] == 0:
                self.helper(nei)
            if self.visited[nei] == 1:
                self.FoundCyle = True

        self.visited[node] = 2


#n = 4
#prerequisities = [[1,0],[2,0],[3,1],[3,2]]
#n = 2
#prerequisities = [[0, 1], [1, 0]]
n = 2
prerequisities = [[0, 1]]

print(Solution().canFinish(n, prerequisities))