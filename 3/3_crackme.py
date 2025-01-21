from unicorn import UC_ARCH_ARM64, UC_MODE_ARM, UC_HOOK_MEM_INVALID, UC_HOOK_CODE
from unicorn.unicorn import Uc, UcError
from unicorn.arm64_const import UC_ARM64_REG_X0, UC_ARM64_REG_X1, UC_ARM64_REG_X2, UC_ARM64_REG_X3, UC_ARM64_REG_PC

ARM64_CODE = bytes.fromhex("1FA001F1E1010054E10321AA211C40923F2C03F161010054A50005CAA500028B630400D17F0000F1A1FFFF54268083D2BF0006EB61000054200080D202000014000080D2EADD97D2")
ADDRESS = 0x10000

def run_emulator():
    x = input("Enter your password: ")
    if len(x) != 4:
        print("Password must be 4 characters long!")
        return False
    try:
        emulator = Uc(UC_ARCH_ARM64, UC_MODE_ARM)
        emulator.mem_map(ADDRESS, 2 * 1024 * 1024)
        emulator.mem_write(ADDRESS, ARM64_CODE)
        emulator.reg_write(UC_ARM64_REG_PC, ADDRESS)
        emulator.reg_write(UC_ARM64_REG_X0, ord(x[0]))
        emulator.reg_write(UC_ARM64_REG_X1, ord(x[1])) 
        emulator.reg_write(UC_ARM64_REG_X2, ord(x[2])) 
        emulator.reg_write(UC_ARM64_REG_X3, ord(x[3])) 
        emulator.emu_start(ADDRESS, ADDRESS + len(ARM64_CODE)) 
        return bool(emulator.reg_read(UC_ARM64_REG_X0))
    except UcError as e:
        print("Error: %s" % e)
        return False

if __name__ == '__main__':
    while True:
        if (run_emulator()):
            print("Correct :)")
            break
        print("Try again...")