import pdb


class answer(object):

    def __init__(self, filename, oneline=None):
        if filename is not None:
            self.f = open(filename)
            self.data = self.f.readlines()
        else:
            self.data = []
            self.data.append(oneline)

    def execute(self):
        pass

    def execute_two(self):
        pass

