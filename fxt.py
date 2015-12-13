import pandas as pd
import numpy as np
from study import *
## Declare Global Variables ##
#oanda = oandapy.API(environment="practice", access_token="21771806357801a589d16cdb0a49c33e-b0b29f1dda8909844e5a50e6995ac2f3")## get your "access_token" from Oanda - this will allow the script to access your accounts - SO USE IT WITH CARE!!!
## There are 3 potential 'environments': 'live', 'practice' and 'sandbox'.  Check out the docs at Oanda REST API developer pages for more information.
#account_id= 9533284 ## this will eventually be set to the account number item in the account list



pair='EUR_USD' ## declare 'pair' variable
back_hist = pd.read_csv('EURUSD_1H.csv', names=['time', 'open', 'high', 'low', 'close', 'volume'], header=0)
h = back_hist[['open', 'high', 'low', 'close']]
f = SMA(20)
f.run(h)
g = SMA(10)
g.run(h)


'''
#global variables
multithread = False

def main():
    #p = Pool(8)
    for generation in range(generations):
        gDNA = []
        traders = []
        best = None
        if(multithread):
            gDNA = p.map(worker, [best for i in range(popsize)])
        else:
            for pop in range (popsize):
                gDNA.append(worker(best))
        best = max(gDNA, key=attrgetter('fitness'))
        DNA.mutationRate = max(0.05, DNA.mutationRate - 0.1*DNA.mutationRate)
        #print(DNA.mutationRate)
        print()
        print("Time: " + str(best.runtime) + "  Generation: " + str(generation) + ". Max Profit:  " + str(best.fitness) + "   Mean Profit: " + str(sum(d.fitness for d in gDNA)/len(gDNA)), flush=True)
        print(best.args, flush=True)

if __name__ == '__main__':
    main()
'''
