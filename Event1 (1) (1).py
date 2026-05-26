from utils import *

class Event():
    def __init__(self,t,k,a,v):
        self._time=t
        self._kind=k
        self._ant=a
        self._vertice=v
        
    def time(self):
        return self._time
        
    def kind(self):
        return self._kind
        
    def ant(self):
        return self._ant
        
    def vertice(self):
        return self._vertice
        
    def __str__(self):
        return "time" + str(self._time) + "," + "kind=" + self._kind + "," + "ant=" + self._ant + "," + "vertice=" + str(self._vertice)