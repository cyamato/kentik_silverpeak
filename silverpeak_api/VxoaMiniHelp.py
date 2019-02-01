#*******************************************************************************
#
# Class:        VxoaMiniHelper
#               "VXOA" is the Appliance Operating System
#
# Description:  This defines an appliance class used for training purposes.
#               You should use this as a starting point to create a more 
#               complete "VxoaHelper" class.
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
import requests, time, json
import requests.packages.urllib3
requests.packages.urllib3.disable_warnings(requests.packages.urllib3.exceptions.InsecureRequestWarning)

class VxoaMiniHelper:
    def __init__(self, ipaddress, user, password):
        self.ipaddress = ipaddress
        self.url_prefix = "https://" + ipaddress + "/rest/json"
        self.session = requests.Session()
        self.data = {}
        self.user = user
        self.password = password 
        self.app_id = ""
        self.group_id = ""
        print("{0} {1} {2} {3}".format(self.ipaddress,
                                        self.url_prefix,
                                        self.user,
                                        self.password))

    def login(self):
        try:
            response = self.post("/login", 
                                 {"user": self.user, "password": self.password})
            if response.status_code == 200:
                print("{0}: VXOA login success".format(self.ipaddress))
                return True
            else:
                print("{0}: VXOA login failed: {1}".format(self.ipaddress, response.text))
                return False
        except:
            print("{0}: Unable to connect to VXOA appliance".format(self.ipaddress))
            return False
            
    def logout(self):
        response = self.post("/logout", {})
        if response.status_code == 200:
            print("{0}: VXOA logout success".format(self.ipaddress))
            return True
        else:
            print("{0}: VXOA logout failed: {1}".format(self.ipaddress, response.text))
            return False

    def get_stats(self):
	# get stats for last n+2 minutes.  For one hour, 62
        response = self.get("/stats/aggregate/application?timeRange=62&&format=csv")
        if response.status_code == 200:
            return response
            print("{0}: - Stats received".format(self.ipaddress))
        else:
            print("{0}: - Error: Unable to get stats: {1}".format(self.ipaddress, response.text))
            
    def reboot(self):
        response = self.post("/reboot", {'reboot_type': 'Normal'})
        if response.status_code == 200:
            print("{0}: - Reboot request sent successfully".format(self.ipaddress))
        else:
            print("{0}: - Error: Unable to send reboot request: {1}".format(self.ipaddress, response.text))

    def waitForReboot(self):
        #wait 30s for reboot to start
        time.sleep(30)
        #wait up to 5 min for reboot to complete
        count = 0
        while True:
            if self.login():
                break
            else:
                print("Waiting for Appliance to return.")
                time.sleep(5)
                count += 1
                if count > 60:
                    print("Timed out waiting for Appliance to return. Quitting...")
                    sys.exit(1)    
 
    def post(self, url, data):
        response = self.session.post(self.url_prefix + url, json=data, verify=False, timeout=120)
        return response

    def get(self, url):
        response = self.session.get(self.url_prefix + url, verify=False, timeout=120)
        return response

    def delete(self, url):
        response = self.session.delete(self.url_prefix + url, verify=False, timeout=120)
        return response

