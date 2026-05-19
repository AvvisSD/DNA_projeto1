class Graph():
    def __init__(self,n):
        self.matrix=[[0 for i in range(n)] for j in range(n)]

    def nnodes(self):
        return len(self.matrix)

    def add(self,i,j,w):
        assert 0<= i< self.nnodes() and 0<=j< self.nnodes()
        self.matrix[i][j]=w

    def adjQ(self,i,j):
        assert 0<= i< self.nnodes() and 0<=j< self.nnodes()
        return self.matrix[i][j]>0

    def adj(self,i):
        r=[]
        for j in range(len(self.matrix)):
            if self.matrix[i][j]>0:
                r=r+[j]
        return r
        
    def __str__(self):
        return str(self.matrix)
        
    def weight(self,i,j):
        return self.matrix[i][j]

    def totalWeight(self):
        r=0
        for i in range(len(self.matrix)):
            for j in range(len(self.matrix[i])):
                r=r+self.matrix[i][j]
        return r   
