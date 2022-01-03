import struct
import sys

from keystone import * 
from pwn import *

from ps3api import RPCPayload
from ps3api.memutils import *

Keystone = Ks(KS_ARCH_PPC, KS_MODE_PPC64 | KS_MODE_BIG_ENDIAN)

with open(sys.argv[1], 'r') as asmfile:
    Encoding, Count = Keystone.asm(asmfile.read(), RPCPayload.LoadAddress)
    MachineCode     = bytes(Encoding)

    with open("RPCPayload.bin", "wb") as file:
        file.write(MachineCode)
        print("Saved to RPCPayload.bin")

    print("==HexDump==")
    print(hexdump(MachineCode))

    print("==Short Strings==")
    PayloadString = "bytearray(\n    b\""

    for i in range(0, len(Encoding)):
        if i % 4 == 0 and i != 0:
            PayloadString += "\"\n    b\""
        PayloadString += "\\x%02X" % Encoding[i]

    PayloadString += "\"\n)"

    print(PayloadString)

    print("==Long String==")

    print("\"" + "".join("\\x%02X" % Byte for Byte in Encoding) + "\"")

    print("==Offsets==")

    for i in range(0, len(Encoding), 4):
        Instruction = UnpackInt32BE(MachineCode[i:i+4])[0]
        if Instruction & 0xFFFF == 0xCAFE:
            print("ArgumentContextsHighOffset = 0x%X" % (i + 2))
        if Instruction & 0xFFFF == 0xBEEF:
            print("ArgumentContextsLowOffset = 0x%X" % (i + 2))
        if Instruction & 0xFFFF == 0xDEAD:
            print("BranchBackHighOffset = 0x%X" % (i + 2))
        if Instruction & 0xFFFF == 0xC0DE:
            print("BranchBackLowOffset = 0x%X" % (i + 2))
        if Instruction == 0x60000000:
            print("OriginalInstructionsOffset = 0x%X" % (i))
            break