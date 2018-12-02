import sys
import pdb
import argparse


def main_two(args):
    pass


def main_one(args):
    with open(args.filename) as file_open:
        data = file_open.readlines()

    count = 0
    array = [int(i) for i in data]
    index = 0

    try:
        while True:
            new_index = array[index]

            increment = 1
            if args.second and new_index >= 3:
                increment = -1
            array[index] += increment
                    
            count += 1
            index += new_index
    except:
        pass
    print count
        

parser = argparse.ArgumentParser()

parser.add_argument('filename')
parser.add_argument('-s', '--second', required=False, action='store_true')
args = parser.parse_args()

main_one(args)
