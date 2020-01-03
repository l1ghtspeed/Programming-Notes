class Solution:
    def numIslands2(self, m: int, n: int, positions: List[List[int]]) -> List[int]:
        parents = [[-1] * m for j in range(n)]
        ranks = [[1] * m for j in range(n)]
        ret = [0]
        for x, y in positions:
            # init neighboring islands
            u = (x - 1, y) if x >= 0 and parents[x - 1][y] !=-1 else None
            d = (x + 1, y) if x + 1 < m and parents[x + 1][y] !=-1 else None
            l = (x, y - 1) if y - 1 >= 0 and parents[x][y -1] !=-1 else None
            r = (x, y + 1) if y + 1 < n and parents[x][y + 1] !=-1 else None
            
            # no neighboring islands
            if not u and not d and not l and not r:
                ret.append(ret[-1]+1)
                parents[x][y] = (x, y)
            
            # init neighboring island parents
            up = find(u) if u else None
            dp = find(d) if d else None
            lp = find(l) if l else None
            rp = find(r) if r else None
            
            if up and dp and up != dp:
                
            
        return ret[1:]
        
        # find island parent
        def find(cell):
            if parents[cell[0]][cell[1]] != cell:
                return find(parents[cel[0]][cel[1]])
            return cell
        