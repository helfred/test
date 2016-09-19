#! python3
# mapit.py - launches a map in the browser using address from the
# command line or clipboard

import webbrowser
import sys
import pyperclip
import argparse

def main():
    parser = argparse.ArgumentParser()

    parser.add_argument("address", help="Enter address to map", type=str)


if len(sys.argv) > 1:
    # Get address from command line
    address = ' '.join(sys.argv[1:])
else:
    # Get address from clip board
    address = pyperclip.paste()

webbrowser.open('https://www.google.com/maps/place/' + address)






if __name__ == '__main__':
    main()