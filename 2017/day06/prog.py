import sys
import pdb
import argparse


def main_two(args):
    pass


def main_one(args):
    with open(args.filename) as file_open:
        data = file_open.readlines()

    count = 0
    array = [int(i) for i in data[0].split()]
    index = 0

    prev = []

    while True:
        
        max_value = max(array)
        for i in range(len(array)):
            if array[i] == max_value:
                max_i = i
                break
        b2d = max_value
        array[max_i] = 0

        index = max_i
        while b2d > 0:
            index = (index + 1) % len(array)
            b2d -= 1
            array[index] += 1
        count += 1
        if array in prev:
            break
        prev.append(list(array))
    if args.second:
        count = 0

        look_for = list(array)

        while True:
            max_value = max(array)
            for i in range(len(array)):
                if array[i] == max_value:
                    max_i = i
                    break
            b2d = max_value
            array[max_i] = 0
    
            index = max_i
            while b2d > 0:
                index = (index + 1) % len(array)
                b2d -= 1
                array[index] += 1
            count += 1
            if array == look_for:
                break
        
    print array
    print count
        

parser = argparse.ArgumentParser()

parser.add_argument('filename')
parser.add_argument('-s', '--second', required=False, action='store_true')
args = parser.parse_args()

main_one(args)
