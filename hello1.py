import optparse

def main():
	parse = optparse.OptionParser()
	parse.add_option('--name', '-n', default="world", help="This prints out the name")
	opt, args = parse.parse_args()
	print("Hello " + str(opt.name))
if __name__ == "__main__":
	main()