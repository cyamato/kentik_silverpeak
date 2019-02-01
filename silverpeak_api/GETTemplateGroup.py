#!/usr/bin/python
#*******************************************************************************
#
# Name:         GETTemplateGroup
#
# Description:  Gets a Template Group from an Orchestrator and saves it to files
#
# Inputs:       Name of the Template Group you wish to save (See Templates tab)

# Outputs:      1. File containing the JSON formatted Template Group
#               2. File containing the Selected Templates (ones used in this group)
#               Note: Output files are used by POSTTemplateGroup.py
#
# Notes:        This is an example script. It is provided WITHOUT any warranty.
#               Use at your own risk.
#
# Suggestions:  Here are some things you could add...
#               - Prompt user for Template Group name
#               - Prompt user for file names
#               - Prompt for Orchestrator password
#               - Modify script to save all Template Groups
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
        
        self.templateGroupName = "CA_Branch"   # Name of the Template Group (see Templates tab)        

        self.outfile1 = "c:\\Users\\tking\\Desktop\\TemplateGroup.txt"
        self.outfile2 = "c:\\Users\\tking\\Desktop\\ActiveTemplates.txt"

    def run(self):
        # Create an object
        orch = OrchMiniHelper(self.orchIP, self.orchUser, self.orchPassword)
        
        # Login -- Uses the IP, user name and password stored in the object
        orch.login()
        
        # Get an array of all Template Groups
        templateGroups = orch.get("/template/templateGroups").json()
        
        # Print a list of all Template Group names
        # Note: In case you want to prompt user in a later version
        print("Template Groups")
        for templateGroup in templateGroups:
            print("    {0}").format(templateGroup['name'])
        
        # Loop through each Template Group and locate the index (idx) that matches
        match = False
        idx = 0
        for templateGroup in templateGroups:           
            if(templateGroup['name'] == self.templateGroupName):
                match = True
                break
            idx += 1
            
        if(not match):
            print("FALIURE: Unable to Locate matching Template Group")
        else:
            # Write the JSON file containing only the matched Template Group
            f1 = open(self.outfile1, "w")
            json.dump(templateGroups[idx], f1)
            print("SUCCESS: Wrote Template Group {0} to: {1}".format(self.templateGroupName,self.outfile1))
            
            # Write the JSON file containing the selected (Active) templates in the group
            select = orch.get("/template/templateSelection/" + templateGroups[idx]['name']).json()
            f2 = open(self.outfile2, "w")
            json.dump(select, f2)
            print("SUCCESS: Wrote active Templates to: {0}".format(self.outfile2))

        #Log out
        orch.logout()

if __name__ == "__main__":
    main_obj = Main(sys.argv[1:])
    main_obj.run()
