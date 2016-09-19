#! python3
# mapit.py - launches a map in the browser using address from the
# command line or clipboard

import webbrowser, sys, pyperclip

if len(sys.argv) > 1:
	# Get address from command line
	address = ' '.join(sys.argv[1:])
else:
	# Get address from clip board
	address = pyperclip.paste()

webbrowser.open('https://www.google.com/maps/place/' + address)
