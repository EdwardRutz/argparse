"""
Using Positional Arguements

    - add_argument() method is used to specify which command-line options the program accepts which is `echo`
    - Calling the program now requires an option to be specified.
    - The parse_args() method actually returns some data from the options specified, in this case, echo.
    - There is no need to specify which variable that value is stored in. 

"""

import argparse
parser = argparse.ArgumentParser()
parser.add_argument("echo", help="echo the string you use here")
args = parser.parse_args()
print(args.echo)