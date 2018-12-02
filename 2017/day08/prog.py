import sys
import pdb
import argparse
import re


def main_two(args):
    pass


class registers(object):
    def __init__(self):
        self.reg = {}
        
    def get(self, key):
        if key not in self.reg:
            self.reg[key] = 0
        return self.reg[key]

    def set(self, key, val):
        if key not in self.reg:
            self.reg[key] = 0
        self.reg[key] = val

    def find_max(self):
        cur_max = (None, 0)
        for key in self.reg.keys():
            if self.reg[key] > cur_max[1]:
                cur_max = (key, self.reg[key])
        return cur_max
            


def main_one(args):
    
    with open(args.filename) as file_open:
        data = file_open.readlines()

    reg = registers()
    all_max = 0
    for line in data:
        instruct = line.split('if')[0].strip()
        cond = line.split('if')[1].strip()

        cond_one = cond.split()[0].strip()
        cond_pred = cond.split()[1].strip()
        cond_val = cond.split()[2].strip()

        reg_val = reg.get(cond_one)

        do_instruct = {'<': reg_val < int(cond_val),
                       '>': reg_val > int(cond_val),
                       '>=': reg_val >= int(cond_val),
                       '==': reg_val == int(cond_val),
                       '!=': reg_val != int(cond_val),
                       '<=': reg_val <= int(cond_val)}[cond_pred]
        if do_instruct:
            reg_w = instruct.split()[0].strip()
            do_a = instruct.split()[1].strip()
            amount = instruct.split()[2].strip()

            org = reg.get(reg_w)
            new_v = {'dec': org - int(amount),
                     'inc': org + int(amount)}[do_a]
            reg.set(reg_w, new_v)
        cur_max = reg.find_max()[1]
        all_max = max(all_max, cur_max)
    print reg.find_max()
    print all_max

parser = argparse.ArgumentParser()

parser.add_argument('filename')
parser.add_argument('-s', '--second', required=False, action='store_true')
args = parser.parse_args()

main_one(args)
