import argparse
import xml.etree.ElementTree as ET
import random

def parseSourceSink():
    parser = argparse.ArgumentParser(prog='dungeonize.py', description='Convert a tmx tilemaze into a dungeon')
    parser.add_argument('-f', required=True)
    parser.add_argument('-o')
    parser.add_argument('--modulo')
    parser.add_argument('--pel')
    args = vars(parser.parse_args())
    return args

class Map:
    def __init__(self, path):
        self.tree = ET.parse(path)
        self.root = self.tree.getroot()
        l = self.root.find("./layer")
        self.height = int(l.attrib['height'])
        self.width = int(l.attrib['width'])
        c = l.find("./data").text
        self.matrix = [x == '5' for x in c.split(',')]

    def export(self, path):
        data = self.root.find('./layer/data')
        text = ','.join(['5' if x else '0' for x in self.matrix])
        data.text = text
        self.tree.write(path)

    def __str__(self):
        st = []
        for i in range(0, self.height):
            l = (i * self.width)
            u = l + self.width
            s = self.matrix[l:u]
            st.append(''.join([' ' if x else 'O' for x in s]))
        return '\n'.join(st)

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
args = parseSourceSink()
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