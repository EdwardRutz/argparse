

import argparse
parser = argparse.ArgumentParser()
parser.add_argument("square", type=int, 
                    help="display a square of a given number")  # Specify command-line arguments to accept
parser.add_argument("-v", "--verbosity", action="count", default=0,
                  help="increase output verbosity")
args = parser.parse_args()
answer = args.square**2
if args.verbosity >= 2:
    print("The square of {} is {}".format(args.square, answer))
elif args.verbosity >= 1:
    print("{}^2 equals {}".format(args.square, answer))
else:
    print(answer)
