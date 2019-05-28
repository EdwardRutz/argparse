"""
Adding Optional Arguments
    The program is written so as to display something when --verbosity is specified 
      and display nothing when not.
    To show that the option is actually optional, there is no error when running the program without it. 
      Note that by default, if an optional argument isn’t used, the relevant variable 
      args.verbosity is given None as a value, which is the reason it fails the truth test 
      of the if statement.
    The help message is a bit different.
    When using the --verbosity option, one must also specify some value, any value.
"""


import argparse
parser = argparse.ArgumentParser()
parser.add_argument("--verbosity", help="increase help verbosity")
args = parser.parse_args()
if args.verbosity:
    print("verbosity turned on")