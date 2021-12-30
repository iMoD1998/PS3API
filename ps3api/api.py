from .tmapi import TMAPI
from .ccapi import CCAPI
from .rpc import RPCFunction, RPC
from .memutils import *

class PS3API:
    API_TMAPI = 0
    API_CCAPI = 1

    def __init__(self, API=API_TMAPI):
        if API == PS3API.API_TMAPI:
            self.API = TMAPI()
        else:
            self.API = CCAPI()

        self.ConnectTarget = self.API.ConnectTarget
        self.AttachProcess = self.API.AttachProcess
        self.ReadMemory = self.API.ReadMemory
        self.WriteMemory = self.API.WriteMemory

        self.ReadInt8 = ReadInt8(self.ReadMemory)
        self.ReadInt16 = ReadInt16(self.ReadMemory)
        self.ReadInt32 = ReadInt32(self.ReadMemory)
        self.ReadInt64 = ReadInt64(self.ReadMemory)
        self.ReadFloat = ReadFloat(self.ReadMemory)
        self.ReadDouble = ReadDouble(self.ReadMemory)
        self.ReadString = ReadString(self.ReadMemory)

        self.WriteInt8 = WriteInt8(self.WriteMemory)
        self.WriteInt16 = WriteInt16(self.WriteMemory)
        self.WriteInt32 = WriteInt32(self.WriteMemory)
        self.WriteInt64 = WriteInt64(self.WriteMemory)
        self.WriteFloat = WriteFloat(self.WriteMemory)
        self.WriteDouble = WriteDouble(self.WriteMemory)
        self.WriteString = WriteString(self.WriteMemory)

        self.RPC = RPC(self)