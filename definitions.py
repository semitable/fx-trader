from enum import Enum
import operator

class Pairs(Enum):
    EUR_USD = 0

cop = {
    '>': operator.gt,
    '<': operator.lt,
    '==': operator.eq
}
aop = {
    '+' : operator.add,
    '-' : operator.sub,
    '*' : operator.mul
}
lop = {
    'xor' : operator.xor,
    'and' : operator.and_,
    'or' : operator.or_
        }

class Bias(Enum):
    sSELL = 0
    SELL = 1
    HOLD =2
    BUY =3
    sBUY =4

class Position(Enum):
    BUY = 0
    SELL = 1
