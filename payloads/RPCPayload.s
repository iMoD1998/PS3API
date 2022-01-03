.set STACK_SIZE, 0x220

#
# Layout for call context structure.
#
.set CALL_CONTEXT_R3,           0x00
.set CALL_CONTEXT_R4,           CALL_CONTEXT_R3 + 0x8
.set CALL_CONTEXT_R5,           CALL_CONTEXT_R4 + 0x8
.set CALL_CONTEXT_R6,           CALL_CONTEXT_R5 + 0x8
.set CALL_CONTEXT_R7,           CALL_CONTEXT_R6 + 0x8
.set CALL_CONTEXT_R8,           CALL_CONTEXT_R7 + 0x8
.set CALL_CONTEXT_R9,           CALL_CONTEXT_R8 + 0x8
.set CALL_CONTEXT_R10,          CALL_CONTEXT_R9 + 0x8
.set CALL_CONTEXT_R11,          CALL_CONTEXT_R10 + 0x8
.set CALL_CONTEXT_F1,           CALL_CONTEXT_R11 + 0x8
.set CALL_CONTEXT_F2,           CALL_CONTEXT_F1 + 0x4
.set CALL_CONTEXT_F3,           CALL_CONTEXT_F2 + 0x4
.set CALL_CONTEXT_F4,           CALL_CONTEXT_F3 + 0x4
.set CALL_CONTEXT_F5,           CALL_CONTEXT_F4 + 0x4
.set CALL_CONTEXT_F6,           CALL_CONTEXT_F5 + 0x4
.set CALL_CONTEXT_F7,           CALL_CONTEXT_F6 + 0x4
.set CALL_CONTEXT_F8,           CALL_CONTEXT_F7 + 0x4
.set CALL_CONTEXT_F9,           CALL_CONTEXT_F8 + 0x4
.set CALL_CONTEXT_CALL_TYPE,    CALL_CONTEXT_F9 + 0x4
.set CALL_CONTEXT_CALL_ADDRESS, CALL_CONTEXT_CALL_TYPE + 0x4
.set CALL_CONTEXT_CALL_TOC,     CALL_CONTEXT_CALL_ADDRESS + 0x8
.set CALL_CONTEXT_RETURN_R3,    CALL_CONTEXT_CALL_TOC  + 0x8
.set CALL_CONTEXT_RETURN_F1,    CALL_CONTEXT_RETURN_R3 + 0x8

.set CALL_TYPE_NONE, 0x00
.set CALL_TYPE_FUNCTION, 0x01
.set CALL_TYPE_FUNCTION_SET_TOC, 0x02
.set CALL_TYPE_FUNCTION_OPD_ENTRY, 0x03
.set CALL_TYPE_SYS_CALL, 0x04

# 
# Save link register.
#
mflr  %r0
std   %r0,  -0x8(%r1)

#
# Backup nonvolatile registers
#
std   %r28, -0x28(%r1)
std   %r29, -0x20(%r1)
std   %r30, -0x18(%r1)
std   %r31, -0x10(%r1)

#
# Allocate stack space
#
stdu  %r1,  -STACK_SIZE(%r1)

#
# Free space address used to store args.
#
lis   %r31, 0xCAFEBEEF@h
ori   %r31, %r31, 0xCAFEBEEF@l

#
# Check if we have a function to call.
#
ld    %r30, CALL_CONTEXT_CALL_ADDRESS(%r31)
cmpwi %r30, 0
beq   _RPCEnd

#
# Backup hooked function args.
#
stfd  %f1,  STACK_SIZE-0x0118(%r1)
stfd  %f2,  STACK_SIZE-0x0110(%r1)
stfd  %f3,  STACK_SIZE-0x0108(%r1)
stfd  %f4,  STACK_SIZE-0x0100(%r1)
stfd  %f5,  STACK_SIZE-0x0098(%r1)
stfd  %f6,  STACK_SIZE-0x0090(%r1)
stfd  %f7,  STACK_SIZE-0x0088(%r1)
stfd  %f8,  STACK_SIZE-0x0080(%r1)
stfd  %f9,  STACK_SIZE-0x0078(%r1)
std   %r3,  STACK_SIZE-0x0070(%r1)
std   %r4,  STACK_SIZE-0x0068(%r1)
std   %r5,  STACK_SIZE-0x0060(%r1)
std   %r6,  STACK_SIZE-0x0058(%r1)
std   %r7,  STACK_SIZE-0x0050(%r1)
std   %r8,  STACK_SIZE-0x0048(%r1)
std   %r9,  STACK_SIZE-0x0040(%r1)
std   %r10, STACK_SIZE-0x0038(%r1)
std   %r11, STACK_SIZE-0x0030(%r1)


#
# Load registers with arguments.
#
ld    %r3,  CALL_CONTEXT_R3(%r31)
ld    %r4,  CALL_CONTEXT_R4(%r31)
ld    %r5,  CALL_CONTEXT_R5(%r31)
ld    %r6,  CALL_CONTEXT_R6(%r31)
ld    %r7,  CALL_CONTEXT_R7(%r31)
ld    %r8,  CALL_CONTEXT_R8(%r31)
ld    %r9,  CALL_CONTEXT_R9(%r31)
ld    %r10, CALL_CONTEXT_R10(%r31)
ld    %r11, CALL_CONTEXT_R11(%r31)
lfs   %f1,  CALL_CONTEXT_F1(%r31)
lfs   %f2,  CALL_CONTEXT_F2(%r31)
lfs   %f3,  CALL_CONTEXT_F3(%r31)
lfs   %f4,  CALL_CONTEXT_F4(%r31)
lfs   %f5,  CALL_CONTEXT_F5(%r31)
lfs   %f6,  CALL_CONTEXT_F6(%r31)
lfs   %f7,  CALL_CONTEXT_F7(%r31)
lfs   %f8,  CALL_CONTEXT_F8(%r31)
lfs   %f9,  CALL_CONTEXT_F9(%r31)

#
# Check which call type we have.
#
lwz   %r29, CALL_CONTEXT_CALL_TYPE(%r31)

#
# Standard call to function pointer in the call context.
#
_CheckCall:
cmpwi %r29, CALL_TYPE_FUNCTION
bne   _CheckCallTOC
mr    %r28, %r2
b     _CallWithTOC

#
# Standard call to function pointer while using the TOC provided in the call context.
#
_CheckCallTOC:
cmpwi %r29, CALL_TYPE_FUNCTION_SET_TOC
bne   _CheckCallOpd
ld    %r28, CALL_CONTEXT_CALL_TOC(%r31)
b     _CallWithTOC

#
# Call to OPD entry pointer which contains the function address and TOC.
#
# Example entry:
# OPDEntry <sub_258460, 0x724C38>
#
_CheckCallOpd:
cmpwi %r29, CALL_TYPE_FUNCTION_OPD_ENTRY
bne   _CheckCallSysCall
lwz   %r28, 4(%r30)
lwz   %r30, 0(%r30)
b     _CallWithTOC

#
# Call system call with the system call index provided in r11
# 
_CheckCallSysCall:
cmpwi %r29, CALL_TYPE_SYS_CALL
bne  _PostCallNoReturn
sc
b    _PostCall

_CallWithTOC:
std   %r2,  STACK_SIZE-0x0120(%r1)
mr    %r2,  %r28
mtctr %r30
bctrl # Call Function
ld    %r2,  STACK_SIZE-0x0120(%r1)

#
# Store return values.
#
_PostCall:
std   %r3,  CALL_CONTEXT_RETURN_R3(%r31)
stfs  %f1,  CALL_CONTEXT_RETURN_F1(%r31)

#
# Set call address to 0.
# Used to determine externally if function has executed.
#
_PostCallNoReturn:
xor   %r30, %r30, %r30
std   %r30, CALL_CONTEXT_CALL_ADDRESS(%r31)

#
# Restore hooked function args.
#
lfd  %f1,  STACK_SIZE-0x0118(%r1)
lfd  %f2,  STACK_SIZE-0x0110(%r1)
lfd  %f3,  STACK_SIZE-0x0108(%r1)
lfd  %f4,  STACK_SIZE-0x0100(%r1)
lfd  %f5,  STACK_SIZE-0x0098(%r1)
lfd  %f6,  STACK_SIZE-0x0090(%r1)
lfd  %f7,  STACK_SIZE-0x0088(%r1)
lfd  %f8,  STACK_SIZE-0x0080(%r1)
lfd  %f9,  STACK_SIZE-0x0078(%r1)
ld   %r3,  STACK_SIZE-0x0070(%r1)
ld   %r4,  STACK_SIZE-0x0068(%r1)
ld   %r5,  STACK_SIZE-0x0060(%r1)
ld   %r6,  STACK_SIZE-0x0058(%r1)
ld   %r7,  STACK_SIZE-0x0050(%r1)
ld   %r8,  STACK_SIZE-0x0048(%r1)
ld   %r9,  STACK_SIZE-0x0040(%r1)
ld   %r10, STACK_SIZE-0x0038(%r1)
ld   %r11, STACK_SIZE-0x0030(%r1)

#
# Free stack.
#
_RPCEnd:
addi  %r1,  %r1, STACK_SIZE

#
# Move old return address to link register
# ready for when we execute the original function.
#
ld    %r0,  -0x8(%r1)
mtlr  %r0

#
# Set the count register to the original function after the hook.
#
lis   %r31, 0xDEADC0DE@h
ori   %r31, %r31, 0xDEADC0DE@l
mtctr %r31

#
# Restore nonvolatile registers.
#
ld    %r28, -0x28(%r1)
ld    %r29, -0x20(%r1)
ld    %r30, -0x18(%r1)
ld    %r31, -0x10(%r1)

#
# Space for hot patching overwritten instructions.
#
nop
nop
nop
nop
nop

#
# Finally branch to original.
#
bctr

#
# If we ended here we are fuck.
#
trap