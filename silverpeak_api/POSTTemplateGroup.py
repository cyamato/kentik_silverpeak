#!/usr/bin/python
#*******************************************************************************
#
# Name:         POSTTemplateGroup
#
# Description:  Posts a saved Template Group (file) to an Orchestrator
#
# Inputs:       1. File containing a JSON formatted Template Group
#               2. File containing the Selected Templates (ones used in this group)
#               Note: Input files were created by GETTemplateGroup.py
#
# Notes:        This is an example script. It is provided WITHOUT any warranty.
#               Use at your own risk.
#
# Suggestions:  Here are some things you could add...
#               - Prompt user for file names
#               - Prompt for Orchestrator password
#               - Add more robust error checking
#               - Improve logging for debugging purposes
#
#********************************************************************************
                
import sys, time, json
from OrchMiniHelp import OrchMiniHelper 

class Main:
    def __init__(self, argv):
        self.orchIP = "192.168.1.145"
        self.orchUser = "admin"
        self.orchPassword = "Silverpeak1"

        #Change paths below for your environment, or prompt user for these values
        self.infile1 = "c:\\Users\\tking\\Desktop\\TemplateGroup.txt"
        self.infile2 = "c:\\Users\\tking\\Desktop\\ActiveTemplates.txt"

    def run(self):
        # Create an object
        orch = OrchMiniHelper(self.orchIP, self.orchUser, self.orchPassword)
        
        # Login -- Uses the IP, user name and password stored in the object
        orch.login()
        
        # Load the Template Group (JSON) from the saved file
        templateGroup = {}
        f1 = open(self.infile1, "r")
        templateGroup = json.load(f1)

        # Convert each Template to POST format
        # Note: The GET format shows template "value", however POST requires
        #       this to be changed to "valObject"
        for template in templateGroup['templates']:          
            template['valObject'] = template['value']
            del template['value']

        # Load the selected Templates from the saved file
        select_templateGroup = {}
        f2 = open(self.infile2, "r")
        select_templateGroup = json.load(f2)
            
        # Create the new Template Group and add the templateGroup
        orch.post("/template/templateCreate", {"name":templateGroup['name'], "templates":[]})
        orch.post("/template/templateGroups/" + templateGroup['name'], templateGroup)
        orch.post("/template/templateSelection/" + templateGroup['name'], select_templateGroup)
        
        # Log out
        orch.logout()

        print("SUCCESS: Posted Template Group {0} to {1}".format(templateGroup['name'], self.orchIP))

if __name__ == "__main__":
    main_obj = Main(sys.argv[1:])
    main_obj.run()
