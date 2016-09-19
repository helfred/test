import argparse

parser=argparse.ArgumentParser()
parser.add_argument("-a", "--add", nargs="+", help="Creates local Linux account")
parser.add_argument("-d", "--delete", nargs="+", help="Removes local Linux account")
args = parser.parse_args()
if args.add:
	for u in args.add:
		print("Creating user(s): " + u)
elif args.delete:
	for u in args.delete:
		print("Deleting user(s): " + u)
