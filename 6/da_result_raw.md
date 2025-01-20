0x10000:        mov     x2, #0
0x10004:        and     x0, x0, #0xffffffff
0x10008:        and     x1, x0, #0xf
0x1000c:        cmp     x1, #9
0x10010:        cinc    x2, x2, eq
0x10014:        lsr     x1, x0, #4
0x10018:        and     x1, x1, #0xf
0x1001c:        cmp     x1, xzr
0x10020:        cinc    x2, x2, eq
0x10024:        lsr     x1, x0, #8
0x10028:        and     x1, x1, #0xf
0x1002c:        cmp     x1, #0xe
0x10030:        cinc    x2, x2, eq
0x10034:        lsr     x1, x0, #0xc
0x10038:        and     x1, x1, #0xf
0x1003c:        cmp     x1, #8
0x10040:        cinc    x2, x2, eq
0x10044:        lsr     x1, x0, #0x10
0x10048:        and     x1, x1, #0xf
0x1004c:        cmp     x1, #0xe
0x10050:        cinc    x2, x2, eq
0x10054:        lsr     x1, x0, #0x14
0x10058:        and     x1, x1, #0xf
0x1005c:        cmp     x1, #2
0x10060:        cinc    x2, x2, eq
0x10064:        lsr     x1, x0, #0x18
0x10068:        and     x1, x1, #0xf
0x1006c:        cmp     x1, xzr
0x10070:        cinc    x2, x2, eq
0x10074:        lsr     x1, x0, #0x1c
0x10078:        and     x1, x1, #0xf
0x1007c:        cmp     x1, xzr
0x10080:        cinc    x2, x2, eq
0x10084:        mov     x1, #0x533
0x10088:        mul     x1, x0, x1
0x1008c:        cmp     x2, #8
0x10090:        cset    x0, eq