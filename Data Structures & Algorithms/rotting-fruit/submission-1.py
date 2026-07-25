class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        q=deque()
        t=0
        count=0
        count1=0
        visited=[[0]*len(grid[0]) for i in range(len(grid))]
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j]==2:
                    q.append((2,i,j))
                if grid[i][j]==1:
                    count=count+1
        if count==0:
            return 0

        while len(q)!=0:
            for i in range(len(q)):
                node,row,col=q.popleft()
                if row+1<len(grid) and col>=0:
                    if grid[row+1][col]==1:
                        if visited[row+1][col]==0:
                            q.append((2,row+1,col))
                            visited[row+1][col]=1
                            count1=count1+1
                            grid[row+1][col]=2
                if row-1>=0 and col>=0:
                    if grid[row-1][col]==1:
                        if visited[row-1][col]==0:
                            q.append((grid[row-1][col],row-1,col))
                            visited[row-1][col]=1
                            count1=count1+1
                            grid[row-1][col]=2
                if row>=0 and col-1>=0:
                    if grid[row][col-1]==1:
                        if visited[row][col-1]==0:
                            q.append((grid[row][col-1],row,col-1))
                            visited[row][col-1]=1
                            count1=count1+1
                            grid[row][col-1]=2
                if row>=0 and col+1<len(grid[0]):
                    if grid[row][col+1]==1:
                        if visited[row][col+1]==0:
                            q.append((grid[row][col+1],row,col+1))
                            visited[row][col+1]=1
                            count1=count1+1
                            grid[row][col+1]=2
            t+=1
            if count==count1:
                return t
        return -1
        



                