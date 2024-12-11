import argparse,sys
from .Interpreter import begin_program


def cli():
    argsParser = argparse.ArgumentParser(description="An interpreter for XXX language.")
    argsParser.add_argument("File", type=argparse.FileType('r'), default=sys.stdin, help="Filename of the input file to interpret")
    args = argsParser.parse_args()
    begin_program(args.File)



