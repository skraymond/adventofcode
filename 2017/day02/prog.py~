import sys
import pdb
import argparse


def main_two(args):
    with open(args.filename) as file_open:
        data = file_open.readlines()

    count = 0
    data = data[0].strip()
    half = len(data) / 2
    
    def next(num):
        return (num + half) % len(data)
    
    for i in range(len(data)/2):
        if int(data[i]) == int(data[next(i)]):
            count += int(data[i]) + int(data[next(i)])
    print count


def main_one(args):
    with open(args.filename) as file_open:
        data = file_open.readlines()

    data = data[0].strip()
    prev = data[len(data) - 1]
    count = 0
    for i in data:
        if prev is None:
            prev = i
            continue
        if int(i) == int(prev):
            count += int(i)
        prev = i
    print count


parser = argparse.ArgumentParser()

parser.add_argument('filename')
parser.add_argument('-s', '--second', required=False, action='store_true')
args = parser.parse_args()

if args.second:
    main_two(args)
else:
    main_one(args)
