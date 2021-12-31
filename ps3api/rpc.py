from enum import IntEnum
from ctypes import *
from ctypes import _SimpleCData
from ctypes import _Pointer
from .memutils import *

class RPCPayload:
    #
    # RPC shelldcode/payload that will be used to call functions (See RPCPayload.s)
    #
    PayloadData = bytearray(
        b"\x7C\x08\x02\xA6"
        b"\xF8\x01\xFF\xF8"
        b"\xFB\x81\xFF\xD8"
        b"\xFB\xA1\xFF\xE0"
        b"\xFB\xC1\xFF\xE8"
        b"\xFB\xE1\xFF\xF0"
        b"\xF8\x21\xFD\xE1"
        b"\x3F\xE0\xCA\xFE"
        b"\x63\xFF\xBE\xEF"
        b"\xEB\xDF\x00\x70"
        b"\x2C\x1E\x00\x00"
        b"\x41\x82\x01\x48"
        b"\xD8\x21\x01\x08"
        b"\xD8\x41\x01\x10"
        b"\xD8\x61\x01\x18"
        b"\xD8\x81\x01\x20"
        b"\xD8\xA1\x01\x88"
        b"\xD8\xC1\x01\x90"
        b"\xD8\xE1\x01\x98"
        b"\xD9\x01\x01\xA0"
        b"\xD9\x21\x01\xA8"
        b"\xF8\x61\x01\xB0"
        b"\xF8\x81\x01\xB8"
        b"\xF8\xA1\x01\xC0"
        b"\xF8\xC1\x01\xC8"
        b"\xF8\xE1\x01\xD0"
        b"\xF9\x01\x01\xD8"
        b"\xF9\x21\x01\xE0"
        b"\xF9\x41\x01\xE8"
        b"\xF9\x61\x01\xF0"
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
        b"\x83\xBF\x00\x6C"
        b"\x2C\x1D\x00\x01"
        b"\x40\x82\x00\x0C"
        b"\x7C\x5C\x13\x78"
        b"\x48\x00\x00\x38"
        b"\x2C\x1D\x00\x02"
        b"\x40\x82\x00\x0C"
        b"\xEB\x9F\x00\x78"
        b"\x48\x00\x00\x28"
        b"\x2C\x1D\x00\x03"
        b"\x40\x82\x00\x10"
        b"\x83\x9E\x00\x04"
        b"\x83\xDE\x00\x00"
        b"\x48\x00\x00\x14"
        b"\x2C\x1D\x00\x04"
        b"\x40\x82\x00\x28"
        b"\x44\x00\x00\x02"
        b"\x48\x00\x00\x18"
        b"\xF8\x41\x01\x00"
        b"\x7F\x82\xE3\x78"
        b"\x7F\xC9\x03\xA6"
        b"\x4E\x80\x04\x21"
        b"\xE8\x41\x01\x00"
        b"\xF8\x7F\x00\x80"
        b"\xD0\x3F\x00\x88"
        b"\x7F\xDE\xF2\x78"
        b"\xFB\xDF\x00\x70"
        b"\xC8\x21\x01\x08"
        b"\xC8\x41\x01\x10"
        b"\xC8\x61\x01\x18"
        b"\xC8\x81\x01\x20"
        b"\xC8\xA1\x01\x88"
        b"\xC8\xC1\x01\x90"
        b"\xC8\xE1\x01\x98"
        b"\xC9\x01\x01\xA0"
        b"\xC9\x21\x01\xA8"
        b"\xE8\x61\x01\xB0"
        b"\xE8\x81\x01\xB8"
        b"\xE8\xA1\x01\xC0"
        b"\xE8\xC1\x01\xC8"
        b"\xE8\xE1\x01\xD0"
        b"\xE9\x01\x01\xD8"
        b"\xE9\x21\x01\xE0"
        b"\xE9\x41\x01\xE8"
        b"\xE9\x61\x01\xF0"
        b"\x38\x21\x02\x20"
        b"\xE8\x01\xFF\xF8"
        b"\x7C\x08\x03\xA6"
        b"\x3F\xE0\xDE\xAD"
        b"\x63\xFF\xC0\xDE"
        b"\x7F\xE9\x03\xA6"
        b"\xEB\x81\xFF\xD8"
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
    ArgumentContextsHighOffset = 0x1E
    ArgumentContextsLowOffset  = 0x22

    #
    # The offsets in the payload for setting the address to branch back to after the hook.
    # 16 bits for higher and lower (lis, ori)
    #
    BranchBackHighOffset       = 0x182
    BranchBackLowOffset        = 0x186

    #
    # The offset for storing instructions that need to be executed before branching back to the original.
    #
    OriginalInstructionsOffset = 0x19C

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
    #
    # Call context offsets and info (see RPCPayload.s)
    #
    NumberGPRegs = 9
    NumberFPRegs = 9

    GPRegisterArrayOffset = 0x00
    FPRegisterArrayOffset = GPRegisterArrayOffset + (8 * NumberGPRegs)
    CallTypeOffset        = FPRegisterArrayOffset + (4 * NumberFPRegs)
    CallAddressOffset     = CallTypeOffset + 4
    CallTOCOffset         = CallAddressOffset + 8
    ReturnGPOffset        = CallTOCOffset + 8
    ReturnFPOffset        = ReturnGPOffset + 8

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
    
    def SetCallType(self, Address):
        self.ArgumentsBuffer[RPCCallContext.CallTypeOffset:RPCCallContext.CallTypeOffset+4] = PackInt32BE(Address)

    def SetCallTOCAddress(self, Address):
        self.ArgumentsBuffer[RPCCallContext.CallTOCOffset:RPCCallContext.CallTOCOffset+8] = PackInt64BE(Address)
    
    def SetCallAddress(self, Address):
        self.ArgumentsBuffer[RPCCallContext.CallAddressOffset:RPCCallContext.CallAddressOffset+8] = PackInt64BE(Address)

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
    #
    # Call types see (RPCPayload.s)
    #
    CALL_TYPE_NONE               = 0x00
    CALL_TYPE_FUNCTION           = 0x01
    CALL_TYPE_FUNCTION_SET_TOC   = 0x02
    CALL_TYPE_FUNCTION_OPD_ENTRY = 0x03
    CALL_TYPE_SYS_CALL           = 0x04

    def __init__(self, API, Address, TOCAddress = 0, Type=CALL_TYPE_FUNCTION):
        self.Address     = Address
        self.TOCAddress  = TOCAddress
        self.ArgTypes    = None
        self.ReturnType  = None
        self.CallType    = Type
        self.API         = API

    def __call__(self, *Args):
        ArgCount    = len(Args)
        CallContext = RPCCallContext(RPC.FreeSpaceAddress, RPC.ArgDataSpaceAddress)

        if ArgCount != len(self.ArgTypes):
            raise Exception('Wrong number of args expected: ' + str(len(self.ArgTypes)))

        for i in range(0, ArgCount):
            ArgType  = self.ArgTypes[i]
            ArgValue = Args[i]
            
            #
            # TODO: Support more complicated types, structures etc.
            #
            if issubclass(self.ArgTypes[i], _SimpleCData):
                RPCCTypeBasicTypes[self.ArgTypes[i]](CallContext, ArgValue)
            #elif issubclass(self.argtypes[i], _Pointer):

        #
        # If we are doing a syscall set r11 to the syscall index.
        #
        if self.CallType == RPCFunction.CALL_TYPE_SYS_CALL:
            CallContext.SetCallAddress(0xDEADBEEF)
            CallContext.SetGPRegister(8, self.Address)
        else:
            CallContext.SetCallTOCAddress(self.TOCAddress)
            CallContext.SetCallAddress(self.Address)

        CallContext.SetCallType(self.CallType)

        FinalArgumentData = CallContext.ArgumentsBuffer + CallContext.ArgumentsData

        print(hexdump(FinalArgumentData))

        #
        # Write call context.
        #
        self.API.WriteMemory(RPC.FreeSpaceAddress, FinalArgumentData)

        #
        # Wait for function to execute.
        #
        while self.API.ReadInt32(RPC.FreeSpaceAddress + RPCCallContext.CallAddressOffset) != 0:
            pass

        #
        # TODO: Support complicated return types??
        #
        if self.ReturnType:           
            if self.ReturnType == c_float:
                return self.API.ReadFloat(RPC.FreeSpaceAddress + RPCCallContext.ReturnFPOffset)
            else:
                return self.API.ReadInt64(RPC.FreeSpaceAddress + RPCCallContext.ReturnGPOffset)
        
        return None

class RPC:
    #
    # Free space to write function arguments.
    #
    FreeSpaceAddress    = 0x10051000

    #
    # Extra space to write arguments that dont fit in a register ie. arrays, strings etc..
    #
    ArgDataSpaceAddress = FreeSpaceAddress + 0x100

    def __init__(self, API):
        self.API = API
        self.Function = lambda Address: RPCFunction(API, Address)
        self.OriginalInstructions = bytearray()
    
    def Enable(self, HookAddress):
        #
        # bla 0x10000
        #
        HookPatch             = b'\x48\x01\x00\x02'
        HookAddressAfterPatch = HookAddress + len(HookPatch)

        #
        # Check if we are already hooked.
        #
        if self.API.ReadMemory(HookAddress, 4) == HookPatch:
            return

        # Set the address to read arguments from (registers)
        RPCPayload.SetArgumentContextsAddress(RPC.FreeSpaceAddress)

        #
        # Set the address to jump back to after our RPC payload has ran.
        #
        RPCPayload.SetBranchBackAddress(HookAddressAfterPatch)

        #
        # Get original instructions
        #
        self.OriginalInstructions = self.API.ReadMemory(HookAddress, len(HookPatch))

        RPCPayload.SetOriginalInstructions(self.OriginalInstructions)

        #
        # Write payload at ELF header because retarded page prot
        #
        self.API.WriteMemory(0x10000, RPCPayload.PayloadData)

        #
        # Write branch for hook.
        #
        self.API.WriteMemory(HookAddress, HookPatch)

    def Disable():
        self.API.WriteMemory(HookAddress, self.OriginalInstructions)