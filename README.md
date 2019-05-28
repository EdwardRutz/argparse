# argparse

>Demo of Python's standard library for providing user input via the command line, `argparse`.

- `args.py` requires a positional arguement
- `optional-args.py` the argument is optional
- `prog.py` uses both optional and positiona arguments

## Notes

- Use the help flag to see the help menu, `python prog.py --help`
- The `add_argument()` method, which is what we use to specify which command-line options the program is willing to accept.
- The `parse_args()` method actually returns some data from the options specified
-  argparse treats the options we give it as strings, unless we tell it otherwise.
- Convert string to integer, `type=int`
-  By default, if an optional argument isn’t specified, it gets the "None" value, 
  and it cannot be compared to an int value (hence the TypeError exception).


## Sources

- [argparse Tutorial](https://docs.python.org/3/howto/argparse.html#id1)
- [Learn Enough Python to be Useful: argparse](https://towardsdatascience.com/learn-enough-python-to-be-useful-argparse-e482e1764e05)


