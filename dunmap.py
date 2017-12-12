import xml.etree.ElementTree as ET

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