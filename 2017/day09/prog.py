import sys
import pdb
import argparse
import re


def main_two(args):
    pass


class program(object):
    def __init__(self, string):
        self.name = string.split()[0].strip()
        self.weight = int(re.split('[()]', string)[1])
        self.parent = None
        try:
            self.kids_names = [s.strip() for s in string.split('->')[1].split(',')]
            self.kids = []
        except:
            self.kids_names = []
            self.kids = None
        
    def __str__(self):
        return "%s (%d) -> %s <- %s" % (self.name, self.weight,
                                        str(self.kids_names),
                                        str(self.parent))


def main_one(args):
    with open(args.filename) as file_open:
        data = file_open.readlines()

    array = [i.strip() for i in data]
    new_array = []
    for row in array:
        print row
        if args.print_out:
            print row
        in_g = False
        next_ignore = False
        for i in range(len(row)):
            char = row[i]
            if next_ignore:
                next_ignore = False
                row = "%sk%s" % (row[:i], row[i+1:])
                continue
            if char == '<' and not in_g:
                in_g = True
            if char == '>' and in_g:
                in_g = False
            if char == '!' and in_g:
                row = "%sk%s" % (row[:i], row[i+1:])
                next_ignore = True
        new_array.append(row.replace('k',''))
        print row.replace('k','')
        print
        if args.print_out:
            print row
            print

    array = new_array
    new_array = []
    for row in array:
        print row
        try:
            print row
            new_array = []
            count = 0
            total = 0
            in_g = False
            for i in range(len(row)):
#                pdb.set_trace()
                char = row[i]
                if char == '<' and not in_g:
                    in_g = True
                    row = "%sk%s" % (row[:i], row[i+1:])
                if char == '>':
                    should = True
                    z = i
                    check_c = row[z-1]
                    while check_c != 'k':
                        if check_c != '>' \
                           and check_c != 'k' and check_c != '!':
                            count += 1
                        if check_c == 'k':
                            should = False
                        z -= 1
                        check_c = row[z]

            print "--%d--" % (count-1)
            print
        except:
            raise
            print "bad"
            print

#    array = new_array
#    new_array = []
#    for row in array:
#        if args.print_out:
#            print row
#        in_g = False
#        next_ignore = False        
#        garbage = 0
#        for i in range(len(row)):
#            char = row[i]
#            if char == '<' and not in_g:
#                in_g = True
#            if char == '>' and in_g:
#                row = "%s %s" % (row[:i], row[i+1:])
#                in_g = False
#            if in_g:
#                if char != '!' and char != '>':
#                    garbage += 1
#                row = "%s %s" % (row[:i], row[i+1:])
#                continue
#        print "Garbage: " + str(garbage-1)
#        new_array.append(row)
#        if args.print_out:
#            print row
#            print
#
#    array = new_array
#    new_array = []
#    for row in array:
#        row = row.replace(' ', '')
#        row = row.replace(',', '')
#        new_array.append(row)
#
#    array = new_array
#    new_array = []
#    for row in array:
#        try:
#            print row
#            new_array = []
#            count = 1
#            total = 0
#            for i in range(len(row)):
##                pdb.set_trace()
#                char = row[i]
#                if char == '{':
#                    new_array.append(count)
#                    new_array.append(char)
#                    count += 1
#                if char == '}':
#                    count -= 1
#                    should = True
#                    while should:
#                        str_val = new_array.pop()
#                        if str_val == '{':
#                            val = new_array.pop()
#                            new_array.append(val)
#                            should = False
#                        else:
#                            total += str_val
#
#            print "%s\t%s\t%d\t%d" % (str(new_array), 
#                                      count, total + 1, garbage)
#            print
#        except:
#            raise
#            print "bad"
#            print
#
#            


parser = argparse.ArgumentParser()

parser.add_argument('filename')
parser.add_argument('-s', '--second', required=False, action='store_true')
parser.add_argument('-p', '--print-out', required=False, action='store_true')
args = parser.parse_args()

main_one(args)
