import sys
import pdb
import argparse
import re


def main_two(args):
    pass


class port(object):
    def __init__(self, string):
        self.p1 = int(string.split('/')[0])
        self.p2 = int(string.split('/')[1])
        self._p1 = self.p1
        self._p2 = self.p2
        self.strength = self.p1 + self.p2

    def can_start(self):
        return self._p1 == 0 or self._p2 == 0

    def start(self):
        if self.p1 == 0:
            self.p1 = None
            return True
        if self.p2 == 0:
            self.p2 = None
            return True
        return False        

    def match(self, other):
        if self.p1 is not None:
            if self.p1 == other.p1:
#                self.p1 = None
#                other.p1 = None
                return True
            if self.p1 == other.p2:
#                self.p1 = None
#                other.p2 = None
                return True
        if self.p2 is not None:
            if self.p2 == other.p1:
#                self.p2 = None
#                other.p1 = None
                return True
            if self.p2 == other.p2:
#                self.p2 = None
#                other.p2 = None
                return True
        return False

    def __repr__(self):
        return self.__str__()
        
    def __str__(self):
        return "%d/%d" % (self._p1, self._p2)

    def __eq__(self, other):
        return self._p1 == other._p1 and self._p2 == other._p2


def main_one(args):
    with open(args.filename) as file_open:
        data = file_open.readlines()

    lst = [port(i) for i in data]
    all_nodes = list(lst)

    starters = []
    for l in lst:
        if l.can_start():
            starters.append([l])
        
    start_l = 0
    end_l = len(starters)
    count = 0
    while start_l != end_l:
        start_l = len(starters)
        enders = []
        for l in starters:
            new_possibles = get_possible(all_nodes, l)
            new_l = add_new_nodes(new_possibles, l, starters)
            for l in new_l:
                enders.append(l)
        end_l = len(enders)
        count += 1
        if count == 1000:
            pdb.set_trace()
        starters = enders

    pdb.set_trace()
    for s in starters:
        print s
        

def add_new_nodes(possible_nodes, current_array, already_found):
    return_l = []
#    return_l.append(list(current_array))
    last = current_array[len(current_array)-1]
    for possible in possible_nodes:
        if possible.match(last):
            new_l = list(current_array)
            new_l.append(possible)

            if new_l not in already_found:
                return_l.append(new_l)
    return return_l

        
def get_possible(all_nodes, used_nodes):
    return_nodes = list(all_nodes)
    for node in used_nodes:
        return_nodes.remove(node)
    return return_nodes


parser = argparse.ArgumentParser()

parser.add_argument('filename')
parser.add_argument('-s', '--second', required=False, action='store_true')
args = parser.parse_args()

main_one(args)
