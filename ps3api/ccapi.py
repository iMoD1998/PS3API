import os
import pathlib
from ctypes import *

from .common import CEnum

class CCAPIError(CEnum):
    CCAPI_OK = (0)
    CCAPI_ERROR = (-1)

class ConsoleIdType(CEnum):
    IDPS = (0)
    PSID = (1)

class ShutdownMode(CEnum):
    SHUTDOWN = (0)
    SOFT_REBOOT = (1)
    HARD_REBOOT = (2)

class BuzzerType(CEnum):
    CONTINIOUS = (0)
    SINGLE = (1)
    DOUBLE = (2)
    TRIPLE = (3)

class ColorLed(CEnum):
    GREEN = (0)
    RED = (1)

class StatusLed(CEnum):
    OFF = (0)
    ON = (1)
    BLINK = (2)

class NotifyIcon(CEnum):
    NOTIFY_INFO = (0)
    NOTIFY_CAUTION = (1)
    NOTIFY_FRIEND = (2)
    NOTIFY_SLIDER = (3)
    NOTIFY_WRONGWAY = (4)
    NOTIFY_DIALOG = (5)
    NOTIFY_DIALOG_SHADOW = (6)
    NOTIFY_TEXT = (7)
    NOTIFY_POINTER = (8)
    NOTIFY_GRAB = (9)
    NOTIFY_HAND = (10)
    NOTIFY_PEN = (11)
    NOTIFY_FINGER = (12)
    NOTIFY_ARROW = (13)
    NOTIFY_ARROW_RIGHT = (14)
    NOTIFY_PROGRESS = (15)
    NOTIFY_TROPHY1 = (16)
    NOTIFY_TROPHY2 = (17)
    NOTIFY_TROPHY3 = (18)
    NOTIFY_TROPHY4 = (19)

class StatusLed(CEnum):
    UNK = (0)
    CEX = (1)
    DEX = (2)
    TOOL = (3)

class ConsoleId(Structure):
    _fields_ = [
        ("value", c_uint8 * 16 )
    ]

class ProcessName(Structure):
    _fields_ = [
        ("value", c_uint8 * 512 )
    ]

class ConsoleName(Structure):
    _fields_ = [
        ("value", c_uint8 * 256 )
    ]

class CCAPIExports:
    def __init__(self):
        os.add_dll_directory(os.getcwd())

        self.CCAPI_DLL = CDLL("CCAPI.dll")

        '''
        int CCAPIConnectConsole(const char* ip);

        Connects to console.
        '''
        self.CCAPIConnectConsole = self.CCAPI_DLL.CCAPIConnectConsole
        self.CCAPIConnectConsole.argtypes = [ c_char_p ]
        self.CCAPIConnectConsole.restype = CCAPIError

        '''
        int CCAPIDisconnectConsole();

        Disconnect from current console.
        '''
        self.CCAPIDisconnectConsole = self.CCAPI_DLL.CCAPIDisconnectConsole
        self.CCAPIDisconnectConsole.argtypes = [ ]
        self.CCAPIDisconnectConsole.restype = CCAPIError

        '''
        int CCAPIGetConnectionStatus(int* status);

        Get connection status of current console.
        '''
        self.CCAPIGetConnectionStatus = self.CCAPI_DLL.CCAPIGetConnectionStatus
        self.CCAPIGetConnectionStatus.argtypes = [ POINTER(c_int32) ]
        self.CCAPIGetConnectionStatus.restype = CCAPIError

        '''
        int CCAPISetBootConsoleIds(ConsoleIdType idType, int on, const ConsoleId* id);

        Set the console ID that will be used on boot.
        '''
        self.CCAPISetBootConsoleIds = CCAPI_DLL.CCAPISetBootConsoleIds
        self.CCAPISetBootConsoleIds.argtypes = [ c_int32, c_int32, POINTER(ConsoleId) ]
        self.CCAPISetBootConsoleIds.restype = CCAPIError

        '''
        int CCAPISetConsoleIds(ConsoleIdType idType, const ConsoleId* id);

        Set the current console ID.
        '''
        self.CCAPISetConsoleIds = self.CCAPI_DLL.CCAPISetConsoleIds
        self.CCAPISetConsoleIds.argtypes = [ c_int32, POINTER(ConsoleId) ]
        self.CCAPISetConsoleIds.restype = CCAPIError

        '''
        int CCAPISetMemory(u32 pid, u64 address, u32 size, const void* data);

        Write memory.
        '''
        self.CCAPISetMemory = self.CCAPI_DLL.CCAPISetMemory
        self.CCAPISetMemory.argtypes = [ c_uint32, c_uint64, c_uint32, POINTER(c_char) ]
        self.CCAPISetMemory.restype = CCAPIError

        '''
        int CCAPIGetMemory(u32 pid, u64 address, u32 size, void* data);

        Read memory.
        '''
        self.CCAPIGetMemory = self.CCAPI_DLL.CCAPIGetMemory
        self.CCAPIGetMemory.argtypes = [ c_uint32, c_uint64, c_uint32, POINTER(c_char) ]
        self.CCAPIGetMemory.restype = CCAPIError

        '''
        int CCAPIGetProcessList(u32* npid, u32* pids);

        Get the list of processes.
        '''
        self.CCAPIGetProcessList = self.CCAPI_DLL.CCAPIGetMemory
        self.CCAPIGetProcessList.argtypes = [ POINTER(c_uint32), POINTER(c_uint32) ]
        self.CCAPIGetProcessList.restype = CCAPIError

        '''
        int CCAPIGetProcessName(u32 pid, ProcessName* name);

        Get the name of the current attached process.
        '''
        self.CCAPIGetProcessName = self.CCAPI_DLL.CCAPIGetProcessName
        self.CCAPIGetProcessName.argtypes = [ c_uint32, POINTER(ProcessName) ]
        self.CCAPIGetProcessName.restype = CCAPIError

        '''
        int CCAPIGetTemperature(int* cell, int* rsx);

        Get connection status of current console.
        '''
        self.CCAPIGetTemperature = self.CCAPI_DLL.CCAPIGetTemperature
        self.CCAPIGetTemperature.argtypes = [ POINTER(c_int32), POINTER(c_int32) ]
        self.CCAPIGetTemperature.restype = CCAPIError

        '''
        int CCAPIGetTemperature(int* cell, int* rsx);

        Get connection status of current console.
        '''
        self.CCAPIGetTemperature = self.CCAPI_DLL.CCAPIGetTemperature
        self.CCAPIGetTemperature.argtypes = [ POINTER(c_int32), POINTER(c_int32) ]
        self.CCAPIGetTemperature.restype = CCAPIError

        '''
        int CCAPIShutdown(ShutdownMode mode);

        Shutdown console.
        '''
        self.CCAPIShutdown = self.CCAPI_DLL.CCAPIShutdown
        self.CCAPIShutdown.argtypes = [ c_int32 ]
        self.CCAPIShutdown.restype = CCAPIError

        '''
        int CCAPIRingBuzzer(BuzzerType type);

        Ring console's buzzer.
        '''
        self.CCAPIRingBuzzer = self.CCAPI_DLL.CCAPIRingBuzzer
        self.CCAPIRingBuzzer.argtypes = [ c_int32 ]
        self.CCAPIRingBuzzer.restype = CCAPIError

        '''
        int CCAPISetConsoleLed(ColorLed color, StatusLed status);

        Set console's LEDs.
        '''
        self.CCAPISetConsoleLed = self.CCAPI_DLL.CCAPISetConsoleLed
        self.CCAPISetConsoleLed.argtypes = [ c_int32, c_int32 ]
        self.CCAPISetConsoleLed.restype = CCAPIError

        '''
        int CCAPIGetFirmwareInfo(u32* firmware, u32* ccapi, ConsoleType* cType);

        Get infomation about the console.
        '''
        self.CCAPIGetFirmwareInfo = self.CCAPI_DLL.CCAPIGetFirmwareInfo
        self.CCAPIGetFirmwareInfo.argtypes = [ POINTER(c_uint32), POINTER(c_uint32), POINTER(c_int32) ]
        self.CCAPIGetFirmwareInfo.restype = CCAPIError

        '''
        int CCAPIVshNotify(NotifyIcon icon, const char* msg);

        Show a notification on the console.
        '''
        self.CCAPIVshNotify = self.CCAPI_DLL.CCAPIVshNotify
        self.CCAPIVshNotify.argtypes = [ c_int32, c_char_p ]
        self.CCAPIVshNotify.restype = CCAPIError

        '''
        int CCAPIGetNumberOfConsoles();

        Get the number of consoles added to CCAPI.
        '''
        self.CCAPIGetNumberOfConsoles = self.CCAPI_DLL.CCAPIGetNumberOfConsoles
        self.CCAPIGetNumberOfConsoles.argtypes = []
        self.CCAPIGetNumberOfConsoles.restype = c_int32

        '''
        int CCAPIGetConsoleInfo(int index, ConsoleName* name, ConsoleIp* ip);

        Get console name and ip.
        '''
        self.CCAPIGetConsoleInfo = self.CCAPI_DLL.CCAPIGetConsoleInfo
        self.CCAPIGetConsoleInfo.argtypes = [ c_uint32, POINTER(ConsoleName), POINTER(ConsoleIp) ]
        self.CCAPIGetConsoleInfo.restype = CCAPIError

        '''
        int CCAPIGetDllVersion();

        Get version of the CCAPI.dll.
        '''
        self.CCAPIGetDllVersion = self.CCAPI_DLL.CCAPIGetDllVersion
        self.CCAPIGetDllVersion.argtypes = [ ]
        self.CCAPIGetDllVersion.restype = c_int32

class CCAPI:
    def __init__(self):
        raise Exception("CCAPI Not Implemented!!")

    def GetDefaultTarget(self):
        raise Exception("CCAPI Not Implemented!!")

    def ConnectTarget(self, TargetIndex):
        raise Exception("CCAPI Not Implemented!!")

    def AttachProcess(self):
        raise Exception("CCAPI Not Implemented!!")

    def ReadMemory(self, Address, Size):
        raise Exception("CCAPI Not Implemented!!")

    def WriteMemory(self, Address, Bytes):
        raise Exception("CCAPI Not Implemented!!")