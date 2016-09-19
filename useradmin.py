import argparse, sys, os, crypt
from datetime import date, timedelta

if not os.geteuid()==0:
	sys.exit("\nOnly root can create users, try sudo " + sys.argv[0] + " <users>\n")

now = date.today()
end = now + timedelta(days=5)
expire = end.isoformat()
password = "Password123"
encPassword = crypt.crypt(password, "a1")

parser=argparse.ArgumentParser()
parser.add_argument("-a", "--add", nargs="+", help="Creates local Linux account")
parser.add_argument("-d", "--delete", nargs="+", help="Removes local Linux account")
args = parser.parse_args()
if args.add:
	for u in args.add:
    	print("Creating user(s): " + u)
    	os.system("useradd -m -p " + encPassword + " " + u)
elif args.delete:
	for u in args.delete:
		print("Deleting user(s): " + u)
		os.system("userdel -r " + u)

