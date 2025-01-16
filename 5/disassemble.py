from capstone import Cs, CS_ARCH_ARM64, CS_MODE_ARM

ARM64_CODE = bytes.fromhex("0102A0D2C29397D2210002AA1F0001EBE0179F9A")
ADDRESS = 0x10000

md = Cs(CS_ARCH_ARM64, CS_MODE_ARM)

print("Disassembled ARM64 Code:")
for instruction in md.disasm(ARM64_CODE, ADDRESS):
    print(f"0x{instruction.address:x}:\t{instruction.mnemonic}\t{instruction.op_str}")
