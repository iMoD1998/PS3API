.set STACK_SIZE, 0x200

# 
# Save link register.
#
mflr  %r0
std   %r0,  -0x8(%r1)

#
# Backup nonvolatile registers
#
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
lwz   %r30, 0x70(%r31)
cmpwi %r30, 0
beq   _RPCEnd

#
# Backup hooked function args.
#
stfd  %f1,  STACK_SIZE-0x0110(%r1)
stfd  %f2,  STACK_SIZE-0x0108(%r1)
stfd  %f3,  STACK_SIZE-0x0100(%r1)
stfd  %f4,  STACK_SIZE-0x0098(%r1)
stfd  %f5,  STACK_SIZE-0x0090(%r1)
stfd  %f6,  STACK_SIZE-0x0088(%r1)
stfd  %f7,  STACK_SIZE-0x0080(%r1)
stfd  %f8,  STACK_SIZE-0x0078(%r1)
stfd  %f9,  STACK_SIZE-0x0070(%r1)
std   %r3,  STACK_SIZE-0x0068(%r1)
std   %r4,  STACK_SIZE-0x0060(%r1)
std   %r5,  STACK_SIZE-0x0058(%r1)
std   %r6,  STACK_SIZE-0x0050(%r1)
std   %r7,  STACK_SIZE-0x0048(%r1)
std   %r8,  STACK_SIZE-0x0040(%r1)
std   %r9,  STACK_SIZE-0x0038(%r1)
std   %r10, STACK_SIZE-0x0030(%r1)
std   %r11, STACK_SIZE-0x0028(%r1)


#
# Load registers with arguments.
#
ld    %r3,  0x00(%r31)
ld    %r4,  0x08(%r31)
ld    %r5,  0x10(%r31)
ld    %r6,  0x18(%r31)
ld    %r7,  0x20(%r31)
ld    %r8,  0x28(%r31)
ld    %r9,  0x30(%r31)
ld    %r10, 0x38(%r31)
ld    %r11, 0x40(%r31)
lfs   %f1,  0x48(%r31)
lfs   %f2,  0x4C(%r31)
lfs   %f3,  0x50(%r31)
lfs   %f4,  0x54(%r31)
lfs   %f5,  0x58(%r31)
lfs   %f6,  0x5C(%r31)
lfs   %f7,  0x60(%r31)
lfs   %f8,  0x64(%r31)
lfs   %f9,  0x68(%r31)
mtctr %r30
bctrl # call

#
# Store return values.
#
std   %r3,  0x78(%r31)
stfs  %f1,  0x80(%r31)

#
# Set call address to 0.
# Used to determine externally if function has executed.
#
xor   %r30, %r30, %r30
stw   %r30, 0x70(%r31)

#
# Restore hooked function args.
#
lfd   %f1,  STACK_SIZE-0x0110(%r1)
lfd   %f2,  STACK_SIZE-0x0108(%r1)
lfd   %f3,  STACK_SIZE-0x0100(%r1)
lfd   %f4,  STACK_SIZE-0x0098(%r1)
lfd   %f5,  STACK_SIZE-0x0090(%r1)
lfd   %f6,  STACK_SIZE-0x0088(%r1)
lfd   %f7,  STACK_SIZE-0x0080(%r1)
lfd   %f8,  STACK_SIZE-0x0078(%r1)
lfd   %f9,  STACK_SIZE-0x0070(%r1)
ld    %r3,  STACK_SIZE-0x0068(%r1)
ld    %r4,  STACK_SIZE-0x0060(%r1)
ld    %r5,  STACK_SIZE-0x0058(%r1)
ld    %r6,  STACK_SIZE-0x0050(%r1)
ld    %r7,  STACK_SIZE-0x0048(%r1)
ld    %r8,  STACK_SIZE-0x0040(%r1)
ld    %r9,  STACK_SIZE-0x0038(%r1)
ld    %r10, STACK_SIZE-0x0030(%r1)
ld    %r11, STACK_SIZE-0x0028(%r1)

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