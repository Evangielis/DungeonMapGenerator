import argparse
import random
from dunmap import Map

def parseArgs():
    parser = argparse.ArgumentParser(prog='dungeonize.py', description='Convert a tmx tilemaze into a dungeon')
    parser.add_argument('-f', required=True)
    parser.add_argument('-o')
    parser.add_argument('--modulo')
    parser.add_argument('--pel')
    args = vars(parser.parse_args())
    return args

# m=matrix, n=mod, r=range over
def moduloFill(m, n):
    mout = list(m)
    for x in range(0, len(mout)): 
        if (x % n == 0):
            mout[x]=True
    return mout

# m=matrix, p=0.5
def pPerElement(m, p=0.5):
    return [x if x else random.random() < p for x in m]

def transform(mp, methods):
    d = mp.matrix
    if methods['modulo']:
        d = moduloFill(d, float(methods['modulo']))
    if methods['pel']:
        d = pPerElement(d, float(methods['pel']))
    mp.matrix = d

### Import Args
args = parseArgs()
source = args['f']
sink = args['o']

### Import Map
mp = Map(source)

### Transform
transform(mp, args)

### Export Map
if not sink:
    print mp
else:
    mp.export(sink)