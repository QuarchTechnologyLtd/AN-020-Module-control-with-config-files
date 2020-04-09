'''
AN-020 - Application note demonstrating module control with configuration files

This example shows how to use the configuration file data to find the capabilities of a Quarch module.
The script uses the selected module to find the config file and then parses it.  We then print the various
sections to the terminal.

########### VERSION HISTORY ###########

19/08/2019 - Andy Norrie    - Initial release

########### INSTRUCTIONS ###########

Update to the latest quarcypy (python -m pip install quarchpy --upgrade) to get the latest configuration files
Connect any Quarch breaker/hot-plug module and run the script

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
# This is useful to check if a module supports features such as driving and monitoring
print ("GENERAL CAPABILITIES:")
for key, value in dev_caps.get_general_capabilities().items():
    print(key + " = " + value)
print ("")
print ("")

# Print the list of signals on the module, and the capability flags for each signal
# This can be used to iterate a test over every signal in a module
print ("SIGNALS AVAILABLE:")
for sig in dev_caps.get_signals():
    print ("Name:\t" + sig.name)
    for key, value in sig.parameters.items():
        print("\t" + key + " = " + value)
print ("")
print ("")

# Print out the list of signal groups, and the list of signals they control
# Groups allow faster settings of blocks of signals, without needing to know all the individual names
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
# Some modules have fewer sources available, or have different timing resolutions
print ("SOURCES AVAILABLE:")
for source in dev_caps.get_sources():
    print ("Name:\t" + source.name)
    for key, value in source.parameters.items():
        print("\t" + key + " = " + str(value))
    print ("")
print ("")
print ("")