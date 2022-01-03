from ctypes import *
from .common import *
from enum import IntEnum

class SyscallIndex(IntEnum):
    SYS_PROCESS_GETPID = 1
    SYS_PROCESS_WAIT_FOR_CHILD = 2
    SYS_PROCESS_EXIT = 3
    SYS_PROCESS_GET_STATUS = 4
    SYS_PROCESS_DETACH_CHILD = 5
    SYS_PROCESS_GET_NUMBER_OF_OBJECT = 12
    SYS_PROCESS_GET_ID = 13
    SYS_PROCESS_IS_SPU_LOCK_LINE_RESERVATION_ADDRESS = 14
    SYS_PROCESS_GETPPID = 18
    SYS_PROCESS_KILL = 19
    SYS_PROCESS_WAIT_FOR_CHILD2 = 23
    SYS_PROCESS_GET_SDK_VERSION = 25
    SYS_PROCESS_GET_PPU_GUID = 31
    SYS_PPU_THREAD_EXIT = 41
    SYS_PPU_THREAD_YIELD = 43
    SYS_PPU_THREAD_JOIN = 44
    SYS_PPU_THREAD_DETACH = 45
    SYS_PPU_THREAD_GET_JOIN_STATE = 46
    SYS_PPU_THREAD_SET_PRIORITY = 47
    SYS_PPU_THREAD_GET_PRIORITY = 48
    SYS_PPU_THREAD_GET_STACK_INFORMATION = 49
    SYS_PPU_THREAD_STOP = 50
    SYS_PPU_THREAD_RESTART = 51
    SYS_PPU_THREAD_CREATE = 52
    SYS_PPU_THREAD_START = 53
    SYS_PPU_THREAD_RENAME = 56
    SYS_PPU_THREAD_RECOVER_PAGE_FAULT = 57
    SYS_PPU_THREAD_GET_PAGE_FAULT_CONTEXT = 58
    SYS_TRACE_CREATE = 60
    SYS_TRACE_START = 61
    SYS_TRACE_STOP = 62
    SYS_TRACE_UPDATE_TOP_INDEX = 63
    SYS_TRACE_DESTROY = 64
    SYS_TRACE_DRAIN = 65
    SYS_TRACE_ATTACH_PROCESS = 66
    SYS_TRACE_ALLOCATE_BUFFER = 67
    SYS_TRACE_FREE_BUFFER = 68
    SYS_TRACE_CREATE2 = 69
    SYS_TIMER_CREATE = 70
    SYS_TIMER_DESTROY = 71
    SYS_TIMER_GET_INFORMATION = 72
    _SYS_TIMER_START = 73
    SYS_TIMER_STOP = 74
    SYS_TIMER_CONNECT_EVENT_QUEUE = 75
    SYS_TIMER_DISCONNECT_EVENT_QUEUE = 76
    SYS_TRACE_CREATE2_IN_CBEPM = 77
    SYS_INTERRUPT_TAG_CREATE = 80
    SYS_INTERRUPT_TAG_DESTROY = 81
    SYS_EVENT_FLAG_CREATE = 82
    SYS_EVENT_FLAG_DESTROY = 83
    _SYS_INTERRUPT_THREAD_ESTABLISH = 84
    SYS_EVENT_FLAG_WAIT = 85
    SYS_EVENT_FLAG_TRYWAIT = 86
    SYS_EVENT_FLAG_SET = 87
    SYS_INTERRUPT_THREAD_EOI = 88
    _SYS_INTERRUPT_THREAD_DISESTABLISH = 89
    SYS_SEMAPHORE_CREATE = 90
    SYS_SEMAPHORE_DESTROY = 91
    SYS_SEMAPHORE_WAIT = 92
    SYS_SEMAPHORE_TRYWAIT = 93
    SYS_SEMAPHORE_POST = 94
    SYS_MUTEX_CREATE = 100
    SYS_MUTEX_DESTROY = 101
    SYS_MUTEX_LOCK = 102
    SYS_MUTEX_TRYLOCK = 103
    SYS_MUTEX_UNLOCK = 104
    SYS_COND_CREATE = 105
    SYS_COND_DESTROY = 106
    SYS_COND_WAIT = 107
    SYS_COND_SIGNAL = 108
    SYS_COND_SIGNAL_ALL = 109
    SYS_COND_SIGNAL_TO = 110
    SYS_SEMAPHORE_GET_VALUE = 114
    SYS_EVENT_FLAG_CLEAR = 118
    SYS_RWLOCK_CREATE = 120
    SYS_RWLOCK_DESTROY = 121
    SYS_RWLOCK_RLOCK = 122
    SYS_RWLOCK_TRYRLOCK = 123
    SYS_RWLOCK_RUNLOCK = 124
    SYS_RWLOCK_WLOCK = 125
    SYS_RWLOCK_WUNLOCK = 127
    SYS_EVENT_QUEUE_CREATE = 128
    SYS_EVENT_QUEUE_DESTROY = 129
    SYS_EVENT_QUEUE_RECEIVE = 130
    SYS_EVENT_QUEUE_TRYRECEIVE = 131
    SYS_EVENT_FLAG_CANCEL = 132
    SYS_EVENT_QUEUE_DRAIN = 133
    SYS_EVENT_PORT_CREATE = 134
    SYS_EVENT_PORT_DESTROY = 135
    SYS_EVENT_PORT_CONNECT_LOCAL = 136
    SYS_EVENT_PORT_DISCONNECT = 137
    SYS_EVENT_PORT_SEND = 138
    SYS_EVENT_FLAG_GET = 139
    SYS_EVENT_PORT_CONNECT_IPC = 140
    SYS_TIMER_USLEEP = 141
    SYS_TIMER_SLEEP = 142
    SYS_TIME_GET_CURRENT_TIME = 145
    SYS_TIME_GET_TIMEBASE_FREQUENCY = 147
    SYS_RWLOCK_TRYWLOCK = 148
    SYS_RAW_SPU_CREATE_INTERRUPT_TAG = 150
    SYS_RAW_SPU_SET_INT_MASK = 151
    SYS_RAW_SPU_GET_INT_MASK = 152
    SYS_RAW_SPU_SET_INT_STAT = 153
    SYS_RAW_SPU_GET_INT_STAT = 154
    SYS_SPU_IMAGE_OPEN = 156
    SYS_RAW_SPU_CREATE = 160
    SYS_RAW_SPU_DESTROY = 161
    SYS_RAW_SPU_READ_PUINT_MB = 163
    SYS_SPU_THREAD_GET_EXIT_STATUS = 165
    SYS_SPU_THREAD_SET_ARGUMENT = 166
    SYS_SPU_THREAD_GROUP_START_ON_EXIT = 167
    SYS_SPU_INITIALIZE = 169
    SYS_SPU_THREAD_GROUP_CREATE = 170
    SYS_SPU_THREAD_GROUP_DESTROY = 171
    SYS_SPU_THREAD_INITIALIZE = 172
    SYS_SPU_THREAD_GROUP_START = 173
    SYS_SPU_THREAD_GROUP_SUSPEND = 174
    SYS_SPU_THREAD_GROUP_RESUME = 175
    SYS_SPU_THREAD_GROUP_YIELD = 176
    SYS_SPU_THREAD_GROUP_TERMINATE = 177
    SYS_SPU_THREAD_GROUP_JOIN = 178
    SYS_SPU_THREAD_GROUP_SET_PRIORITY = 179
    SYS_SPU_THREAD_GROUP_GET_PRIORITY = 180
    SYS_SPU_THREAD_WRITE_LS = 181
    SYS_SPU_THREAD_READ_LS = 182
    SYS_SPU_THREAD_WRITE_SNR = 184
    SYS_SPU_THREAD_GROUP_CONNECT_EVENT = 185
    SYS_SPU_THREAD_GROUP_DISCONNECT_EVENT = 186
    SYS_SPU_THREAD_SET_SPU_CFG = 187
    SYS_SPU_THREAD_GET_SPU_CFG = 188
    SYS_SPU_THREAD_WRITE_SPU_MB = 190
    SYS_SPU_THREAD_CONNECT_EVENT = 191
    SYS_SPU_THREAD_DISCONNECT_EVENT = 192
    SYS_SPU_THREAD_BIND_QUEUE = 193
    SYS_SPU_THREAD_UNBIND_QUEUE = 194
    SYS_RAW_SPU_SET_SPU_CFG = 196
    SYS_RAW_SPU_GET_SPU_CFG = 197
    SYS_SPU_THREAD_RECOVER_PAGE_FAULT = 198
    SYS_RAW_SPU_RECOVER_PAGE_FAULT = 199
    SYS_SPU_THREAD_GROUP_SET_COOPERATIVE_VICTIMS = 250
    SYS_SPU_THREAD_GROUP_CONNECT_EVENT_ALL_THREADS = 251
    SYS_SPU_THREAD_GROUP_DISCONNECT_EVENT_ALL_THREADS = 252
    SYS_SPU_THREAD_GROUP_LOG = 254
    SYS_SPU_IMAGE_OPEN_BY_FD = 260
    SYS_VM_MEMORY_MAP = 300
    SYS_VM_UNMAP = 301
    SYS_VM_APPEND_MEMORY = 302
    SYS_VM_RETURN_MEMORY = 303
    SYS_VM_LOCK = 304
    SYS_VM_UNLOCK = 305
    SYS_VM_TOUCH = 306
    SYS_VM_FLUSH = 307
    SYS_VM_INVALIDATE = 308
    SYS_VM_STORE = 309
    SYS_VM_SYNC = 310
    SYS_VM_TEST = 311
    SYS_VM_GET_STATISTICS = 312
    SYS_MEMORY_CONTAINER_CREATE = 324
    SYS_MEMORY_CONTAINER_DESTROY = 325
    SYS_MMAPPER_ALLOCATE_FIXED_ADDRESS = 326
    SYS_MMAPPER_ENABLE_PAGE_FAULT_NOTIFICATION = 327
    SYS_MMAPPER_ALLOCATE_ADDRESS = 330
    SYS_MMAPPER_FREE_ADDRESS = 331
    SYS_MMAPPER_CHANGE_ADDRESS_ACCESS_RIGHT = 336
    SYS_MMAPPER_SEARCH_AND_MAP = 337
    SYS_MEMORY_CONTAINER_GET_SIZE = 343
    SYS_MEMORY_ALLOCATE = 348
    SYS_MEMORY_FREE = 349
    SYS_MEMORY_ALLOCATE_FROM_CONTAINER = 350
    SYS_MEMORY_GET_PAGE_ATTRIBUTE = 351
    SYS_MEMORY_GET_USER_MEMORY_SIZE = 352
    SYS_CONSOLE_WRITE = 398
    SYS_TTY_READ = 402
    SYS_TTY_WRITE = 403
    SYS_OVERLAY_LOAD_MODULE = 450
    SYS_OVERLAY_UNLOAD_MODULE = 451
    SYS_OVERLAY_GET_MODULE_LIST = 452
    SYS_OVERLAY_GET_MODULE_INFO = 453
    SYS_OVERLAY_LOAD_MODULE_BY_FD = 454
    SYS_OVERLAY_GET_MODULE_INFO2 = 455
    SYS_OVERLAY_GET_SDK_VERSION = 456
    _SYS_PRX_GET_MODULE_ID_BY_ADDRESS = 461
    _SYS_PRX_LOAD_MODULE_BY_FD = 463
    _SYS_PRX_LOAD_MODULE_ON_MEMCONTAINER_BY_FD = 464
    _SYS_PRX_LOAD_MODULE_LIST = 465
    _SYS_PRX_LOAD_MODULE_LIST_ON_MEMCONTAINER = 466
    SYS_PRX_GET_PPU_GUID = 467
    _SYS_PRX_LOAD_MODULE = 480
    _SYS_PRX_START_MODULE = 481
    _SYS_PRX_STOP_MODULE = 482
    _SYS_PRX_UNLOAD_MODULE = 483
    _SYS_PRX_REGISTER_MODULE = 484
    _SYS_PRX_QUERY_MODULE = 485
    _SYS_PRX_REGISTER_LIBRARY = 486
    _SYS_PRX_UNREGISTER_LIBRARY = 487
    _SYS_PRX_LINK_LIBRARY = 488
    _SYS_PRX_UNLINK_LIBRARY = 489
    _SYS_PRX_QUERY_LIBRARY = 490
    _SYS_PRX_GET_MODULE_LIST = 494
    _SYS_PRX_GET_MODULE_INFO = 495
    _SYS_PRX_GET_MODULE_ID_BY_NAME = 496
    _SYS_PRX_LOAD_MODULE_ON_MEMCONTAINER = 497
    _SYS_PRX_START = 498
    _SYS_PRX_STOP = 499
    SYS_STORAGE_OPEN = 600
    SYS_STORAGE_CLOSE = 601
    SYS_STORAGE_READ = 602
    SYS_STORAGE_WRITE = 603
    SYS_STORAGE_SEND_DEVICE_COMMAND = 604
    SYS_STORAGE_ASYNC_CONFIGURE = 605
    SYS_STORAGE_ASYNC_READ = 606
    SYS_STORAGE_ASYNC_WRITE = 607
    SYS_STORAGE_ASYNC_CANCEL = 608
    SYS_STORAGE_GET_DEVICE_INFO = 609
    SYS_STORAGE_GET_DEVICE_CONFIG = 610
    SYS_STORAGE_REPORT_DEVICES = 611
    SYS_STORAGE_CONFIGURE_MEDIUM_EVENT = 612
    SYS_STORAGE_SET_MEDIUM_POLLING_INTERVAL = 613
    SYS_STORAGE_CREATE_REGION = 614
    SYS_STORAGE_DELETE_REGION = 615
    SYS_STORAGE_EXECUTE_DEVICE_COMMAND = 616
    SYS_STORAGE_GET_REGION_ACL = 617
    SYS_STORAGE_SET_REGION_ACL = 618
    SYS_STORAGE_ASYNC_SEND_DEVICE_COMMAND = 619
    SYS_STORAGE_GET_REGION_OFFSET = 622
    SYS_STORAGE_SET_EMULATED_SPEED = 623
    SYS_IO_BUFFER_CREATE = 624
    SYS_IO_BUFFER_DESTROY = 625
    SYS_IO_BUFFER_ALLOCATE = 626
    SYS_IO_BUFFER_FREE = 627
    SYS_GPIO_SET = 630
    SYS_GPIO_GET = 631
    SYS_FSW_CONNECT_EVENT = 633
    SYS_FSW_DISCONNECT_EVENT = 634
    SYS_RSX_DEVICE_OPEN = 666
    SYS_RSX_DEVICE_CLOSE = 667
    SYS_RSX_MEMORY_ALLOCATE = 668
    SYS_RSX_MEMORY_FREE = 669
    SYS_RSX_CONTEXT_ALLOCATE = 670
    SYS_RSX_CONTEXT_FREE = 671
    SYS_RSX_CONTEXT_IOMAP = 672
    SYS_RSX_CONTEXT_IOUNMAP = 673
    SYS_RSX_CONTEXT_ATTRIBUTE = 674
    SYS_RSX_DEVICE_MAP = 675
    SYS_RSX_DEVICE_UNMAP = 676
    SYS_RSX_ATTRIBUTE = 677
    SYS_BDEMU_SEND_COMMAND = 699
    SYS_SS_GET_OPEN_PSID = 872
    SYS_DECI3_OPEN = 880
    SYS_DECI3_CREATE_EVENT_PATH = 881
    SYS_DECI3_CLOSE = 882
    SYS_DECI3_SEND = 883
    SYS_DECI3_RECEIVE = 884
    MAX_NUM_OF_SYSTEM_CALLS = 1024

#
# https://github.com/RPCS3/rpcs3/blob/master/rpcs3/Emu/Cell/lv2/sys_prx.h
#
class CellPrxError(CEnum):
	CELL_PRX_ERROR_ERROR                       = 0x80011001 # Error state
	CELL_PRX_ERROR_ILLEGAL_PERM                = 0x800110d1 # No permission to execute API
	CELL_PRX_ERROR_UNKNOWN_MODULE              = 0x8001112e # Specified PRX could not be found
	CELL_PRX_ERROR_ALREADY_STARTED             = 0x80011133 # Specified PRX is already started
	CELL_PRX_ERROR_NOT_STARTED                 = 0x80011134 # Specified PRX is not started
	CELL_PRX_ERROR_ALREADY_STOPPED             = 0x80011135 # Specified PRX is already stopped
	CELL_PRX_ERROR_CAN_NOT_STOP                = 0x80011136 # Specified PRX must not be stopped
	CELL_PRX_ERROR_NOT_REMOVABLE               = 0x80011138 # Specified PRX must not be deleted
	CELL_PRX_ERROR_LIBRARY_NOT_YET_LINKED      = 0x8001113a # Called unlinked function
	CELL_PRX_ERROR_LIBRARY_FOUND               = 0x8001113b # Specified library is already registered
	CELL_PRX_ERROR_LIBRARY_NOTFOUND            = 0x8001113c # Specified library is not registered
	CELL_PRX_ERROR_ILLEGAL_LIBRARY             = 0x8001113d # Library structure is invalid
	CELL_PRX_ERROR_LIBRARY_INUSE               = 0x8001113e # Library cannot be deleted because it is linked
	CELL_PRX_ERROR_ALREADY_STOPPING            = 0x8001113f # Specified PRX is in the process of stopping
	CELL_PRX_ERROR_UNSUPPORTED_PRX_TYPE        = 0x80011148 # Specified PRX format is invalid and cannot be loaded
	CELL_PRX_ERROR_INVAL                       = 0x80011324 # Argument value is invalid
	CELL_PRX_ERROR_ILLEGAL_PROCESS             = 0x80011801 # Specified process does not exist
	CELL_PRX_ERROR_NO_LIBLV2                   = 0x80011881 # liblv2.sprx does not exist
	CELL_PRX_ERROR_UNSUPPORTED_ELF_TYPE        = 0x80011901 # ELF type of specified file is not supported
	CELL_PRX_ERROR_UNSUPPORTED_ELF_CLASS       = 0x80011902 # ELF class of specified file is not supported
	CELL_PRX_ERROR_UNDEFINED_SYMBOL            = 0x80011904 # References undefined symbols
	CELL_PRX_ERROR_UNSUPPORTED_RELOCATION_TYPE = 0x80011905 # Uses unsupported relocation type
	CELL_PRX_ERROR_ELF_IS_REGISTERED           = 0x80011910 # Fixed ELF is already registered
	CELL_PRX_ERROR_NO_EXIT_ENTRY               = 0x80011911

class CellLv2ErrorCodes(CEnum):
    CELL_OK      = 0 # Success
    EAGAIN       = 0x80010001 # The resource is temporarily unavailable
    EINVAL       = 0x80010002 # An invalid argument or flag
    ENOSYS       = 0x80010003 # The feature is not yet implemented
    ENOMEM       = 0x80010004 # Memory allocation failure
    ESRCH        = 0x80010005 # The resource is not found
    ENOENT       = 0x80010006 # The file does not exist
    ENOEXEC      = 0x80010007 # The file is not a valid ELF file
    EDEADLK      = 0x80010008 # Resource deadlock is avoided
    EPERM        = 0x80010009 # The operation is not permitted
    EBUSY        = 0x8001000a # The device or resource is busy
    ETIMEDOUT    = 0x8001000b # The operation is timed out
    EABORT       = 0x8001000c # The operation is aborted
    EFAULT       = 0x8001000d # Invalid memory access
    ESTAT        = 0x8001000f # State of the target thread is invalid
    EALIGN       = 0x80010010 # Alignment is invalid
    EKRESOURCE   = 0x80010011 # Shortage of the kernel resource
    EISDIR       = 0x80010012 # The file is a directory
    ECANCELED    = 0x80010013 # Operation canceled
    EEXIST       = 0x80010014 # Entry already exists
    EISCONN      = 0x80010015 # Already connected
    ENOTCONN     = 0x80010016 # Not connected
    EAUTHFAIL    = 0x80010017 # Failure in authorizing SELF
    ENOTMSELF    = 0x80010018 # The file is not MSELF
    ESYSVER      = 0x80010019 # System version error
    EAUTHFATAL   = 0x8001001A # Fatal system error occurred while authorizing SELF
    EDOM         = 0x8001001B
    ERANGE       = 0x8001001C
    EILSEQ       = 0x8001001D
    EFPOS        = 0x8001001E
    EINTR        = 0x8001001F
    EFBIG        = 0x80010020
    EMLINK       = 0x80010021
    ENFILE       = 0x80010022
    ENOSPC       = 0x80010023
    ENOTTY       = 0x80010024
    EPIPE        = 0x80010025
    EROFS        = 0x80010026
    ESPIPE       = 0x80010027
    E2BIG        = 0x80010028
    EACCES       = 0x80010029
    EBADF        = 0x8001002A # The file descriptor is invalid
    EIO          = 0x8001002B # I/O error
    EMFILE       = 0x8001002C # The number of files which can be opened is exceeding the limit
    ENOTDIR      = 0x8001002E # The directory name is invalid
    ENXIO        = 0x8001002F
    EXDEV        = 0x80010030
    EBADMSG      = 0x80010031
    EINPROGRESS  = 0x80010032
    EMSGSIZE     = 0x80010033
    ENAMETOOLONG = 0x80010034 # The length of the name is exceeding the limit
    ENOLCK       = 0x80010035
    ENOTEMPTY    = 0x80010036
    ENOTSUP      = 0x80010037
    EFSSPECIFIC  = 0x80010038 # Error specific to the file system
    EOVERFLOW    = 0x80010039
    ENOTMOUNTED  = 0x8001003A # The file system is not mounted 
    ENOTSDATA    = 0x8001003B
    ESDKVER      = 0x8001003C
    ENOLICDISC   = 0x8001003D
    ENOLICENT    = 0x8001003E

class sys_prx_load_module_option_t(BigEndianStructure):
    _fields_ = [ 
        ("size", c_uint64),
        ("base", c_uint32)
    ]

class sys_prx_start_module_option_t(BigEndianStructure):
    _fields_ = [ 
        ("size", c_uint64)
    ]

class sys_prx_stop_module_option_t(BigEndianStructure):
    _fields_ = [ 
        ("size", c_uint64)
    ]

class SystemCallDefinitions:
    def __init__(self, RPC):
        """
        sys_pid_t sys_process_getpid(
            void
        );

        Get the process id
        """
        self.sys_process_getpid = RPC.SystemCall(SyscallIndex.SYS_PROCESS_GETPID)
        self.sys_process_getpid.ReturnType = c_uint32

        """ 
        int sys_process_wait_for_child(
            sys_pid_t pid,
            uint32_t *status,
            uint32_t unknown
        );
        """
        self.sys_process_wait_for_child = RPC.SystemCall(SyscallIndex.SYS_PROCESS_WAIT_FOR_CHILD)
        self.sys_process_wait_for_child.ArgTypes = [ c_uint32, POINTER(c_uint32), c_uint32 ]
        self.sys_process_wait_for_child.ReturnType = c_uint32

        """
        void sys_process_exit(
            int status
        );

        Terminate a process
        """
        self.sys_process_exit = RPC.SystemCall(SyscallIndex.SYS_PROCESS_EXIT)
        self.sys_process_exit.ArgTypes = [ c_uint32 ]
        self.sys_process_exit.ReturnType = c_uint32

        """
        int sys_process_get_status(
            sys_pid_t pid
        )

        Get process status
        """
        self.sys_process_get_status = RPC.SystemCall(SyscallIndex.SYS_PROCESS_GET_STATUS)
        self.sys_process_get_status.ArgTypes = [ c_uint32 ]
        self.sys_process_get_status.ReturnType = c_uint32

        """
        int sys_process_get_number_of_object(
            uint32_t object,
            size_t *nump
        );

        Obtain the total number of specified objects
        """
        self.sys_process_get_number_of_object = RPC.SystemCall(SyscallIndex.SYS_PROCESS_GET_NUMBER_OF_OBJECT)
        self.sys_process_get_number_of_object.ArgTypes = [ c_uint32, POINTER(c_uint32) ]
        self.sys_process_get_number_of_object.ReturnType = c_int32

        """
        int sys_process_get_id(
            uint32_t object,
            uint32_t *buff,
            size_t size,
            size_t *set_size
        );

        Obtain ID of specified object
        """
        self.sys_process_get_id = RPC.SystemCall(SyscallIndex.SYS_PROCESS_GET_ID)
        self.sys_process_get_id.ArgTypes = [ c_uint32, POINTER(c_uint32), c_uint32, POINTER(c_uint32) ]
        self.sys_process_get_id.ReturnType = c_int32

        """
        sys_pid_t sys_process_getppid(
            void
        );

        Get the parent process id
        """
        self.sys_process_getppid = RPC.SystemCall(SyscallIndex.SYS_PROCESS_GETPPID)
        self.sys_process_getppid.ArgTypes = [ ]
        self.sys_process_getppid.ReturnType = c_uint32

        """
        int sys_process_kill(
            sys_pid_t pid
        )

        Get process status
        """
        self.sys_process_kill = RPC.SystemCall(SyscallIndex.SYS_PROCESS_KILL)
        self.sys_process_kill.ArgTypes = [ c_uint32 ]
        self.sys_process_kill.ReturnType = c_int32

        """
        int sys_process_get_sdk_version(
            sys_pid_t pid,
            uint32_t* sdk_version
        )

        Gets a process SDK version. Needs root permission if pid is not the current process.
        """
        self.sys_process_get_sdk_version = RPC.SystemCall(SyscallIndex.SYS_PROCESS_GET_SDK_VERSION)
        self.sys_process_get_sdk_version.ArgTypes = [ c_uint32, POINTER(c_uint32) ]
        self.sys_process_get_sdk_version.ReturnType = c_int32
        
        """
        sys_addr_t sys_process_get_ppu_guid(
            void
        );

        Obtain PPU GUID information
        """
        self.sys_process_get_ppu_guid = RPC.SystemCall(SyscallIndex.SYS_PROCESS_GET_PPU_GUID)
        self.sys_process_get_ppu_guid.ReturnType = POINTER(c_uint32)

        """
        int sys_ppu_thread_exit(
            uint64_t errorcode
        )

        Exit a PPU thread
        """
        self.sys_ppu_thread_exit = RPC.SystemCall(SyscallIndex.SYS_PPU_THREAD_EXIT)
        self.sys_ppu_thread_exit.ArgTypes = [ c_int32 ]
        self.sys_ppu_thread_exit.ReturnType = c_int32

        """
        int sys_console_write(
            const char *s,
            uint32_t len
        );

        Undocumented
        """
        self.sys_console_write = RPC.SystemCall(SyscallIndex.SYS_CONSOLE_WRITE)
        self.sys_console_write.ArgTypes = [ c_char_p, c_uint32 ]
        self.sys_console_write.ReturnType = c_uint32

        """
        int sys_tty_read(
            int ch,
            void *buf,
            unsigned int len,
            unsigned int *preadlen
        );

        Read from a TTY channel
        """
        self.sys_tty_read = RPC.SystemCall(SyscallIndex.SYS_TTY_READ)
        self.sys_tty_read.ArgTypes = [ c_int32, POINTER(c_char), c_uint32, POINTER(c_uint32) ]

        """
        int sys_tty_write(
            int ch,
            const void *buf,
            unsigned int len,
            unsigned int *pwritelen
        );

        Write to a TTY channel
        """
        self.sys_tty_write = RPC.SystemCall(SyscallIndex.SYS_TTY_WRITE)
        self.sys_tty_write.ArgTypes = [ c_int32, c_char_p, c_uint32, POINTER(c_uint32) ]

        """
        sys_prx_id_t sys_prx_load_module(
            const char* path,
            sys_prx_flags_t flags, 
            sys_prx_load_module_option_t pOpt
        );

        Load PRX onto memory
        """
        self.sys_prx_load_module = RPC.SystemCall(SyscallIndex._SYS_PRX_LOAD_MODULE)
        self.sys_prx_load_module.ArgTypes = [ c_char_p, c_uint64, POINTER(sys_prx_load_module_option_t) ]
        self.sys_prx_load_module.ReturnType = c_uint32

        """
        int sys_prx_start_module(
            sys_prx_id_t id,
            size_t args,
            void *argp,
            int *modres,
            sys_prx_flags_t flags, 
            sys_prx_start_module_option_t pOpt
        );

        Start loaded PRX and drive start entry defined in PRX
        """
        self.sys_prx_start_module = RPC.SystemCall(SyscallIndex._SYS_PRX_START_MODULE)
        self.sys_prx_start_module.ArgTypes = [ c_int32, c_uint64, c_void_p, POINTER(c_uint32), POINTER(sys_prx_start_module_option_t) ]
        self.sys_prx_start_module.ReturnType = c_uint32

        """
        int sys_prx_stop_module(
            sys_prx_id_t id,
            size_t args,
            void *argp,
            int *modres,
            sys_prx_flags_t flags, 
            sys_prx_stop_module_option_t pOpt
        );
        Stop loaded PRX and drive stop entry defined in PRX
        """
        self.sys_prx_stop_module = RPC.SystemCall(SyscallIndex._SYS_PRX_STOP_MODULE)
        self.sys_prx_stop_module.ArgTypes = [ c_int32, c_uint64, c_void_p, POINTER(c_uint32), POINTER(sys_prx_stop_module_option_t) ]
        self.sys_prx_stop_module.ReturnType = c_uint32