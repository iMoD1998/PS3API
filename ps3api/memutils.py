import struct

'''
Byte Conversions
'''
PackInt8BE = struct.Struct('>B').pack
PackInt16BE = struct.Struct('>H').pack
PackInt32BE = struct.Struct('>L').pack
PackInt64BE = struct.Struct('>Q').pack
PackFloatBE = struct.Struct('>f').pack
PackDoubleBE = struct.Struct('>d').pack

UnpackInt8BE = struct.Struct('>B').unpack
UnpackInt16BE = struct.Struct('>H').unpack
UnpackInt32BE = struct.Struct('>L').unpack
UnpackInt64BE = struct.Struct('>Q').unpack
UnpackFloatBE = struct.Struct('>f').unpack
UnpackDoubleBE = struct.Struct('>d').unpack

def ReadInt8(ReadMemory):
    return lambda Address: UnpackInt8BE(ReadMemory(Address, 1))[0]

def ReadInt16(ReadMemory):
    return lambda Address: UnpackInt16BE(ReadMemory(Address, 2))[0]

def ReadInt32(ReadMemory):
    return lambda Address: UnpackInt32BE(ReadMemory(Address, 4))[0]

def ReadInt64(ReadMemory):
    return lambda Address: UnpackInt64BE(ReadMemory(Address, 8))[0]

def ReadFloat(ReadMemory):
    return lambda Address: UnpackFloatBE(ReadMemory(Address, 4))[0]

def ReadDouble(ReadMemory):
    return lambda Address: UnpackDoubleBE(ReadMemory(Address, 8))[0]

def ReadString(ReadMemory):
    return lambda Address, Encoding="ascii", MaxLength=1024 : ReadMemory(Address, MaxLength).decode(Encoding).split("\x00")[0]

def WriteInt8(WriteMemory):
    return lambda Address, Value: WriteMemory(Address, PackInt8BE(Value))

def WriteInt16(WriteMemory):
    return lambda Address, Value: WriteMemory(Address, PackInt16BE(Value))

def WriteInt32(WriteMemory):
    return lambda Address, Value: WriteMemory(Address, PackInt32BE(Value))

def WriteInt64(WriteMemory):
    return lambda Address, Value: WriteMemory(Address, PackInt64BE(Value))

def WriteFloat(WriteMemory):
    return lambda Address, Value: WriteMemory(Address, PackFloatBE(Value))

def WriteDouble(WriteMemory):
    return lambda Address, Value: WriteMemory(Address, PackDoubleBE(Value))

def WriteString(WriteMemory):
    return lambda Address, String, Encoding="ascii": WriteMemory(Address, String.encode(Encoding) + b"\x00")