"""

Author : Robin Phoeng
Date : 21/06/2018


"""


"""
A stress bar in the Fate SRD
box indexes start at 1
"""
class Bar:
    def __init__(self,name):
        self.name = name
        self.boxes = []

    def add_box(self,box):
        assert isinstance(box,Box)
        self.boxes.append(box)

    def __getitem__(self, index):
        return self.boxes[index-1] # we start our indexing at 1.

    def __str__(self):
        output = ""
        output += self.name
        for box in self.boxes:
            output += "\n" + str(box)
        return output


"""
A bar consists of boxes
"""
class Box:

    def __init__(self,size):
        self.size = size
        self.used = False

    def spend(self):
        self.used = True

    def refresh(self):
        self.used = False

    def __str__(self):
        return "Size: " + str(self.size) + " Used :" + ("Y" if self.used else "N")


