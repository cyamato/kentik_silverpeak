#!/usr/bin/python
#*******************************************************************************
#
# Name:         HelloAppliance
#
# Description:  Simple application to use REST API calls to an Appliance
#               to get statistics
#
# Inputs:       None

# Outputs:      1. Return Value (of a REST GET request)
#               2. Response Code
#               3. JSON Object
#               4. JSON Object for use with Python
#               5. The "hostname" value
#
# Notes:        This is an example script. It is provided WITHOUT any warranty.
#               Use at your own risk.
#
# Suggestions:  Here are some things you could add...
#               - Test the Response Code to verify the GET/POST worked
#
#********************************************************************************

import sys, time, json
from VxoaMiniHelp import VxoaMiniHelper 

class Main:
    def __init__(self, argv):
        self.orchIP = "192.168.1.25"
        self.orchUser = "admin"
        self.orchPassword = "Silverpeak1"
        
    def run(self):
        # Create an object
        vxoa = VxoaMiniHelper(self.orchIP, self.orchUser, self.orchPassword)
        
        # Login, get the statistics, then logout
        vxoa.login()
        response = vxoa.get_stats()
        vxoa.logout()

        # Display the "response" object in various formats
        print("1. The return value:    {0}".format(response))             
        print("2. Response Code:       {0}".format(response.status_code)) 
        print("3. CSV output:\n{0}".format(response.text))
        
if __name__ == "__main__":
    main_obj = Main(sys.argv[1:])
    main_obj.run()
