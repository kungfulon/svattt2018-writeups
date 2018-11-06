// g++ decrypt.cpp -o decrypt -Wall -O2 -std=c++17

#include <bits/stdc++.h>

void dec(uint32_t *v, uint32_t *k) {
    uint32_t n = 32, delta = 0x8c033a98 ^ 0x12344321, sum = delta * n, y = v[0], z = v[1];
    
    while (n--) {
        z -= ((y << 4) + k[2]) ^ (y + sum) ^ ((y >> 5) + k[3]);
        y -= ((z << 4) + k[0]) ^ (z + sum) ^ ((z >> 5) + k[1]);
        sum -= delta; 
    }

    v[0] = y, v[1] = z; 
}

uint32_t CIPHER[8]; 
uint32_t key[4];

void out(uint32_t x) {
    char tmp[5];
    *(uint32_t *)tmp = x;
    tmp[4] = 0;
    printf("%s", tmp);
}

int main() {
    *(uint64_t *)CIPHER = 0x98A7B9AFF92C9FADULL;
    *(uint64_t *)(CIPHER + 2) = 0x7D47CFE2D315641CULL;
    *(uint64_t *)(CIPHER + 4) = 0x96783142887E4D5ULL;
    *(uint64_t *)(CIPHER + 6) = 0xABD84461C327347FULL;	
    
    key[0] = 0x12345678 ^ 0x58016041;
    key[1] = 0x87654321 ^ 0xE9022F73;
    key[2] = 0xDEADBEEF ^ 0xADE58BA1;
    key[3] = 0xB00BDEAD ^ 0xFE3FB6E7;
    
    for (int i = 0; i < sizeof(CIPHER) / sizeof(CIPHER[0]); i += 2) {
        dec(CIPHER + i, key);
        out(CIPHER[i]);
        out(CIPHER[i + 1]);
    }
}
