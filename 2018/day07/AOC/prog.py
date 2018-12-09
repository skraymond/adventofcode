import argparse
from day import answer


def main_one(args):
    print "First answer: " + str(answer(args.filename).execute())
    

def main_two(args):
    a = answer(args.filename)
    a.execute_two()
    print "Second answer: " + str(a.seconds)


parser = argparse.ArgumentParser()
parser.add_argument('filename')
parser.add_argument('-s', '--second', required=False, action='store_true')
args = parser.parse_args()

if args.second:
    main_two(args)
else:
    main_one(args)



