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
        dic = {}
        valid = True
        row = [i.split() for i in row_w.split()]
        for phrase_w in row:
            phrase = str(phrase_w[0])
            
            if args.second:
                phrase = ''.join(sorted(phrase))
            if phrase in dic:
                valid = False
            dic[phrase] = None
        if valid:
            count += 1
        print str(row) + str(valid)
    print count
        

parser = argparse.ArgumentParser()

parser.add_argument('filename')
parser.add_argument('-s', '--second', required=False, action='store_true')
args = parser.parse_args()

main_one(args)
