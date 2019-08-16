'''
AN-012 - Application note demonstrating control of power modules via QIS

This example checks everything is working by connecting to QIS and listing the devices
available for connection.  This verifies QuarchPy, QIS and the connection to the module(s)

########### VERSION HISTORY ###########

14/12/2016 - Iain Robertson - Minor edits for formatting and layout
24/04/2018 - Andy Norrie    - Updated for QuarchPy

########### INSTRUCTIONS ###########

For localhost QIS, run the example as it is.
For remote QIS, comment out the 'openQis()' command and specify the IP:Port in the qusInterface(...) command

####################################
'''
from quarchpy.device import *
from quarchpy.config_files import *
from quarchpy.config_files import test_config_parser

# Scan for devices
allDevices = scanDevices("all")
# Ask user to select one and connect to it
dev_select = userSelectDevice (allDevices)    
my_device = quarchDevice (dev_select)

# Find the correct config file for the connected module (breaker modules only for now)
# We're passing the module connection here, the idn_string can be supplied instead if the module is not currently attached (simulation/demo mode)
file = get_config_path_for_module (module_connection = my_device)
# Parse the file to get the device capabilities
dev_caps = parse_config_file (file)
print ("CONFIG FILE LOCATED:")
print (file)
print ("")
print ("")

# Prints a list of top level capabilities that this module has (differentiating from a 'base' module)
print ("GENERAL CAPABILITIES:")
for key, value in dev_caps.get_general_capabilities().items():
    print(key + " = " + value)
print ("")
print ("")

# Print the list of signals on the module, and the capability flags for each signal
print ("SIGNALS AVAILABLE:")
for sig in dev_caps.get_signals():
    print ("Name:\t" + sig.name)
    for key, value in sig.parameters.items():
        print("\t" + key + " = " + value)
print ("")
print ("")

# Print out the list of signal groups, and the list of signals they control
print ("SIGNALS GROUPS AVAILABLE:")
for group in dev_caps.get_signal_groups():
    print ("Name:\t" + group.name)
    print ("\t", end='')
    for sig in group.signals:
        print (sig + ",", end='')
    print ("")
print ("")
print ("")

# Print the sources on the module, and list their capabilities
print ("SOURCES AVAILABLE:")
for source in dev_caps.get_sources():
    print ("Name:\t" + source.name)
    for key, value in source.parameters.items():
        print("\t" + key + " = " + str(value))
    print ("")
print ("")
print ("")