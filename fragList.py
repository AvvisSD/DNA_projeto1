class FragList():
    def __init__(self):
        self.list=[]
        
    def add(self,w):
        self.list=self.list + [w] 
        
    def len(self):
        return len(self.list)
        
    def pos(self,i):
        if 0<=i<len(self.list):
            return self.list[i]
        elif i>len(self.list): 
            print("nº natural > ao ao comprimento da lista") 
        
    def __str__(self):
        res = "["
        i = 0
        while i < len(self.list):
            res = res + str(self.list[i]) + ","
            i = i + 1
        res = res + "]"
        return str(res)

    def purge(self):
        lb=set() #lista dos bons
        n=len(self.list)
        for i in range(n):
            b = True
            j=0
            while j < n and b:
                if i != j:
                    if self.list[i].occursQ(self.list[j]):                     
                        b=False
                j=j+1        
            if b:
                lb.add(self.list[i]) #se n enonctrar 
        self.list=list(lb)
        