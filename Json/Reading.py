import json


class Reading:
    def __init__(self, file, height, width):
        self.height = height
        self.width = width
        self.file = file

    def getfile(self):
        return self.file

    def getwidth(self):
        return self.width

    def gh(self):
        return self.height

    def read(self):
        with open(self.file, 'r') as f:
            p = json.load(f)
            print(p['width'])
            print(p['height'])
