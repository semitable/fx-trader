
from study import *

population = 64


010101010100011101010101010000101010101010101010001010111100001110111011010010101010101101111010101011101010011101010111010
----
(diff(SMA(20)-SMA(35)) > 4 ) or SAR(34)>SAR(23) and (BBAND(23)[1]) => uint8



OUT =>
00 sSELL
01 SELL
11 BUY
10 sBUY
    


chr_signal = {
    'operator' = set('+', '-', '*', 'and', 'or', 'xor', '==', '>', '<'),
    'study' = set(SMA, EMA, BBAND, SAR, ADX, MACD, RSI, ULTOSC, WILLR, ATTR),
    'real' = float
}
class SignalGene = {
    pool = set('+', '-', '*', 'and', 'or', 'xor', '==', '>', '<',SMA, EMA, BBAND, SAR, ADX, MACD, RSI, ULTOSC, WILLR, ATTR)
    op_dict = {
        0000 : '+',
        0001 : '-',
        0011 : '*',
        0010 : 'and',
        0110 : 'or',
        0111 : 'xor',
        0101 : '==',
        0100 : '!=',
        1100 : '>=',
        1101 : '<=',
        1111 : '>',
        1110 : '<',
        1010 : SAR,
        1011 : ADX,
        1001 : MACD,
        1000 : RSI
    }

}

class Mutable(object):
    """Any child class has the ability to "Mutate" or "Cross" and has a fitness() function"""
    def __init__(self):
        self.genes = None
    def mutate(self):
        raise NotImplementedError
    def cross(self, other):
        raise NotImplementedError
    def fitness(self):
        raise NotImplementedError



class Signal(Mutable):
    """generate() Creates the signal. get(time) returns a BIAS at the selected time"""

    def __init__(self):
        pass

    def generate(self):
        self.result = None

    def get(self, time):
        pass
