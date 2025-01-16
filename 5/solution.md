First, we need to disassemble the ARM64_CODE *0102A0D2C29397D2210002AA1F0001EBE0179F9A*

Use disassemble.py to get the result
```
0x10000:        mov     x1, #0x100000 // load the value 0x100000 into x1
0x10004:        mov     x2, #0xbc9e // load the value 0xbc9e into x2
0x10008:        orr     x1, x1, x2 // bitwise OR, *0x10BC9E*
0x1000c:        cmp     x0, x1 // compare x0 and x1
0x10010:        cset    x0, eq // if x0 is equal to x1, set x0 to 1, otherwise, set x0 to 0
```

So we know the correct value is 0x10BC9E, which, when converted to decimal, is *1096862*. Now, we just need to convert this number to base 36 to get the solution: **NICE**