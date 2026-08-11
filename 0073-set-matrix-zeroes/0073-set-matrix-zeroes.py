class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        m,n = len(matrix), len(matrix[0])
        marker = float('inf')
        print(m,n)
        def marki(i):
            for j in range(0,n):
                if matrix[i][j] !=0:
                    matrix[i][j] =marker
        def markj(j)  :
            for i in range(0,m):
                if matrix[i][j] !=0:
                    matrix[i][j] =marker  
        for i in range(0,m):
            for j in range(0,n) :
                if matrix[i][j] == 0:
                    marki(i)
                    markj(j)
        for i in range(0,m):
            for j in range(0,n) :
                if matrix[i][j]  == marker:
                    matrix[i][j]=0            
    # m,n = len(matrix), len(matrix[0])

                  
       

