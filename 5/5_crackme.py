from unicorn import UC_ARCH_ARM64, UC_MODE_ARM
from unicorn.unicorn import Uc, UcError
from unicorn.arm64_const import UC_ARM64_REG_X0

def print_outcome(f):
    def wrapper():
        print("Valóban!" if (result := f()) else "Nem...", end="\n\n")
        return result
    return wrapper

ARM64_CODE = bytes.fromhex("0102A0D2C29397D2210002AA1F0001EBE0179F9A")
ADDRESS = 0x10000

@print_outcome
def is_wizard():
    x = input("What's the magic word? ")
    try:
        emulator = Uc(UC_ARCH_ARM64, UC_MODE_ARM)
        emulator.mem_map(ADDRESS, 1024)
        emulator.mem_write(ADDRESS, ARM64_CODE)
        emulator.reg_write(UC_ARM64_REG_X0, int(x, 36))
        emulator.emu_start(ADDRESS, ADDRESS + len(ARM64_CODE))
        return bool(emulator.reg_read(UC_ARM64_REG_X0))
    except UcError as e:
        print("Error: %s" % e)
        return False

if __name__ == '__main__':
    while True:
        if (is_wizard()): 
            break
