class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        visited=[[0]*len(grid[0]) for i in range(len(grid))]
        def dfs(row,col):
            visited[row][col]=1
            if row+1<len(grid) and col>=0 and grid[row+1][col]=='1' and visited[row+1][col]==0:
                dfs(row+1,col)
            if row-1>=0 and col>=0 and grid[row-1][col]=='1' and visited[row-1][col]==0:
                dfs(row-1,col)
            if row>=0 and col+1<len(grid[0]) and grid[row][col+1]=='1' and  visited[row][col+1]==0:
                dfs(row,col+1)
            if row>=0 and col-1>=0 and grid[row][col-1]=='1' and visited[row][col-1]==0:
                dfs(row,col-1)
        count=0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if visited[i][j]==0 and grid[i][j]=='1':
                    count+=1
                    dfs(i,j)
        return count
            
