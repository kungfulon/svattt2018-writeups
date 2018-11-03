from z3 import *

v0, v1, v2, v3, v4, v5, v6, v7, v8, v9, v10, v11, v12, v13, v14, v15, v16, v17, v18, v19, v20, v21, v22, v23, v24, v25, v26, v27, v28, v29, v30 = Ints('v0 v1 v2 v3 v4 v5 v6 v7 v8 v9 v10 v11 v12 v13 v14 v15 v16 v17 v18 v19 v20 v21 v22 v23 v24 v25 v26 v27 v28 v29 v30')
s = Solver();
s.add([v0 + v1 + v2 + v3 == 318,
v1 + v2 + v3 + v4 == 319,
v2 + v3 + v4 + v5 == 317,
v3 + v4 + v5 + v6 == 302,
v4 + v5 + v6 + v7 == 266,
v5 + v6 + v7 + v8 == 231,
v6 + v7 + v8 + v9 == 203,
v7 + v8 + v9 + v10 == 276,
v8 + v9 + v10 + v11 == 276,
v9 + v10 + v11 + v12 == 325,
v10 + v11 + v12 + v13 == 371,
v11 + v12 + v13 + v14 == 365,
v12 + v13 + v14 + v15 == 370,
v13 + v14 + v15 + v16 == 371,
v14 + v15 + v16 + v17 == 321,
v15 + v16 + v17 + v18 == 320,
v16 + v17 + v18 + v19 == 372,
v17 + v18 + v19 + v20 == 321,
v18 + v19 + v20 + v21 == 379,
v19 + v20 + v21 + v22 == 358,
v20 + v21 + v22 + v23 == 362,
v21 + v22 + v23 + v24 == 365,
v22 + v23 + v24 + v25 == 306,
v23 + v24 + v25 + v26 == 327,
v24 + v25 + v26 + v27 == 313,
v25 + v26 + v27 + v28 == 348,
v26 + v27 + v28 + v29 == 374,
v27 + v28 + v29 + v30 == 383,
v0 == ord('S'),
v1 == ord('V'),
v2 == ord('A'),
v3 == ord('T'),
v4 == ord('T'),
v5 == ord('T'),
v6 == ord('2'),
v7 == ord('0'),
v8 == ord('1'),
v9 == ord('8'),
v10 == ord('{'),
v30 == ord('}')])
s.check()
lines = str(s.model()).replace('[', '').replace(']', '').replace(',', '').replace('v', '').replace(" = ", " ").split('\n')
arr = []

for line in lines:
  args = line.strip().split()
  arr.append((int(args[0]), chr(int(args[1]))))

arr = sorted(arr)
flag = ""

for k, v in arr:
  flag += v

print(flag)
