from unicorn import UC_ARCH_ARM64, UC_MODE_ARM
from unicorn.unicorn import Uc, UcError
from unicorn.arm64_const import UC_ARM64_REG_X0, UC_ARM64_REG_X1
import hashlib

KEY = "8b702ceda67e92c5e0b4"
INDEXES = [41, 0, 3, 34, 49, 46, 25, 58, 30]

def verify_pin(code):
    result = hashlib.sha256(code.encode()).hexdigest()
    if result[5:25] == KEY:
        return "".join(chr(int(result[i:i+2], 16)) for i in INDEXES)
    return False

def access_granted(f):
    granted, pin = f()
    if granted and (flag := verify_pin(pin)):
        print("[+] Access Granted.\n")
        print(f"+{'-'*22}+")
        print(f"|{' '*4}FLAG-{flag}{' '*4}|")
        print(f"+{'-'*22}+\n")
        return True
    print("[-] Access Denied.\n")
    return False


ARM64_CODE = bytes.fromhex("020080D2007C4092010C40923F2400F14214829A01FC44D3210C40923F001FEB4214829A01FC48D3210C40923F3800F14214829A01FC4CD3210C40923F2000F14214829A01FC50D3210C40923F3800F14214829A01FC54D3210C40923F0800F14214829A01FC58D3210C40923F001FEB4214829A01FC5CD3210C40923F001FEB4214829A61A680D2017C019B5F2000F1E0179F9A")
ADDRESS = 0x10000

def gateway():
    x = input("[*] Enter Access Code: ")
    try:
        emulator = Uc(UC_ARCH_ARM64, UC_MODE_ARM)
        emulator.mem_map(ADDRESS, 1024)
        emulator.mem_write(ADDRESS, ARM64_CODE)
        emulator.reg_write(UC_ARM64_REG_X0, int(x, 16))
        emulator.emu_start(ADDRESS, ADDRESS + len(ARM64_CODE))
        x0 = emulator.reg_read(UC_ARM64_REG_X0)
        x1 = emulator.reg_read(UC_ARM64_REG_X1)
        return bool(x0), str(x1)

    except UcError as e:
        print("Error: %s" % e)
        return 0

if __name__ == '__main__':
    while True:
        if (access_granted(gateway)): 
            break





