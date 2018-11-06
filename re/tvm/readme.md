# TVm

Bài này sẽ khá khoai nếu BTC không share 1 phần code làm hint. Trong hint thì có các macro cho từng phần của chương trình nên việc đọc hiểu dễ dàng hơn rất nhiều. Không chỉ thế, trong file còn có 1 cái ```#define TEA_CONST 0x9e3779b9``` để ta biết ngay chương trình dùng mã hóa TEA.

Để decrypt TEA, ta cần:
- Delta, chính là ```TEA_CONST```
- Key, 4 bytes

Bắt đầu phân tích chương trình:

``` cpp
VM_PUSH_I4(key.data[0] ^ KM0),
VM_STORE(MEM_POS_KEY),
VM_PUSH_I4(key.data[1] ^ KM1),
VM_STORE(MEM_POS_KEY + 1),
VM_PUSH_I4(key.data[2] ^ KM2),
VM_STORE(MEM_POS_KEY + 2),
VM_PUSH_I4(key.data[3] ^ KM3),
VM_STORE(MEM_POS_KEY + 3),
```

Vậy là key được lưu trong mem, nhưng đã được xor với ```KM0, KM1, KM2, KM3```. Việc tiếp theo của chúng ta là tìm 4 số này. Sau đoạn đẩy key vào trong mem, chương trình gọi hàm mã hóa input:

``` cpp
ENCRYPT_INPUT(0),
ENCRYPT_INPUT(2),
ENCRYPT_INPUT(4),
ENCRYPT_INPUT(6),
```

Sau một loạt các bước chuẩn bị, macro ```ENCRYPT_INPUT``` gọi ```ENCRYPT_LOOP```, cái này thực chất là gọi ```ENCRYPT_ITERATION``` 32 lần. Trong macro ```ENCRYPT_ITERATION``` ta thấy có 4 chỗ đẩy ```KM0, KM1, KM2, KM3``` vào stack. Như vậy là ta đã có đủ thông tin. Tiếp theo là lấy các số này ra từ binary. Tại hàm main, có đoạn:

``` cpp
// Mình đã thêm type STACK_VM để phân tích dễ dàng hơn
while ( v6.pc <= 0x3601 && off_404740[byte_401120[v6.pc]](&v6) )
{
    if ( v6.finished )
        return 0;
}
```

Vậy ta biết list handler là ```off_404740```, bytecode VM là ```byte_401120``` và size của bytecode là ```0x3601```. Trong hint đã có sẵn bảng opcode của VM, nhưng khi phân tích binary thì mình nhận ra ở giữa ```VmNop``` và ```VmPushI4``` là một opcode nữa, nó sẽ push 1 byte vào stack. Mình đặt tên nó là ```VmPushByte```. Sau một hồi phân tích để biết cách thức hoạt động của các opcode, mình viết disassembler để việc phân tích bytecode VM trở nên dễ dàng hơn (file ```disassembler.py```). ```Ctrl+E``` export ```byte_401120``` dưới dạng raw binary, cho chạy qua disassembler. Trace theo code đã disassemble, ta sẽ có được:

```
TEA_CONST_MASK ^ TEA_CONST = 0x8c033a98
TEA_CONST_MASK = 0x12344321
key.data[0] ^ KM0 = 0x58016041
key.data[1] ^ KM1 = 0xe9022f73
key.data[2] ^ KM2 = 0xade58ba1
key.data[3] ^ KM3 = 0xfe3fb6e7
KM0 = 0x12345678
KM1 = 0x87654321
KM2 = 0xdeadbeef
KM3 = 0xb00bdead
```

Đến đây ta đã có thể tính toán đủ thông tin cần thiết để decrypt TEA. Việc cuối cùng là dump ciphertext. Trong hàm main, có 1 đoạn gán 1 đống số, nhưng ta chỉ cần quan tâm 4 dòng sau:

``` cpp
// #define MEM_POS_TARGET_VALUE 16
*(_QWORD *)&v6.mem[16] = 0x98A7B9AFF92C9FADLL;
*(_QWORD *)&v6.mem[18] = 0x7D47CFE2D315641CLL;
*(_QWORD *)&v6.mem[20] = 0x96783142887E4D5LL;
*(_QWORD *)&v6.mem[22] = 0xABD84461C327347FLL;
```

Giờ chỉ cần input các dữ liệu đã có cho hàm decrypt (file ```decrypt.cpp```, dòng lệnh compile nằm ở đầu file), và ta có flag:

```
SVATTT2018{t3A_5t@ck_i5_s0_345y}
```
