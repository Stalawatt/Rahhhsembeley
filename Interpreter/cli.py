import argparse
import Interpreter

if __name__ == "__main__":
    argsParser = argparse.ArgumentParser(description="An interpreter for XXX language.")
    argsParser.add_argument("file", required=True, help="Filename of the input file to interpret")
    file = argsParser.parse_args()

    

