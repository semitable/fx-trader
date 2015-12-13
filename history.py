import pandas as pd

class History(object):
    """docstring for Hist"""
    def __init__(self, history, pointer=0):
        super(History, self).__init__()
        self.value = history
        self.pointer = pointer

    def view(self):
        return self.value[:self.pointer]
    def viewall(self):
        return self.value
    def current(self):
        return self.value[self.pointer]
    def forward(self):
        self.pointer = self.pointer + 1
    def append(self,candle):
        self.value = pd.concat([self.value, candle])
