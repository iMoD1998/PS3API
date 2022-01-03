import os
import pathlib
from ctypes import *
from ctypes import _SimpleCData
from ctypes import _Pointer

from .common import CEnum

class SNResult(CEnum):
    SN_S_OK = (0)
    SN_S_PENDING = (1)
    SN_S_NO_MSG = (3)
    SN_S_TM_VERSION = (4)
    SN_S_REPLACED = (5)
    SN_S_NO_ACTION = (6)
    SN_S_CONNECTED = SN_S_NO_ACTION
    SN_S_TARGET_STILL_REGISTERED = (7)
    SN_E_NOT_IMPL = (-1)
    SN_E_TM_NOT_RUNNING = (-2)
    SN_E_BAD_TARGET = (-3)
    SN_E_NOT_CONNECTED = (-4)
    SN_E_COMMS_ERR = (-5)
    SN_E_TM_COMMS_ERR = (-6)
    SN_E_TIMEOUT = (-7)
    SN_E_HOST_NOT_FOUND = (-8)
    SN_E_TARGET_IN_USE = (-9)
    SN_E_LOAD_ELF_FAILED = (-10)
    SN_E_BAD_UNIT = (-11)
    SN_E_OUT_OF_MEM = (-12)
    SN_E_NOT_LISTED = (-13)
    SN_E_TM_VERSION = (-14)
    SN_E_DLL_NOT_INITIALISED = (-15)
    SN_E_TARGET_RUNNING = (-17)
    SN_E_BAD_MEMSPACE = (-18)
    SN_E_NO_TARGETS = (-19)
    SN_E_NO_SEL = (-20)
    SN_E_BAD_PARAM = (-21)
    SN_E_BUSY = (-22)
    SN_E_DECI_ERROR = (-23)
    SN_E_INSUFFICIENT_DATA = (-25)
    SN_E_DATA_TOO_LONG = (-26)
    SN_E_DEPRECATED = (-27)
    SN_E_BAD_ALIGN = (-28)
    SN_E_FILE_ERROR = (-29)
    SN_E_NOT_SUPPORTED_IN_SDK_VERSION = (-30)
    SN_E_LOAD_MODULE_FAILED = (-31)
    SN_E_CHECK_TARGET_CONFIGURATION = (-33)
    SN_E_MODULE_NOT_FOUND = (-34)
    SN_E_CONNECT_TO_GAMEPORT_FAILED = (-35)
    SN_E_COMMAND_CANCELLED = (-36)
    SN_E_PROTOCOL_ALREADY_REGISTERED = (-37)
    SN_E_CONNECTED = (-38)
    SN_E_COMMS_EVENT_MISMATCHED_ERR = (-39)
    SN_E_TARGET_IS_POWERED_OFF = (-40)

class SNTargetInfoFlags(CEnum):
    SN_TI_TARGETID = (0x00000001)
    SN_TI_NAME = (0x00000002)
    SN_TI_INFO = (0x00000004)
    SN_TI_HOMEDIR = (0x00000008)
    SN_TI_FILESERVEDIR = (0x00000010)
    SN_TI_BOOT = (0x00000020)

class SNPS3TargetInfo(Structure):
    _fields_ = [
        ("nFlags", c_uint32 ),
        ("hTarget", c_uint32 ),
        ("pszName", c_char_p ),
        ("pszType", c_char_p ),
        ("pszInfo", c_char_p ),
        ("pszHomeDir", c_char_p ),
        ("pszFSDir", c_char_p ),
        ("boot", c_uint64 ),
    ]

class TMAPIExports:
    def __init__(self):
        os.add_dll_directory(os.getcwd())
        os.add_dll_directory(os.path.join(os.getenv('SN_PS3_PATH'), "bin"))
        self.TMAPI_DLL = CDLL("ps3tmapi.dll")

        '''
        SNAPI SNRESULT SNPS3InitTargetComms(void);

        Initialises target communications and launches Target Manager.
        '''
        self.SNPS3InitTargetComms = self.TMAPI_DLL.SNPS3InitTargetComms
        self.SNPS3InitTargetComms.argtypes = []
        self.SNPS3InitTargetComms.restype = SNResult

        '''
        SNAPI SNRESULT SNPS3CloseTargetComms(void);

        Shuts down internal communications (but does not close the Target Manager) and frees resources.
        '''
        self.SNPS3CloseTargetComms = self.TMAPI_DLL.SNPS3CloseTargetComms
        self.SNPS3CloseTargetComms.argtypes = []
        self.SNPS3CloseTargetComms.restype = SNResult

        '''
        SNAPI SNRESULT SNPS3IsScanning();

        Returns SN_E_BUSY if a search is already in progress.
        '''
        self.SNPS3IsScanning = self.TMAPI_DLL.SNPS3IsScanning
        self.SNPS3IsScanning.argtypes = []
        self.SNPS3IsScanning.restype = SNResult

        '''
        SNAPI SNRESULT SNPS3Connect(
            HTARGET hTarget,
            const char *pszApplication
        );

        Connect to specified target.
        '''
        self.SNPS3Connect = self.TMAPI_DLL.SNPS3Connect
        self.SNPS3Connect.argtypes = [ c_uint32, c_char_p ]
        self.SNPS3Connect.restype = SNResult

        '''
        SNAPI SNRESULT SNPS3ConnectEx(
            HTARGET hTarget,
            const char *pszApplication,
            BOOL bForceFlag
        );

        Connect to specified target.
        '''
        self.SNPS3ConnectEx = self.TMAPI_DLL.SNPS3ConnectEx
        self.SNPS3ConnectEx.argtypes = [ c_uint32, c_char_p, c_bool ]
        self.SNPS3ConnectEx.restype = SNResult

        '''
        SNAPI SNRESULT SNPS3GetTargetInfo(
            SNPS3TargetInfo *pTargetInfo
        );

        Retrieves information for a target specified by hTarget member of SNPS3TargetInfo() structure.
        '''
        self.SNPS3GetTargetInfo = self.TMAPI_DLL.SNPS3GetTargetInfo
        self.SNPS3GetTargetInfo.argtypes = [ POINTER(SNPS3TargetInfo) ]
        self.SNPS3GetTargetInfo.restype = SNResult

        '''
        SNAPI SNRESULT SNPS3GetDefaultTarget(
            HTARGET *pTarget
        );

        Gets the default target.
        '''
        self.SNPS3GetDefaultTarget = self.TMAPI_DLL.SNPS3GetDefaultTarget
        self.SNPS3GetDefaultTarget.argtypes = [ POINTER(c_uint32) ]
        self.SNPS3GetDefaultTarget.restype = SNResult

        '''
        SNAPI SNRESULT SNPS3SetDefaultTarget(
            HTARGET hTarget
        );

        Gets the default target.
        '''
        self.SNPS3SetDefaultTarget = self.TMAPI_DLL.SNPS3SetDefaultTarget
        self.SNPS3SetDefaultTarget.argtypes = [ c_uint32 ]
        self.SNPS3SetDefaultTarget.restype = SNResult

        '''
        SNAPI SNRESULT SNPS3ProcessList(
            HTARGET hTarget,
            UINT32 *puCount,
            UINT32 *puBuffer
        );

        Fetches a list of processes running on the specified target.
        '''
        self.SNPS3ProcessList = self.TMAPI_DLL.SNPS3ProcessList
        self.SNPS3ProcessList.argtypes = [ c_uint32, POINTER(c_uint32), POINTER(c_uint32) ]
        self.SNPS3ProcessList.restype = SNResult

        '''
        SNAPI SNRESULT SNPS3ProcessAttach(
            HTARGET hTarget,
            UINT32 uUnitID,
            UINT32 uProcessID
        );

        Attach to a process.
        '''
        self.SNPS3ProcessAttach = self.TMAPI_DLL.SNPS3ProcessAttach
        self.SNPS3ProcessAttach.argtypes = [ c_uint32, c_uint32, c_uint32 ]
        self.SNPS3ProcessAttach.restype = SNResult

        '''
        SNAPI SNRESULT SNPS3ProcessContinue(
            HTARGET hTarget,
            UINT32 uProcessID
        );

        Continues all threads from a specified process.
        '''
        self.SNPS3ProcessContinue = self.TMAPI_DLL.SNPS3ProcessContinue
        self.SNPS3ProcessContinue.argtypes = [ c_uint32, c_uint32 ]
        self.SNPS3ProcessContinue.restype = SNResult

        '''
        SNAPI SNRESULT SNPS3ProcessStop(
            HTARGET hTarget,
            UINT32 uProcessID
        );

        Stops all threads from a specified process.
        '''
        self.SNPS3ProcessStop = self.TMAPI_DLL.SNPS3ProcessStop
        self.SNPS3ProcessStop.argtypes = [ c_uint32, c_uint32 ]
        self.SNPS3ProcessStop.restype = SNResult

        '''
        SNAPI SNRESULT SNPS3ProcessGetMemory(
            HTARGET hTarget,
            UINT32 uUnit,
            UINT32 uProcessID,
            UINT64 uThreadID,
            UINT64 uAddress,
            int nCount,
            BYTE *pBuffer
        );
        '''
        self.SNPS3ProcessGetMemory = self.TMAPI_DLL.SNPS3ProcessGetMemory
        self.SNPS3ProcessGetMemory.argtypes = [ c_uint32, c_uint32, c_uint32, c_uint64, c_uint64, c_int32, POINTER(c_char)  ]
        self.SNPS3ProcessGetMemory.restype = SNResult

        '''
        SNAPI SNRESULT SNPS3ProcessSetMemory(
            HTARGET hTarget,
            UINT32 uUnit,
            UINT32 uProcessID,
            UINT64 uThreadID,
            UINT64 uAddress,
            int nCount,
            const BYTE *pBuffer
        );
        '''
        self.SNPS3ProcessSetMemory = self.TMAPI_DLL.SNPS3ProcessSetMemory
        self.SNPS3ProcessSetMemory.argtypes = [ c_uint32, c_uint32, c_uint32, c_uint64, c_uint64, c_int32, POINTER(c_char)  ]
        self.SNPS3ProcessSetMemory.restype = SNResult

class TMAPI:
    def __init__(self):
        self.NativeAPI = TMAPIExports()
        self.PS3TargetIndex = -1
        self.IsConnected = False

        if self.NativeAPI.SNPS3InitTargetComms() != SNResult.SN_S_OK:
            raise Exception("SNPS3InitTargetComms() Failed")

    def ThrowIfNotConnected(self):
        if self.IsConnected == False:
            raise Exception("Error: Not Connected to PS3")

    def GetDefaultTarget(self):
        DefaultTargetIndex = pointer(c_uint32(0))

        if self.NativeAPI.SNPS3GetDefaultTarget(DefaultTargetIndex) != SNResult.SN_S_OK:
            raise Exception("SNPS3InitTargetComms() Failed")

        return DefaultTargetIndex[0]

    def ConnectTarget(self, TargetIndex=-1):
        self.IsConnected = False

        if TargetIndex == -1:
            TargetIndex = self.GetDefaultTarget()

        if self.NativeAPI.SNPS3ConnectEx(TargetIndex, None, True) not in [ SNResult.SN_S_OK, SNResult.SN_S_CONNECTED ]:
            return False

        self.PS3TargetIndex = TargetIndex

        self.IsConnected = True

        return True

    def GetProcessList(self):
        self.ThrowIfNotConnected()

        NumProcessesPtr = pointer(c_uint32(0))

        if self.NativeAPI.SNPS3ProcessList(self.PS3TargetIndex, NumProcessesPtr, None) != SNResult.SN_S_OK:
            raise Exception("SNPS3ProcessList(): GetNumProcesses Failed")

        NumProcesses = NumProcessesPtr.contents.value

        if NumProcesses == 0:
            raise Exception("No process running")

        ProcessList = (c_uint32*NumProcesses)()

        if self.NativeAPI.SNPS3ProcessList(self.PS3TargetIndex, NumProcessesPtr, ProcessList) != SNResult.SN_S_OK:
            raise Exception("SNPS3ProcessList(): GetProcessInfos Failed")

        return list(ProcessList)

    def AttachProcess(self, ProcessID=-1):
        self.ThrowIfNotConnected()

        if ProcessID == -1:
            ProcessList = self.GetProcessList()

            if len(ProcessList) == 0:
                return False

            ProcessID = ProcessList[0]

        if self.NativeAPI.SNPS3ProcessAttach(self.PS3TargetIndex, 0, ProcessID) != SNResult.SN_S_OK:
            return False

        if self.NativeAPI.SNPS3ProcessContinue(self.PS3TargetIndex, ProcessID) != SNResult.SN_S_OK:     
            raise Exception("SNPS3ProcessContinue() Failed")

        self.ProcessID = ProcessID

        return True

    def ReadMemory(self, Address, Size):
        self.ThrowIfNotConnected()

        MemoryBuffer = (c_char * Size)()

        self.NativeAPI.SNPS3ProcessGetMemory(self.PS3TargetIndex, 0, self.ProcessID, 0, Address, Size, MemoryBuffer)
        
        return bytes(MemoryBuffer)

    def WriteMemory(self, Address, Bytes):
        self.ThrowIfNotConnected()

        WriteBuffer = (c_char * len(Bytes)).from_buffer(bytearray(Bytes))
        
        return self.NativeAPI.SNPS3ProcessSetMemory(self.PS3TargetIndex, 0, self.ProcessID, 0, Address, len(Bytes), WriteBuffer)