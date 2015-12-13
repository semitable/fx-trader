import talib.abstract as ta
import pandas as pd
from history import History

class Study(object):
    """docstring for Study"""
    def __init__(self, name, f, param):
        super(Study, self).__init__()
        self.name = name
        self.f = f
        self.param = param

        self.result = None

    def run(self, hist):
        self.result =  self.f(hist *self.param)

    def get(self):
        return self.result
    def __str__(self):
        return str(self.name)

    def __add__(self, other):
        return self.result + other.result
    def __sub__(self,other):
        return self.result - other.result

    def __iter__(self):

class SMA(Study):
    """docstring for SMA"""
    def __init__(self, *args):#period = 30):
        super(SMA, self).__init__("SMA", ta.SMA, (args[0],))

class EMA(Study):
    """docstring for EMA"""
    def __init__(self, *args):# period = 30):
        super(EMA, self).__init__("EMA", ta.EMA, (args[0],))

class BBAND(Study):
    """docstring for BBAND"""
    def __init__(self, *args):# period = 5):
        super(BBAND, self).__init__("BBAND", ta.BBANDS, (args[0],))

class SAR(Study):
    """docstring for SAR"""
    def __init__(self, *args):# maxim=0,acc=0):
        super(SAR, self).__init__("SAR", ta.SAR, (args[0],args[1]))

class ADX(Study):
    """docstring for ADX"""
    def __init__(self, *args):# period =14):
        super(ADX, self).__init__("SMA", ta.ADX, (args[0],))

class MACD(Study):
    """docstring for SMA"""
    def __init__(self, *args):# periodshort=12, periodlong=26):
        super(MACD, self).__init__("MACD", ta.MACD, (args[0], args[1]))

class RSI(Study):
    """docstring for RSI"""
    def __init__(self, *args):# period=9):
        super(RSI, self).__init__("RSI", ta.RSI, (args[0],))

class ULTOSC(Study):
    """docstring for ULTOSC"""
    def __init__(self, *args):# periodshort=7, periodmed=14, periodlong=28):
        super(ULTOSC, self).__init__("ULTOSC", ta.ULTOSC, (args[0], args[1], args[2]))

class WILLR(Study):
    """docstring for WILLR"""
    def __init__(self, *args):# period =14):
        super(WILLR, self).__init__("WILLR", ta.WILLR, (args[0],))

class ATR(Study):
    """docstring for ATR"""
    def __init__(self, *args):# period=14):
        super(ATR, self).__init__("ATR",ta.ATR, (args[0],))
