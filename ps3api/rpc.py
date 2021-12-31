from enum import IntEnum
from ctypes import *
from ctypes import _SimpleCData
from ctypes import _Pointer
from .memutils import *

class RPCPayload:
    # RPC shelldcode/payload that will be used to call functions (See RPCPayload.s)
    PayloadData = bytearray(
        b"\x7C\x08\x02\xA6"
        b"\xF8\x01\xFF\xF8"
        b"\xFB\xA1\xFF\xE0"
        b"\xFB\xC1\xFF\xE8"
        b"\xFB\xE1\xFF\xF0"
        b"\xF8\x21\xFE\x01"
        b"\x3F\xE0\xCA\xFE"
        b"\x63\xFF\xBE\xEF"
        b"\x83\xDF\x00\x70"
        b"\x2C\x1E\x00\x00"
        b"\x41\x82\x00\xF4"
        b"\xD8\x21\x00\xF0"
        b"\xD8\x41\x00\xF8"
        b"\xD8\x61\x01\x00"
        b"\xD8\x81\x01\x68"
        b"\xD8\xA1\x01\x70"
        b"\xD8\xC1\x01\x78"
        b"\xD8\xE1\x01\x80"
        b"\xD9\x01\x01\x88"
        b"\xD9\x21\x01\x90"
        b"\xF8\x61\x01\x98"
        b"\xF8\x81\x01\xA0"
        b"\xF8\xA1\x01\xA8"
        b"\xF8\xC1\x01\xB0"
        b"\xF8\xE1\x01\xB8"
        b"\xF9\x01\x01\xC0"
        b"\xF9\x21\x01\xC8"
        b"\xF9\x41\x01\xD0"
        b"\xF9\x61\x01\xD8"
        b"\xE8\x7F\x00\x00"
        b"\xE8\x9F\x00\x08"
        b"\xE8\xBF\x00\x10"
        b"\xE8\xDF\x00\x18"
        b"\xE8\xFF\x00\x20"
        b"\xE9\x1F\x00\x28"
        b"\xE9\x3F\x00\x30"
        b"\xE9\x5F\x00\x38"
        b"\xE9\x7F\x00\x40"
        b"\xC0\x3F\x00\x48"
        b"\xC0\x5F\x00\x4C"
        b"\xC0\x7F\x00\x50"
        b"\xC0\x9F\x00\x54"
        b"\xC0\xBF\x00\x58"
        b"\xC0\xDF\x00\x5C"
        b"\xC0\xFF\x00\x60"
        b"\xC1\x1F\x00\x64"
        b"\xC1\x3F\x00\x68"
        b"\x7F\xC9\x03\xA6"
        b"\x4E\x80\x04\x21"
        b"\xF8\x7F\x00\x78"
        b"\xD0\x3F\x00\x80"
        b"\x7F\xDE\xF2\x78"
        b"\x93\xDF\x00\x70"
        b"\xC8\x21\x00\xF0"
        b"\xC8\x41\x00\xF8"
        b"\xC8\x61\x01\x00"
        b"\xC8\x81\x01\x68"
        b"\xC8\xA1\x01\x70"
        b"\xC8\xC1\x01\x78"
        b"\xC8\xE1\x01\x80"
        b"\xC9\x01\x01\x88"
        b"\xC9\x21\x01\x90"
        b"\xE8\x61\x01\x98"
        b"\xE8\x81\x01\xA0"
        b"\xE8\xA1\x01\xA8"
        b"\xE8\xC1\x01\xB0"
        b"\xE8\xE1\x01\xB8"
        b"\xE9\x01\x01\xC0"
        b"\xE9\x21\x01\xC8"
        b"\xE9\x41\x01\xD0"
        b"\xE9\x61\x01\xD8"
        b"\x38\x21\x02\x00"
        b"\xE8\x01\xFF\xF8"
        b"\x7C\x08\x03\xA6"
        b"\x3F\xE0\xDE\xAD"
        b"\x63\xFF\xC0\xDE"
        b"\x7F\xE9\x03\xA6"
        b"\xEB\xA1\xFF\xE0"
        b"\xEB\xC1\xFF\xE8"
        b"\xEB\xE1\xFF\xF0"
        b"\x60\x00\x00\x00"
        b"\x60\x00\x00\x00"
        b"\x60\x00\x00\x00"
        b"\x60\x00\x00\x00"
        b"\x60\x00\x00\x00"
        b"\x4E\x80\x04\x20"
        b"\x7F\xE0\x00\x08"
    )

    #
    # The offset in the payload conaining the address where arguments will be loaded from.
    # 16 bits for higher and lower (lis, ori)
    #
    ArgumentContextsHighOffset = 0x1A
    ArgumentContextsLowOffset  = 0x1E

    #
    # The offsets in the payload for setting the address to branch back to after the hook.
    # 16 bits for higher and lower (lis, ori)
    #
    BranchBackHighOffset       = 0x12A
    BranchBackLowOffset        = 0x12E

    #
    # The offset for storing instructions that need to be executed before branching back to the original.
    #
    OriginalInstructionsOffset = 0x140

    def SetPayloadData(Offset, Data):
        RPCPayload.PayloadData[Offset:Offset+len(Data)] = Data

    def SetArgumentContextsAddress(Address):
        RPCPayload.SetPayloadData(RPCPayload.ArgumentContextsHighOffset, PackInt16BE((Address >> 16) & 0xFFFF))
        RPCPayload.SetPayloadData(RPCPayload.ArgumentContextsLowOffset,  PackInt16BE(Address & 0xFFFF))

    def SetBranchBackAddress(Address):
        RPCPayload.SetPayloadData(RPCPayload.BranchBackHighOffset, PackInt16BE((Address >> 16) & 0xFFFF))
        RPCPayload.SetPayloadData(RPCPayload.BranchBackLowOffset,  PackInt16BE(Address & 0xFFFF))

    def SetOriginalInstructions(Instructions):
        RPCPayload.SetPayloadData(RPCPayload.OriginalInstructionsOffset, Instructions)

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
    GPRegisterArrayOffset = 0x00
    FPRegisterArrayOffset = 0x48
    CallAddressOffset     = 0x70
    ReturnGPOffset        = 0x78
    ReturnFPOffset        = 0x80

    def GetGPRegisterOffset(RegisterIndex):
        return RPCCallContext.GPRegisterArrayOffset + (0x8 * RegisterIndex)

    def GetFPRegisterOffset(RegisterIndex):
        return RPCCallContext.FPRegisterArrayOffset + (0x4 * RegisterIndex)

    def __init__(self, ArgsAddress, ArgDataAddress):
        self.ArgsAddress        = ArgsAddress
        self.ArgDataAddress     = ArgDataAddress
        self.ArgumentsBuffer    = bytearray([ 0x0 ] * 0x100)
        self.ArgumentsData      = bytearray()
        self.ArgumentIntIndex   = 0
        self.ArgumentFloatIndex = 0
    
    def SetCallAddress(self, Address):
        self.ArgumentsBuffer[RPCCallContext.CallAddressOffset:RPCCallContext.CallAddressOffset+4] = PackInt32BE(Address)

    def SetGPRegister(self, RegIndex, Value):
        RegOffset = RPCCallContext.GetGPRegisterOffset(RegIndex)
        self.ArgumentsBuffer[RegOffset:RegOffset+8] = PackInt64BE(Value)

    def AddGPRegister(self, Value):
        if self.ArgumentIntIndex > 9:
            raise Exception('Too many int args!')

        self.SetGPRegister(self.ArgumentIntIndex, Value)
        self.ArgumentIntIndex += 1

    def SetFPRegister(self, RegIndex, Value):
        RegOffset = RPCCallContext.GetFPRegisterOffset(RegIndex)
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

from pwn import *

class RPCFunction:
    def __init__(self, API, Address):
        self.address  = Address
        self.argtypes = None
        self.restype  = None
        self.API      = API

    def __call__(self, *Args):
        ArgCount    = len(Args)
        CallContext = RPCCallContext(RPC.FreeSpaceAddress, RPC.ArgDataSpaceAddress)

        if ArgCount != len(self.argtypes):
            raise Exception('Wrong number of args expected: ' + str(len(self.argtypes)))

        for i in range(0, ArgCount):
            ArgType  = self.argtypes[i]
            ArgValue = Args[i]
            
            # TODO: Support more complicated types, structures etc.
            if issubclass(self.argtypes[i], _SimpleCData):
                RPCCTypeBasicTypes[self.argtypes[i]](CallContext, ArgValue)
            #elif issubclass(self.argtypes[i], _Pointer):

        # Set the function address to call in the payload.
        CallContext.SetCallAddress(self.address)

        FinalArgumentData = CallContext.ArgumentsBuffer + CallContext.ArgumentsData

        print(hexdump(FinalArgumentData))

        # Write payload
        self.API.WriteMemory(RPC.FreeSpaceAddress, FinalArgumentData)

        # Wait for function to execute
        while self.API.ReadInt32(RPC.FreeSpaceAddress + 0x70) != 0:
            pass

        # TODO: Support complicated return types??
        if self.restype:           
            if self.restype == c_float:
                return self.API.ReadFloat(RPC.FreeSpaceAddress + 0x80)
            else:
                return self.API.ReadInt64(RPC.FreeSpaceAddress + 0x78)
        
        return None

class RPC:
    # Free space to write function arguments.
    FreeSpaceAddress    = 0x10051000
    # Extra space to write arguments that dont fit in a register ie. arrays, strings etc..
    ArgDataSpaceAddress = FreeSpaceAddress + 0x100

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

        # Set the address to read arguments from (registers)
        RPCPayload.SetArgumentContextsAddress(RPC.FreeSpaceAddress)

        # Set the address to jump back to after our RPC payload has ran.
        RPCPayload.SetBranchBackAddress(HookAddressAfterPatch)

        # Get original instructions
        self.OriginalInstructions = self.API.ReadMemory(HookAddress, len(HookPatch))

        RPCPayload.SetOriginalInstructions(self.OriginalInstructions)

        # Write payload at ELF header because retarded page prot
        self.API.WriteMemory(0x10000, RPCPayload.PayloadData)

        # Write branch for hook.
        self.API.WriteMemory(HookAddress, HookPatch)

    def Disable():
        self.API.WriteMemory(HookAddress, self.OriginalInstructions)