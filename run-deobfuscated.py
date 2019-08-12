import time, os
d1 = '\033[1;90m'
r1 = '\033[1;91m'
g1 = '\033[1;92m'
y1 = '\033[1;93m'
b1 = '\033[1;94m'
p1 = '\033[1;95m'
c1 = '\033[1;96m'
w1 = '\033[1;97m'
d0 = '\033[0;90m'
r0 = '\033[0;91m'
g0 = '\033[0;92m'
y0 = '\033[0;93m'
b0 = '\033[0;94m'
p0 = '\033[0;95m'
c0 = '\033[0;96m'
w0 = '\033[0;97m'
re = '\033[0;0m'
os.system("clear")
try:
	print(f"""\n\n
 {p1}* {c1}PACMAN ENCRYPTER for python
 {p1}* {d0}Code by njank soekamti
""")
	print(f"   {p1}> {w0}example   {p1}:  {w0}/$HOME/path/file.py")
	file=input(f"   {p1}> {w0}filepath  {p1}:  {w0}")
	try:
		open(file).read
	except FileNotFoundError:
		exit(f"\n   {r1}x {w0}file not found\n")
	os.system(f"python2 .emoji.py -i {file} -o ENC{file}")
	print(f"\n   {g1}- {w0}file encrypted")
	time.sleep(1);os.system("xdg-open https://youtube.com/NjankSoekamti")
	exit(f"   {g1}  {w0}saved {p1}: {w0}ENC{file}\n")
except KeyboardInterrupt:
	exit(f"\n   {r1}x {w0}exiting program\n")

