#*******************************************************************************
#
# Class:        OrchMiniHelper
#
# Description:  This defines an orchestrator class used for training purposes.
#               You should use this as a starting point to create a more 
#               complete "OrchHelper" class.
#
# Inputs:       

# Outputs:      
#
# Notes:        This is an example script. It is provided WITHOUT any warranty.
#               Use at your own risk.
#
# Suggestions:  This file is a mini version of a class. Here are some things you
#               could add...
#               - Add more robust error checking
#               - Improve logging for debugging purposes
#               - Other commly used methods
#
#********************************************************************************
import requests
import json

class OrchMiniHelper:

    def __init__(self, ipaddress, user, password):
        self.ipaddress = ipaddress
        self.url_prefix = "https://" + ipaddress + ":443/gms/rest"
        self.session = requests.Session()
        self.data = {}
        self.user = user
        self.password = password 
        
    def login(self):
        try:
            response = self.post("/authentication/login", 
                                {"user": self.user, "password": self.password})
            if response.status_code == 200:
                print("{0}: Orchestrator login success".format(self.ipaddress))
                return True
            else:
                print("{0}: Orchestrator login failed: {1}".format(self.ipaddress, response.text))
                return False
        except:
            print("{0}: Unable to connect to Orchestrator".format(self.ipaddress))
            return False

    def logout(self):
        response = self.get("/authentication/logout")
        if response.status_code == 200:
            print("{0}: Orchestrator logout success".format(self.ipaddress))
            return True
        else:
            print("{0}: Orchestrator logout failed: {1}".format(self.ipaddress, response.text))
            return False
        
    def post(self, url, data):
        requests.packages.urllib3.disable_warnings()
        response = self.session.post(self.url_prefix + url, json=data, timeout=120, verify=False)
        return response

    def get(self, url):
        requests.packages.urllib3.disable_warnings()
        response = self.session.get(self.url_prefix + url, timeout=120, verify=False)
        return response

    def delete(self, url):
        requests.packages.urllib3.disable_warnings()
        response = self.session.delete(self.url_prefix + url, timeout=120, verify=False)
        return response

