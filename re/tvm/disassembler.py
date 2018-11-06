import sys

def main():
    with open(sys.argv[1], "rb") as f:
        bytecode = f.read()
        i = 0
        
        while i < len(bytecode):
            op = bytecode[i]
            i += 1
        
            if op == 0:
                print("nop")
            elif op == 1:
                print("push " + hex(bytecode[i]))
                i += 1
            elif op == 2:
                print("push " + hex((bytecode[i + 3] << 24) | (bytecode[i + 2] << 16) | (bytecode[i + 1] << 8) | bytecode[i]))
                i += 4
            elif op == 3:
                print("load " + hex(bytecode[i]))
                i += 1
            elif op == 4:
                print("ltid")
            elif op == 5:
                print("stor " + hex(bytecode[i]))
                i += 1
            elif op == 6:
                print("add")
            elif op == 7:
                print("sub")
            elif op == 8:
                print("mul")
            elif op == 9:
                print("and")
            elif op == 10:
                print("or")
            elif op == 11:
                print("xor")
            elif op == 12:
                print("not")
            elif op == 13:
                print("shl")
            elif op == 14:
                print("shr")
            elif op == 15:
                print("iz")
            elif op == 16:
                print("putc")
            elif op == 17:
                print("exit")

if __name__ == "__main__":
    main()
