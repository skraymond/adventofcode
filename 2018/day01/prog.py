import argparse

def main_one(args):
    
    n = 0
    for f in open(args.filename):
        n += int(f)
        print n
    print n
 
def main_two(args):
    
    n = 0
    past = [0] 
    while True:
        for f in open(args.filename):
            n += int(f)
    
            if n in past:
                print "Answer: " + str(n)
                exit()
            past.append(n)

 
parser = argparse.ArgumentParser()

parser.add_argument('filename')
parser.add_argument('-s', '--second', required=False, action='store_true')
args = parser.parse_args()

if args.second:
    main_two(args)
else:
    main_one(args)











