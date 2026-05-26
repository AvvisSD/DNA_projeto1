class Ant():
    def __init__(self,g,i):
        self.graph=g
        self.list=[i]
        
    def last(self):
        return self.list[-1]

    def add(self,j):
        lastnnode=self.list[-1]
        if self.graph.weight(lastnnode,j)!=0:
            self.list=self.list+[j]
        
    def len(self):
        return len(self.list)

    def pop(self):
        if self.list==[]:
            return []
        else:
            self.list=self.list[:-1]

    def path(self):
        return self.list

    def weight(self):
        w=0
        for i in range(len(self.list)-1):
            w+=self.graph.weight(self.list[i],self.list[i+1])
        return w
    def hamiltonianQ(self):
        found=True
        if self.len() != self.graph.nnodes():
            found=False
        i = 0
        while i< self.len() -1 and found:
            j=i+1
            while j < self.len() and found:
                if self.list[i] ==self.list[j]:
                    found=False
                j += 1
            i+=1
        return found

    def extendableQ(self,d):
        return d not in self.list

    def __str__(self):
        return str(self.list)

    