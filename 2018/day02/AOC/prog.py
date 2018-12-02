import argparse
from day import answer


def main_one(args):
    print "first answer is " + str(answer(args.filename).execute())
    

def main_two(args):
    print "second answe is " + str(answer(args.filename).execute_two())


parser = argparse.ArgumentParser()
parser.add_argument('filename')
parser.add_argument('-s', '--second', required=False, action='store_true')
args = parser.parse_args()

if args.second:
    main_two(args)
else:
    main_one(args)



