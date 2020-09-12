import sys
from Lexer import Lexer

def main():
    if len(sys.argv) != 2:
        print('Usage: Python Main.py FILENAME')
        return - 1

    filename = sys.argv[1]
    try:

        run = Lexer(filename)
        try:
            input = open(filename, "r")
            input.close()
            token = run.scan()

            while token is not None:
                print(token)
                token = run.scan()
            print("##FINISHED##")
        except FileNotFoundError:
            print("File not found")
            return - 1
    except FileNotFoundError:
        print("File not found")
        return - 1

if __name__ == "__main__":
    main()
