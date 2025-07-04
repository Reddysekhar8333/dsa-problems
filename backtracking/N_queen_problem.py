#51.leetcode problem 
"""
The n-queen puzzle is the problem of placing n queens on an N*N chessboard such that no two queens attack each other .
Given an integer n, return all distinct solutions to the n-queens puzzle.
you may return the answer in any order .
Each solution contains a distint board configuration of the n-queen's placement ,where 'Q' and '.' both indicate a queen and an empty space, respectively 
"""
class Solution:
    def solveNQueens(self,n:int)->list[list[str]]:
        col=set()
        posdiag=set()#(r+c)
        negdiag=set()#(r-c)
        result=[]
        board=[["."]*n for i in range(n)]
        def backtrack(r):
            if r==n:
                copy=["".join(row) for row in board]
                result.append(copy)
                return
            for c in range(n):
                if c in col or (r+c) in posdiag or (r-c) in negdiag:
                    continue
                col.add(c)
                posdiag.add(r+c)
                negdiag.add(r-c)
                board[r][c]="Q"
                backtrack(r+1)
                col.remove(c)
                posdiag.remove(r+c)
                negdiag.remove(r-c)
                board[r][c]="."
        backtrack(0)
        return result

if __name__=="__main__": # the execution starts here
    sq=Solution()
    ans=sq.solveNQueens(4)
    print(ans)