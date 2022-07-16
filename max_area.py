from logging.config import valid_ident
from netrc import netrc
from operator import ne
from tkinter import W


class Solution(object):

    def valid_travel(self, pos, seen: set, grid) -> bool:
        """
        Returns true if the position is within range has not been visited.
        """
        x = 0
        y = 1
        in_range_x = pos[x] < len(grid) and pos[x] >= 0
        if not in_range_x:
            return
        in_range_y = pos[y] < len(grid[pos[x]]) and pos[y] >= 0
        if not in_range_y:
            return
        not_seen = pos not in seen
        in_range = in_range_x and in_range_y
        valid =  not_seen and in_range
        is_area_space = valid and grid[pos[x]][pos[y]]
        return is_area_space 


    def travel(self, grid, seen, next) -> tuple:
        x = 0
        y = 1
        directions = [
        (next[x],     next[y] + 1),
        (next[x] + 1, next[y]),
        (next[x],     next[y] - 1),
        (next[x] - 1, next[y])
        ]
        for dir in directions:
            if self.valid_travel(dir, seen, grid):
                return dir
        return None

    def maxAreaOfIsland(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        seen = set()
        area = 0
        for x in range(len(grid)):
            for y in range(len(grid[x])):
                if grid[x][y] and (x,y) not in seen:
                    next = (x, y)
                    search_stack = [(x, y)]
                    seen.add((x, y))
                    cur_area = 0
                    while(search_stack):
                        old = next
                        next = self.travel(grid, seen, old)
                        # if None we found no more 1:s and need to backtrack
                        if not next:
                            search_stack.pop(0)
                            if search_stack:
                                next = search_stack[0]
                            cur_area += 1
                            continue
                        seen.add(next)
                        search_stack.insert(0, next)
                    
                    if cur_area > area:
                        area = cur_area

        return area
test = Solution()
# should return 9
print(test.maxAreaOfIsland([[0,1,0],
                            [1,1,1],
                            [0,1,0]]))