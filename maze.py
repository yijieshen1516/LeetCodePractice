class Solution(object):
    def hasPath(self, maze, start, destination):
        """
        :type maze: List[List[int]]
        :type start: List[int]
        :type destination: List[int]
        :rtype: bool
        """

        visited = set()

        return self.helper(start[0], start[1], maze, visited, start, destination)

    def helper(self, i, j, maze, visited, start, destination):

        if i < 0 or i >=len(maze) or j < 0 or j >= len(maze[0]) or maze[i][j] == 1 or (i, j) in visited:
            return False

        if [i, j] == destination:
            return True

        visited.add((i, j))

        return self.helper(i+1, j, maze, visited, start, destination) or self.helper(i-1, j, maze, visited, start, destination) or self.helper(i, j+1, maze, visited, start, destination) or self.helper(i, j-1, maze, visited, start, destination)
