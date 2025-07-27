grid = [list(input()) for _ in range(3)]
increments = [(1,0),(0,1),(-1,0),(0,-1),(1,1),(-1,1),(1,-1),(-1,-1)]
ans = "ZZZ"
for j  in range(len(grid)):
    for jj in range(len(grid)):
        for i in range(len(increments)):
            for ii in range(0,len(increments)):
                index_1x,index_1y = j, jj
                index_2x,index_2y = j+increments[i][0], jj+increments[i][1]
                index_3x,index_3y = index_2x+increments[ii][0], index_2y+increments[ii][1]
                if index_1x<0 or index_2x<0 or index_3x<0 or index_1y<0 or index_2y<0 or index_3y<0:
                    continue
                if index_1x>2 or index_2x>2 or index_3x>2 or index_1y>2 or index_2y>2 or index_3y>2:
                    continue
                if (index_1x,index_1y) == (index_2x,index_2y) or (index_2x,index_2y) == (index_3x,index_3y) or (index_3x,index_3y) == (index_1x,index_1y):
                    continue
                cur = grid[index_1x][index_1y]+grid[index_2x][index_2y]+grid[index_3x][index_3y]
                ans = min(cur,ans)
print(ans)