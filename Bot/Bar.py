"""

Author : Robin Phoeng
Date : 21/06/2018


"""



class Bar:
    """
    A stress bar in the Fate SRD
    box indexes start at 1
    """
    def __init__(self,name):
        self.name = name
        self.boxes = []

    def add_box(self,box):
        '''
        Adds a new box to the bar
        :param box: a box, must be of Box type
        '''
        assert isinstance(box,Box)
        self.boxes.append(box)

    def __getitem__(self, index):
        '''
        retrieves an item
        we start our indexing at 1.
        :param index: index, must be integer
        :return: the Box at the index
        '''
        return self.boxes[index-1]

    def __str__(self):
        output = ""
        output += self.name
        for box in self.boxes:
            output += " " + str(box)
        return output



class Box:
    """
    A bar consists of boxes
    """
    def __init__(self,size):
        self.size = size
        self.used = False

    def spend(self):
        '''
        toggle a box as used
        '''
        self.used = True

    def refresh(self):
        '''
        Toggle a box as un-used
        '''
        self.used = False

    def __str__(self):
        if self.used:
            return "\033[0;31m[%d]\033[0m" % self.size
        else:
            return "\033[0;32m[%d]\033[0m" % self.size

