import sys
assert sys.version_info >= (3,5), "Python version >= 3.5 required"

#-------------------------------------------------------------------------------
# Version info
#-------------------------------------------------------------------------------
__version__ = "2021-02-22"
# 2020-02-22    Performance added
# 2020-12-18    Ble added
# 2020-11-13    LogfileJson added
# 2020-04-27    MultiProcessing added
# 2020-03-04    Python version check added
#                   Will affect every module that includes debug.py
# 2020-01-25    First version
#-------------------------------------------------------------------------------

#-------------------------------------------------------------------------------
# Define global constants
# Modules that include these variables have to prefix: if debug.On(debug.No) ...
#-------------------------------------------------------------------------------
# 8421 8421 8421 8421 
# ---C EWID bpjm uafA   Characters that can be used in -d flag
#-------------------------------------------------------------------------------
No				= 0x0000    #    0
Application    	= 0x0001    #    1
Function       	= 0x0002    #    2
Data1          	= 0x0004    #    4			antDongle
Data2          	= 0x0008    #    8			usbTrainer
MultiProcessing = 0x0010    #   16
LogfileJson     = 0x0020    #   32
Ble             = 0x0040    #   64
Performance     = 0x0080    #  128

logging_DEBUG   = 0x0100    #  256      That's all
logging_INFO    = 0x0200    #  512
logging_WARNING = 0x0400    # 1024
logging_ERROR   = 0x0800    # 2048
logging_CRITICAL= 0x1000    # 4096      Critical only

All	        	= 0xffff    # 65535		When setting, it's All
Any				= All		#			When checing, it's Any

#-------------------------------------------------------------------------------
# debug.on / off
#-------------------------------------------------------------------------------
# input:        debug level, if not specified set to highest
#
# description:  activate debugging
#
# returns:      true / false
#-------------------------------------------------------------------------------
def activate(pxDebug = All):
    global xDebug
    xDebug = int(pxDebug)

def deactivate():
    global xDebug
    xDebug = No

#-------------------------------------------------------------------------------
# debug
#-------------------------------------------------------------------------------
# input:        Required
#
# description:  Return whether requested debugging is activated
#
#				if on (Application)			returns whether application is to be debugged
#				if on (Application | Function)
#											returns whether one of the two must be debugged
#				if on (Application) and on (Function)
#											returns whether both must be debugged
#				if on (Application & Function)
#											will always return False
#
# returns:      true / false
#-------------------------------------------------------------------------------
def on(pxRequired = All):
    global xDebug

    try:
        xDebug = xDebug
    except:
        xDebug = No	    # If not activated/deactivated; show nothing.

    if xDebug & pxRequired:
        return True
    else:
        return False

#-------------------------------------------------------------------------------
# Main program to test the previous functions
#-------------------------------------------------------------------------------
if __name__ == "__main__":
    print ("Test of debug")

    if on():				print ("Debugging is not initialized")

    deactivate()
    if on():				print ("Debugging is on")

    activate(Application)
    if on():				print ("1. ANY Debugging is on")
    if on(Data1):			print ("1. Data1 debugging is on")
    if on(Function):		print ("1. Function debugging is on")
    if on(Application):	    print ("1. Application debugging is on")

    activate(Data1 | Application)
    if on():				print ("2. ANY Debugging is on")
    if on(Data1):			print ("2. Data1 debugging is on")
    if on(Function):		print ("2. Function debugging is on")
    if on(Application):	    print ("2. Application debugging is on")

    activate(Data1 | Function | Application)
    if on():				print ("3. ANY Debugging is on")
    if on(Data1):			print ("3. Data debugging is on")
    if on(Function):		print ("3. Function debugging is on")
    if on(Application):	    print ("3. Application debugging is on")

    deactivate()
    if on():				print ("Debugging is on")
else:
    pass                    # We're included so do not take action!
