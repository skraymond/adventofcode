import sys
import pdb
import argparse
import re


def main_two(args):
    pass


class program(object):
    def __init__(self, string):
        self.name = string.split()[0].strip()
        self._weight = int(re.split('[()]', string)[1])
        self.parent = None
        try:
            self.kids_names = [s.strip() for s in
                               string.split('->')[1].split(',')]
            self.kids = []
        except:
            self.kids_names = []
            self.kids = None

    def weight(self):
        r = self._weight
        if self.kids is not None:
            for kid in self.kids:
                r += kid.weight()
        return r

    def __repr__(self):
        return str(self)

    def __str__(self):
        return "%s (%d) -> %s" % (self.name, self._weight,
                                  str(self.kids_names))


def main_one(args):
    with open(args.filename) as file_open:
        data = file_open.readlines()

    dic = {i.split()[0].strip(): program(i) for i in data}
    for key in dic:
        cur = dic[key.strip()]
        if cur.kids is None:
            continue
        for name in cur.kids_names:
            dic[name].parent = cur
            cur.kids.append(dic[name])

    root = None
    for key in dic:
        cur = dic[key]
        if cur.parent is None:
            root = cur
    #print str(root)

   # print root.weight()

    def kid_count(node):
        if node.kids is None:
            return
        if len(node.kids) < 3:
            print "Bad kids: " + str(node)
        for kid in node.kids:
            kid_count(kid)

#    kid_count(root)

    def find_bad(node):

        if node.kids is None:
            raise Exception("No kids: %s", str(node))
        
        kids_weights = {kid: kid.weight() for kid in node.kids}
        weight_counts = {i: kids_weights.values().count(i)
                         for i in kids_weights.values()}
        keys = weight_counts.keys()
        if len(keys) == 1:
            print "Node with mismatch: " + str(node)
            parent = node.parent
            print "----"
            print str(parent)
            for kid in parent.kids:
                print "\t" + str(kid.weight()) + "\t" + str(kid)
            print "++++"
            return
        bad_weight = keys[0]
        if weight_counts[keys[0]] > weight_counts[keys[1]]:
            bad_weight = keys[1]
        mismatch = None
        for kid in kids_weights:
            if kids_weights[kid] == bad_weight:
                if mismatch is not None:
                    raise Exception("Found two mismatches! ")
                mismatch = kid
        if mismatch is None:
            print "No mismatch! " + str(mismatch)
        find_bad(mismatch)

    find_bad(root)


parser = argparse.ArgumentParser()

parser.add_argument('filename')
parser.add_argument('-s', '--second', required=False, action='store_true')
args = parser.parse_args()

main_one(args)
