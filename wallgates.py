class Solution(object):
    def wallsAndGates(self, rooms):
        """
        :type rooms: List[List[int]]
        :rtype: None Do not return anything, modify rooms in-place instead.
        """

        for i in range(len(rooms)):
            for j in range(len(rooms[0])):
                if rooms[i][j] == 0:
                    q=[(i, j)]
                    self.bfs(rooms, i, j, q)
                    print('one finished')

        return rooms

    def bfs(self, rooms, i, j, q):

        directions = [(-1, 0), (1, 0), (0, 1), (0, -1)]

        while q:
            row, col= q.pop(0)
            for direction in directions:
                new_row = row+direction[0]
                new_col = col+direction[1]

                if 0<=new_row<len(rooms) and 0<=new_col<len(rooms[0]) and rooms[new_row][new_col] == 2147483647:
                    rooms[new_row][new_col] = rooms[row][col]+1
                    q.append((new_row, new_col))


rooms = [[2147483647,-1,0,2147483647],[2147483647,2147483647,2147483647,-1],[2147483647,-1,2147483647,-1],[0,-1,2147483647,2147483647]]
print(Solution().wallsAndGates(rooms))