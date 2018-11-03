import sys

key = 404982000012063942418231892259
flag = []
p = 1

while True:
	flag.append('A')

	if 26 ** p > key:
		break
		
	key -= 26 ** p
	p += 1
	
idx = 0
p -= 1

while p > -1:
	flag[idx] = chr(ord(flag[idx]) + int(key / (26 ** p)))
	key %= 26 ** p
	p -= 1
	idx += 1
		
print("SVATTT2018{" + ''.join(flag) + '}')
