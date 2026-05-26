from Event import*

class CEP():
    def _init_(self):
        self._lis=[]
    def addE(self,e):
        self._lis=[x for x in self._lis if x.time()<=e.time()] + [e] + [x for x in self._lis if x.time()>e.time()]
    def firstE(self):
        return self._lis[0]

    def delE(self):
        self._lis=self._lis[1:]
    def _str_(self):
        s=""
        for e in self._lis:
            s=s+str(e)+"\n"
        return s
        