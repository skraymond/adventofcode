import sys
import pdb
import argparse


def main_two(args):
    pass


def main_one(args):
    with open(args.filename) as file_open:
        data = file_open.readlines()
    
    count = 0
    for row_w in data:
        row = [int(i) for i in row_w.split()]
        max_i = row[0]
        min_i = row[0]

        if not args.second:
            for i in row:
                min_i = min(min_i, i)
                max_i = max(max_i, i)
        else:
            for i in row:
                for x in row:
                    if i == x:
                        continue
                    if x % i == 0:
                        min_i = i
                        max_i = x
        print "%d/%d" % (max_i, min_i)
        
        def one(x, y):
            return x - y

        def two(x, y):
            return x / y
        add = one
        if args.second:
            add = two
        count += add(max_i, min_i)
    print count
        

parser = argparse.ArgumentParser()

parser.add_argument('filename')
parser.add_argument('-s', '--second', required=False, action='store_true')
args = parser.parse_args()

main_one(args)
