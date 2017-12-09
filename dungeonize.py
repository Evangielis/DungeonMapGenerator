import argparse
import xml.etree.ElementTree as ET

def parseSourceSink():
    parser = argparse.ArgumentParser(prog='dungeonize.py', description='Convert a tmx tilemaze into a dungeon')
    parser.add_argument('-f', nargs='?', required=True)
    parser.add_argument('-o', nargs='?', required=True)
    args = vars(parser.parse_args())
    return args['f'], args['o']



class Map:
    def __init__(self, path):
        t = ET.parse(path)
        self.root = t.getroot()
        l = self.root.find("./layer")
        self.height = int(l.attrib['height'])
        self.width = int(l.attrib['width'])
        c = l.find("./data").text
        self.matrix = [x == '5' for x in c.split(',')]

sourceFile, sinkFile = parseSourceSink()
m = Map(sourceFile)

print m.height, m.width, m.matrix





