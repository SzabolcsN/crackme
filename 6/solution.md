First, we need to disassemble the ARM64_CODE *020080D2007C4092010C40923F2400F14214829A01FC44D3210C40923F001FEB4214829A01FC48D3210C40923F3800F14214829A01FC4CD3210C40923F2000F14214829A01FC50D3210C40923F3800F14214829A01FC54D3210C40923F0800F14214829A01FC58D3210C40923F001FEB4214829A01FC5CD3210C40923F001FEB4214829A61A680D2017C019B5F2000F1E0179F9A*

Use disassemble.py to get the result (the original can be seen in the file named da_result_raw.md)
```
// x0 holds our 32-bit candidate
mov    x2, #0           // x2 will count how many nibble-conditions are met
and    x0, x0, #0xffffffff

// nibble0: (x0 >> 0) & 0xf must be 9
and    x1, x0, #0xf
cmp    x1, #9
cinc   x2, x2, eq       // if nibble0 == 9, increment x2

// nibble1: (x0 >> 4) & 0xf must be 0
lsr    x1, x0, #4
and    x1, x1, #0xf
cmp    x1, xzr
cinc   x2, x2, eq       // if nibble1 == 0, increment x2

// nibble2: (x0 >> 8) & 0xf must be 0xe
lsr    x1, x0, #8
and    x1, x1, #0xf
cmp    x1, #0xe
cinc   x2, x2, eq

// nibble3: (x0 >> 12) & 0xf must be 8
lsr    x1, x0, #0xc
and    x1, x1, #0xf
cmp    x1, #8
cinc   x2, x2, eq

// nibble4: (x0 >> 16) & 0xf must be 0xe
lsr    x1, x0, #0x10
and    x1, x1, #0xf
cmp    x1, #0xe
cinc   x2, x2, eq

// nibble5: (x0 >> 20) & 0xf must be 2
lsr    x1, x0, #0x14
and    x1, x1, #0xf
cmp    x1, #2
cinc   x2, x2, eq

// nibble6: (x0 >> 24) & 0xf must be 0
lsr    x1, x0, #0x18
and    x1, x1, #0xf
cmp    x1, xzr
cinc   x2, x2, eq

// nibble7: (x0 >> 28) & 0xf must be 0
lsr    x1, x0, #0x1c
and    x1, x1, #0xf
cmp    x1, xzr
cinc   x2, x2, eq
```

| NIBBLE                   | REQUIRED VALUE | HEX DIGIT |
|--------------------------|----------------|-----------|
| nibble0 (lowest 4 bits)  | 9              | 0x9       |
| nibble1                  | 0              | 0x0       |
| nibble2                  | 14             | 0xE       |
| nibble3                  | 8              | 0x8       |
| nibble4                  | 14             | 0xE       |
| nibble5                  | 2              | 0x2       |
| nibble6                  | 0              | 0x0       |
| nibble7 (highest 4 bits) | 0              | 0x0       |

```
 nibble7 nibble6 nibble5 nibble4 nibble3 nibble2 nibble1 nibble0
     0       0      2       E      8       E      0       9
```

*CINC x2, x2 eq* is a way to *increment if equal*, this sequence repeats eight times, checking each of the eight 4-bit fields

*correct 32-bit input is 0x002E8E09 (or simply 2E8E09)*

