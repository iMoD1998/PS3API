import os
import pathlib
from ctypes import *

from .common import CEnum

class CCAPIError(CEnum):
    CCAPI_OK = (0)
    CCAPI_ERROR = (-1)

class CCAPIConsoleIdType(CEnum):
    IDPS = (0)
    PSID = (1)

class CCAPIShutdownMode(CEnum):
    SHUTDOWN = (0)
    SOFT_REBOOT = (1)
    HARD_REBOOT = (2)

class CCAPIBuzzerType(CEnum):
    CONTINIOUS = (0)
    SINGLE = (1)
    DOUBLE = (2)
    TRIPLE = (3)

class CCAPIColorLed(CEnum):
    GREEN = (0)
    RED = (1)

class CCAPIStatusLed(CEnum):
    OFF = (0)
    ON = (1)
    BLINK = (2)

class CCAPINotifyIcon(CEnum):
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

class CCAPIConsoleType(CEnum):
    UNK = (0)
    CEX = (1)
    DEX = (2)
    TOOL = (3)

class CCAPIConsoleId(Structure):
    _fields_ = [
        ("value", c_char * 16 )
    ]

class CCAPIProcessName(Structure):
    _fields_ = [
        ("value", c_char * 512 )
    ]

class CCAPIConsoleName(Structure):
    _fields_ = [
        ("value", c_char * 256 )
    ]

class CCAPIConsoleIp(Structure):
    _fields_ = [
        ("value", c_char * 256 )
    ]

class CCAPIExports:
    def __init__(self):
        #
        # TODO: might need to bundle in future
        #
        os.add_dll_directory(os.getcwd())
        os.add_dll_directory(os.path.join(os.getenv('APPDATA'), "ControlConsoleAPI"))

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
        self.CCAPISetBootConsoleIds = self.CCAPI_DLL.CCAPISetBootConsoleIds
        self.CCAPISetBootConsoleIds.argtypes = [ c_int32, c_int32, POINTER(CCAPIConsoleId) ]
        self.CCAPISetBootConsoleIds.restype = CCAPIError

        '''
        int CCAPISetConsoleIds(ConsoleIdType idType, const ConsoleId* id);

        Set the current console ID.
        '''
        self.CCAPISetConsoleIds = self.CCAPI_DLL.CCAPISetConsoleIds
        self.CCAPISetConsoleIds.argtypes = [ CCAPIConsoleIdType, POINTER(CCAPIConsoleId) ]
        self.CCAPISetConsoleIds.restype = CCAPIError

        '''
        int CCAPISetMemory(u32 pid, u64 address, u32 size, const void* data);

        Write memory.
        '''
        self.CCAPISetMemory = self.CCAPI_DLL.CCAPISetMemory
        self.CCAPISetMemory.argtypes = [ c_uint32, c_uint64, c_uint32, POINTER(c_char) ]
        self.CCAPISetMemory.restype = c_ulong

        '''
        int CCAPIGetMemory(u32 pid, u64 address, u32 size, void* data);

        Read memory.
        '''
        self.CCAPIGetMemory = self.CCAPI_DLL.CCAPIGetMemory
        self.CCAPIGetMemory.argtypes = [ c_uint32, c_uint64, c_uint32, POINTER(c_char) ]
        self.CCAPIGetMemory.restype = c_ulong

        '''
        int CCAPIGetProcessList(u32* npid, u32* pids);

        Get the list of processes.
        '''
        self.CCAPIGetProcessList = self.CCAPI_DLL.CCAPIGetProcessList
        self.CCAPIGetProcessList.argtypes = [ POINTER(c_uint32), POINTER(c_uint32) ]
        self.CCAPIGetProcessList.restype = c_ulong

        '''
        int CCAPIGetProcessName(u32 pid, ProcessName* name);

        Get the name of the current attached process.
        '''
        self.CCAPIGetProcessName = self.CCAPI_DLL.CCAPIGetProcessName
        self.CCAPIGetProcessName.argtypes = [ c_uint32, POINTER(CCAPIProcessName) ]
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
        void CCAPIGetConsoleInfo(int index, ConsoleName* name, ConsoleIp* ip);

        Get console name and ip.
        '''
        self.CCAPIGetConsoleInfo = self.CCAPI_DLL.CCAPIGetConsoleInfo
        self.CCAPIGetConsoleInfo.argtypes = [ c_uint32, POINTER(CCAPIConsoleName), POINTER(CCAPIConsoleIp) ]
        self.CCAPIGetConsoleInfo.restype = None

        '''
        int CCAPIGetDllVersion();

        Get version of the CCAPI.dll.
        '''
        self.CCAPIGetDllVersion = self.CCAPI_DLL.CCAPIGetDllVersion
        self.CCAPIGetDllVersion.argtypes = [ ]
        self.CCAPIGetDllVersion.restype = c_int32

class CCAPI:
    def __init__(self):
        self.NativeAPI      = CCAPIExports()
        self.PS3TargetIndex = -1
        self.IsConnected    = False
        self.ProcessID      = 0

    def GetNumberOfTargets(self):
        return self.NativeAPI.CCAPIGetNumberOfConsoles()

    def GetDefaultTarget(self):
        NumConsoles = self.GetNumberOfTargets()

        if NumConsoles == 0:
            return None

        return 0

    def GetConsoleInfo(self, TargetIndex):
        NamePtr = pointer(CCAPIConsoleName())
        IPPtr   = pointer(CCAPIConsoleIp())

        self.NativeAPI.CCAPIGetConsoleInfo(TargetIndex, NamePtr, IPPtr)

        Name = NamePtr.contents.value
        IP   = IPPtr.contents.value

        if Name == b"" or IP == b"":
            return (None, None)

        return (Name.decode("ascii"), IP.decode("ascii"))

    def ConnectTargetWithIP(self, TargetIP):
        if self.NativeAPI.CCAPIConnectConsole(bytes(TargetIP, "ascii")) == CCAPIError.CCAPI_OK:
            return True
        
        return False

    def ConnectTarget(self, TargetIndex=-1):
        NumConsoles = self.GetNumberOfTargets()

        if NumConsoles == 0:
            raise Exception("No Consoles Added In CCAPI")

        TargetIndex = self.GetDefaultTarget() if TargetIndex == -1 else TargetIndex

        if TargetIndex == None:
            raise Exception("Could not find default console")

        ConsoleName, IP = self.GetConsoleInfo(TargetIndex)

        if IP == None:
            raise Exception("Failed to find console info")

        print(IP)

        return self.ConnectTargetWithIP(IP)

    def GetProcessList(self):
        NumProcessPtr = pointer(c_uint32(0))

        if self.NativeAPI.CCAPIGetProcessList(NumProcessPtr, None) == CCAPIError.CCAPI_ERROR:
            raise Exception("CCAPIGetProcessList() Failed")

        print(NumProcessPtr.contents.value)

        ProccessIDList = (c_uint32 * NumProcessPtr.contents.value)()

        if self.NativeAPI.CCAPIGetProcessList(NumProcessPtr, ProccessIDList) == CCAPIError.CCAPI_ERROR:
            raise Exception("CCAPIGetProcessList() Failed")

        return list(ProccessIDList)

    def GetProcessName(self, ProcessID):
        ProcessNamePtr = pointer(CCAPIProcessName())

        if self.NativeAPI.CCAPIGetProcessName(ProcessID, ProcessNamePtr) == CCAPIError.CCAPI_OK:
            ProcessName = ProcessNamePtr.contents.value
            return ProcessName.decode("ascii")

        return None

    def AttachProcess(self, ProcessID=-1):
        if ProcessID == -1:
            ProcessList = self.GetProcessList()

            for Process in ProcessList:
                ProcessName = self.GetProcessName(Process)

                if "dev_flash" not in ProcessName:
                    ProcessID = Process
                    break
        
        if ProcessID == -1:
            raise Exception("Failed to find game process ID")

        self.ProcessID = ProcessID

    def ReadMemory(self, Address, Size):
        MemoryBuffer = (c_char * Size)()

        Error = self.NativeAPI.CCAPIGetMemory(self.ProcessID, Address, Size, MemoryBuffer)

        return bytes(MemoryBuffer)

    def WriteMemory(self, Address, Bytes):
        WriteBuffer = (c_char * len(Bytes)).from_buffer(bytearray(Bytes))

        Error = self.NativeAPI.CCAPISetMemory(self.ProcessID, Address, len(Bytes), WriteBuffer)
