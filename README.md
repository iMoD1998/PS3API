# PS3API
PS3 API for TMAPI and CCAPI in python.

## **Note**
This only works on 32 bit python as TMAPI and CCAPI are 32 bit DLLs.

## Examples
### Connecting and Attaching
```python
from ps3api import PS3API

PS3 = PS3API(PS3API.API_TMAPI)

if PS3.ConnectTarget(PS3.GetDefaultTarget()) == False:
	raise Exception("Failed to connect to PS3.")

if PS3.AttachProcess() == False:
	raise Exception("Failed to attach to process.")
```

### Memory
#### Reading
```python
PS3.ReadMemory(Address, NumBytes)
PS3.ReadInt8(Address)
PS3.ReadInt16(Address)
PS3.ReadInt32(Address)
PS3.ReadInt64(Address)
PS3.ReadFloat(Address)
PS3.ReadDouble(Address)
PS3.ReadString(Address, Encoding="ascii", MaxLength=1024)
```
#### Writing
```python
PS3.WriteMemory(Address, Bytes)
PS3.WriteInt8(Address, Value)
PS3.WriteInt16(Address, Value)
PS3.WriteInt32(Address, Value)
PS3.WriteInt64(Address, Value)
PS3.WriteFloat(Address, Value)
PS3.WriteDouble(Address, Value)
PS3.WriteString(Address, Value, Encoding="ascii")
```

### Remote Procedure Call (RPC)
```python
PS3.RPC.Enable(0x02539F8) # MW2 1.14

CG_BoldGameMessage = PS3.RPC.Function(0x0005EF68)
CG_BoldGameMessage.argtypes = [ ctypes.c_ulong, ctypes.c_char_p ]

CG_BoldGameMessage(0, "Hello World!")
```

### Interacting With C API
```python
>>> PS3.API.NativeAPI.SNPS3InitTargetComms()
<SNReturnCode.SN_S_OK: 0>
```
or 
```python
>>> from ps3api import TMAPIExports
>>> C_API = TMAPIExports()
>>> C_API.SNPS3InitTargetComms()
<SNReturnCode.SN_S_OK: 0>
```

### Useful Scripts
#### Assembler
```python
>>> from keystone import *
>>> from pwn import * # for hex dump
>>> Keystone = Ks(KS_ARCH_PPC, KS_MODE_64 | KS_MODE_BIG_ENDIAN)
>>> Encoding, Count = Keystone.asm("li %r3, 0x1234\nblr")
>>> print(hexdump(bytes(Encoding)))
00000000  38 60 12 34  4e 80 00 20                            │8`·4│N·· │
00000008
```

#### Disassembler
```python
>>> from capstone import *
>>> Capstone = Cs(CS_ARCH_PPC, CS_MODE_64 | CS_MODE_BIG_ENDIAN)
>>> for i in Capstone.disasm(PS3.ReadMemory(0x10000, 0xE0), 0x10000):
...   print("0x%x:\t%s\t%s" %(i.address, i.mnemonic, i.op_str))
...
0x10000:        mflr    r0
0x10004:        std     r0, -8(r1)
0x10008:        std     r30, -0x18(r1)
0x1000c:        std     r31, -0x10(r1)
0x10010:        stdu    r1, -0x200(r1)
0x10014:        lis     r31, 0x1005
0x10018:        ori     r31, r31, 0x1000
0x1001c:        lwz     r30, 0x70(r31)
0x10020:        cmpwi   r30, 0
0x10024:        beq     0x10118
0x10028:        stfs    f1, 0x178(r1)
....
```