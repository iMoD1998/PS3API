# PS3API
PS3 API for TMAPI and CCAPI in python.

## Examples
### Connecting and Attaching
```python
from ps3api import PS3API

PS3 = PS3API(PS3API.API_TMAPI)

if PS3.ConnectTarget(PS3.API.GetDefaultTarget()) == False:
	raise Exception("Failed to connect to PS3.")

if PS3.AttachProcess() == False:
	raise Exception("Failed to attach to process.")
```

### Memory
```python
PS3.ReadMemory(Address, NumBytes)
PS3.ReadInt8(Address)
PS3.ReadInt16(Address)
PS3.ReadInt32(Address)
PS3.ReadInt64(Address)
PS3.ReadFloat(Address)
PS3.ReadDouble(Address)
PS3.ReadString(Address, Encoding="ascii", MaxLength=1024)

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