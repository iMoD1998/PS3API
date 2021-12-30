from enum import IntEnum
from ctypes import *
from ctypes import _SimpleCData
from ctypes import _Pointer
from .memutils import *

# RPC shelldcode/payload that will be used to call functions (See RPCPayload.s)
RPCPayload      = bytearray(b"\x7C\x08\x02\xA6\xF8\x01\xFF\xF8\xFB\xC1\xFF\xE8\xFB\xE1\xFF\xF0\xF8\x21\xFE\x01\x3F\xE0\x10\x05\x63\xFF\x10\x00\x83\xDF\x00\x70\x2C\x1E\x00\x00\x41\x82\x00\xF4\xD0\x21\x01\x78\xD0\x41\x01\x7C\xD0\x61\x01\x80\xD0\x81\x01\x84\xD0\xA1\x01\x88\xD0\xC1\x01\x8C\xD0\xE1\x01\x90\xD1\x01\x01\x94\xD1\x21\x01\x98\xF8\x61\x01\xA0\xF8\x81\x01\xA8\xF8\xA1\x01\xB0\xF8\xC1\x01\xB8\xF8\xE1\x01\xC0\xF9\x01\x01\xC8\xF9\x21\x01\xD0\xF9\x41\x01\xD8\xF9\x61\x01\xE0\xE8\x7F\x00\x00\xE8\x9F\x00\x08\xE8\xBF\x00\x10\xE8\xDF\x00\x18\xE8\xFF\x00\x20\xE9\x1F\x00\x28\xE9\x3F\x00\x30\xE9\x5F\x00\x38\xE9\x7F\x00\x40\xC0\x3F\x00\x48\xC0\x5F\x00\x4C\xC0\x7F\x00\x50\xC0\x9F\x00\x54\xC0\xBF\x00\x58\xC0\xDF\x00\x5C\xC0\xFF\x00\x60\xC1\x1F\x00\x64\xC1\x3F\x00\x68\x7F\xC9\x03\xA6\x4E\x80\x04\x21\xF8\x7F\x00\x78\xD0\x3F\x00\x80\x7F\xDE\xF2\x78\x93\xDF\x00\x70\xC0\x21\x01\x78\xC0\x41\x01\x7C\xC0\x61\x01\x80\xC0\x81\x01\x84\xC0\xA1\x01\x88\xC0\xC1\x01\x8C\xC0\xE1\x01\x90\xC1\x01\x01\x94\xC1\x21\x01\x98\xE8\x61\x01\xA0\xE8\x81\x01\xA8\xE8\xA1\x01\xB0\xE8\xC1\x01\xB8\xE8\xE1\x01\xC0\xE9\x01\x01\xC8\xE9\x21\x01\xD0\xE9\x41\x01\xD8\xE9\x61\x01\xE0\x38\x21\x02\x00\xE8\x01\xFF\xF8\x7C\x08\x03\xA6\x3F\xE0\xDE\xAD\x63\xFF\xBE\xEF\x7F\xE9\x03\xA6\xEB\xC1\xFF\xE8\xEB\xE1\xFF\xF0\x60\x00\x00\x00\x60\x00\x00\x00\x60\x00\x00\x00\x60\x00\x00\x00\x60\x00\x00\x00\x4E\x80\x04\x20\x7F\xE0\x00\x08")
# Free space to write function arguments.
RPCFreeSpace    = 0x10051000
# Extra space to write arguments that dont fit in a register ie. arrays, strings etc..
RPCArgDataSpace = RPCFreeSpace + 0x100

def RPCAddIntValue(Context, Value):
    Context.AddGPRegister(Value)

def RPCAddFloatValue(Context, Value):
    Context.AddFPRegister(Value)

def RPCAddString(Context, Value):
    Value += "\0"
    Context.AddGPRegister(Context.AddArgData(Value.encode("ascii")))

def RPCAddWString(Context, Value):
    Value += "\0"
    Context.AddGPRegister(Context.AddArgData(Value.encode("utf-16")))

RPCCTypeBasicTypes = {
    c_int8:    RPCAddIntValue,
    c_int16:   RPCAddIntValue,
    c_int32:   RPCAddIntValue,
    c_int64:   RPCAddIntValue,
    c_uint8:   RPCAddIntValue,
    c_uint16:  RPCAddIntValue,
    c_uint32:  RPCAddIntValue,
    c_uint64:  RPCAddIntValue,
    c_void_p:  RPCAddIntValue,
    c_float:   RPCAddFloatValue,
    c_char_p:  RPCAddString,
    c_wchar_p: RPCAddWString
}

class RPCCallContext:
    def __init__(self, ArgsAddress, ArgDataAddress):
        self.ArgsAddress        = ArgsAddress
        self.ArgDataAddress     = ArgDataAddress
        self.ArgumentsBuffer    = bytearray([ 0x0 ] * 0x100)
        self.ArgumentsData      = bytearray()
        self.ArgumentIntIndex   = 0
        self.ArgumentFloatIndex = 0
    
    def SetGPRegister(self, RegIndex, Value):
        RegOffset = (0x8 * RegIndex)
        self.ArgumentsBuffer[RegOffset:RegOffset+8] = PackInt64BE(Value)

    def AddGPRegister(self, Value):
        if self.ArgumentIntIndex > 9:
            raise Exception('Too many int args!')

        self.SetGPRegister(self.ArgumentIntIndex, Value)
        self.ArgumentIntIndex += 1

    def SetFPRegister(self, RegIndex, Value):
        RegOffset = (0x48 + (0x4 * RegIndex))
        self.ArgumentsBuffer[RegOffset:RegOffset+4] = PackIntFloatBE(Value)

    def AddFPRegister(self, Value):
        if self.ArgumentFloatIndex > 9:
            raise Exception('Too many int args!')

        self.SetFPRegister(self.ArgumentFloatIndex, Value)
        self.ArgumentFloatIndex += 1

    def AddArgData(self, Data):
        DataBeginOffset = len(self.ArgumentsData)
        self.ArgumentsData.extend(Data)
        return self.ArgDataAddress + DataBeginOffset

class RPCFunction:
    def __init__(self, API, Address):
        self.address  = Address
        self.argtypes = None
        self.restype  = None
        self.API      = API

    def __call__(self, *Args):
        ArgCount    = len(Args)
        CallContext = RPCCallContext(RPCFreeSpace, RPCArgDataSpace)

        if ArgCount != len(self.argtypes):
            raise Exception('Wrong number of args expected: ' + str(len(self.argtypes)))

        for i in range(0, ArgCount):
            ArgType  = self.argtypes[i]
            ArgValue = Args[i]
            
            # TODO: Support more complicated types, structures etc.
            if issubclass(self.argtypes[i], _SimpleCData):
                RPCCTypeBasicTypes[self.argtypes[i]](CallContext, ArgValue)
            #elif issubclass(self.argtypes[i], _Pointer):

        FinalPayload = CallContext.ArgumentsBuffer + CallContext.ArgumentsData

        # Set the function address to call in the payload.
        FinalPayload[0x70:0x74] = PackInt32BE(self.address)

        # Write payload
        self.API.WriteMemory(RPCFreeSpace, FinalPayload)

        # Wait for function to execute
        while self.API.ReadInt32(RPCFreeSpace + 0x70) != 0:
            pass

        # TODO: Support complicated return types??
        if self.restype:           
            if self.restype == c_float:
                return self.API.ReadFloat(RPCFreeSpace + 0x80)
            else:
                return self.API.ReadInt64(RPCFreeSpace + 0x78)
        
        return None

class RPC:
    def __init__(self, API):
        self.API = API
        self.Function = lambda Address: RPCFunction(API, Address)
        self.OriginalInstructions = bytearray()
    
    def Enable(self, HookAddress):
        # bla 0x10000
        HookPatch             = b'\x48\x01\x00\x02'
        HookAddressAfterPatch = HookAddress + len(HookPatch)

        # Check if we are already hooked.
        if self.API.ReadMemory(HookAddress, 4) == HookPatch:
            return

        '''
        0x124 lis   %r31, 0xDEADBEEF@h
        0x128 ori   %r31, %r31, 0xDEADBEEF@l
        0x12C mtctr %r31
        '''
        
        # Set the address to jump back to after our RPC payload has ran.
        RPCPayload[0x126:0x126+2] = PackInt16BE((HookAddressAfterPatch >> 16) & 0xFFFF)
        RPCPayload[0x12A:0x12A+2] = PackInt16BE(HookAddressAfterPatch & 0xFFFF)

        # Get original instructions
        self.OriginalInstructions = self.API.ReadMemory(HookAddress, len(HookPatch))

        RPCPayload[0x138:0x138+len(HookPatch)] = self.OriginalInstructions

        # Write payload at ELF header because retarded page prot
        self.API.WriteMemory(0x10000, RPCPayload)

        # Write branch for hook.
        self.API.WriteMemory(HookAddress, HookPatch)

    def Disable():
        self.API.WriteMemory(HookAddress, self.OriginalInstructions)