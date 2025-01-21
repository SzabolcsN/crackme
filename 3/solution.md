First, we need to disassemble the ARM64_CODE *1FA001F1E1010054E10321AA211C40923F2C03F161010054A50005CAA500028B630400D17F0000F1A1FFFF54268083D2BF0006EB61000054200080D202000014000080D2EADD97D2*

Use disassemble.py to get the result
```
0x00010000:  cmp     x0, #0x68        //  compare x0 to 0x68 (h)
0x00010004:  b.ne    #0x10040         //  if not equal jump to failure

0x00010008:  mvn     x1, x1           //  x1 = ~x1 bitwise NOT
0x0001000c:  and     x1, x1, #0xff    //  lower 8 bits
0x00010010:  cmp     x1, #0xcb        //  compare x1 to 0xcb
0x00010014:  b.ne    #0x10040         //  if not equal jump to failure

0x00010018:  eor     x5, x5, x5       //  x5 = 0
0x0001001c:  add     x5, x5, x2       //  x5 += x2
0x00010020:  sub     x3, x3, #1       //  x3 -= 1
0x00010024:  cmp     x3, #0           //  compare x3 to 0
0x00010028:  b.ne    #0x1001c         //  loop if x3 != 0

0x0001002c:  mov     x6, #0x1c01      //  x6 = 0x1c01 (7169)
0x00010030:  cmp     x5, x6           //  compare x5 to x6
0x00010034:  b.ne    #0x10040         //  if not equal jump to failure

0x00010038:  mov     x0, #1           //  x0 = 1 success
0x0001003c:  b       #0x10044         //  jump to end

0x00010040:  mov     x0, #0           //  x0 = 0 (failure)
0x00010044:  mov     x10, #0xbeef     //  not used
```

**First character**
*HEX: 0x68* is *ASCII: h*

**Second character**
0xff − 0xcb = 0x34
*HEX: 0x34* is *ASCII: 4*

**Third and fourth character** 
*x5* is set to *0* initially
loop: add *x2* value to *x5, x3* times *so x2 \* x3 = x5*
so we need factors of *#0x1c01 (7169)* because the code check if *x5 = 0x1c01*
Factors of *7169* are *67* and *107*
*ASCII 67* is *C*
*ASCII 107* is *k*