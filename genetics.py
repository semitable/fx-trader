

import numpy as np
import operator


from study import *


population = 64

'''
0101 0101 0100 0111 0101 0101 0100 0010 1010 1010 1010 1010 0010 1011 1100 0011 1011 1011 0100 1010 1010 1011 0111 1010 1010 1110 1010 0111 0101 0111 0110
----
(diff(SMA(20)-SMA(35)) > 4 ) or SAR(34)>SAR(23) and (BBAND(23)[1])  ==> TRUE/FALSE(sSELL)
--------FLOAT---------          ------FLOAT----      ---FLOAT---
-----------BOOL------------


OUT =>
000 sSELL   TRUE
001 SELL    FALSE
011 HOLD    TRUE
111 BUY     FALSE
110 sBUY    FALSE

set(SMA, EMA, BBAND, SAR, ADX, MACD, RSI, ULTOSC, WILLR, ATTR)
set('+', '-', '*', 'and', 'or', 'xor', '==', '>', '<', 'diff'),


'''


class DNA(object):
    dperiod = 7
    keylen = 5
    mask = np.uint64(2**keylen - 1)


    studies = set([EMA, SMA, SAR, ADX, MACD, RSI, ULTOSC, WILLR, ATR, BBAND])
    gene_dict = {
        0b00000 : operator.add, 0b00001 : operator.sub, 0b00011 : operator.mul, 0b00010 : None,
        0b00110 : operator.or_, 0b00111 : operator.xor, 0b00101 : operator.and_,
        0b00100 : '!=', 0b01100 : '>=', 0b01101 : '<=', 0b01111 : operator.gt, 0b01110 : operator.lt, 0b01010 : operator.eq,
        0b01011 : EMA, 0b01001 : SMA, 0b01000 : SAR, 0b11000 : ADX, 0b11001 : MACD, 0b11011 : RSI, 0b11010 : ULTOSC, 0b11110 : WILLR, 0b11111 : ATR, 0b11101 : BBAND,
        0b11100 : 'f', 0b10100 : 'i', 0b10101 : None, 0b10111 : None, 0b10110 : None, 0b10010 : None, 0b10011 : None, 0b10001 : None, 0b10000 : None
    }
    def __init__(self):
        self.G = np.uint32([23465,13464,67494,24375,2345,6745])
        self.I = np.ones(32, dtype=np.uint32)*DNA.dperiod
        self.F = np.ones(32)

        self.curF = 0
        self.curI = 0


class Gene(object):
    def __init__(self):
        self.v = np.uint32()
    def __iter__(self):
        pass
    def __next__(self):
        pass

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



dna = SignalDNA()
dna.decode()
