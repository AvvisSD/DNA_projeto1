class DNAseq():

    def __init__(self):
        self.seq=[]
        
    def add(self,c):
        assert (c in [0,1,2,3])
        self.seq=self.seq + [c]
        
    def len(self):
        return len(self.seq)
        
    def pos(self,i):
        return self.seq[i]
        
    def prefix(self,n):
        new=DNAseq()
        new.seq=self.seq[:n]
        return new
        
    def suxfix(self,n):
        new=DNAseq()
        new.seq=self.seq[-n:]
        return new

    def conc(self,w):
        self.seq=self.seq + w.seq
    
    def __str__(self):
        return str(self.seq)
        
    def overlay(self,w):
        i = max(self.len(), w.len())
        while i > 0 and self.seq[-i:] != w.seq[:i]:
            i=i-1 
        return i

    def occursQ(self,w):
        found = False
        i = 0
        while i < w.len()-self.len()+1 and not found:
            if self.seq == w.seq[i:i+self.len()]:
                found = True
            i += 1
        return found