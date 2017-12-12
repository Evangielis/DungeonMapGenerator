import argparse
import random
from dunmap import Map

def parseArgs():
    parser = argparse.ArgumentParser(prog='dungen.py', description='Generate a dungeon')
    parser.add_argument('-H', required=True)
    parser.add_argument('-W', required=True)
    args = vars(parser.parse_args())
    return args

def growTree(w, h):
    m = [None]*(w * h)
    q = [int(len(m)/2)]

    while (len(q) > 0):
    

args = parseArgs()
growTree(int(args['W']), int(args['H']))