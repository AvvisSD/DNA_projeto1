class Event():
    def __init__(self,t,k,w):
        self._time=t
        self._kind=k
        self._who=w
    def time(self):
        return self._time
    def kind(self):
        return self._kind
    def who(self):
        return self._who
    def __str__(self):
        return "time" + str(self.time) + "," + "kind=" + self._kind + "who=" + self._who