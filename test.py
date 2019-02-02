import requests
from requests.packages.urllib3.exceptions import InsecureRequestWarning
import json

class Orch:
    def __init__(self):
        self.url_prefix = "https://msp-us-orch.core.kronos.com:443/gms/rest"
        self.session = requests.Session()
        self.data = {}
        self.user = "kentik"
        self.password = "Kronos@78" 
        
    def login(self):
        try:
            response = self.post("/authentication/login", 
                                {"user": self.user, "password": self.password})
            if response.status_code == 200:
                print("Orchestrator login success")
                return True
            else:
                print("Orchestrator login failed: {0}".format(response.text))
                return False
        except:
            print("Unable to connect to Orchestrator")
            return False

    def logout(self):
        response = self.get("/authentication/logout")
        if response.status_code == 200:
            print("Orchestrator logout success")
            return True
        else:
            print("Orchestrator logout failed: {0}".format(response.text))
            return False
        
    def post(self, url, data):
        requests.packages.urllib3.disable_warnings(InsecureRequestWarning)
        response = self.session.post(self.url_prefix + url, json=data, timeout=120, verify=False)
        return response

    def get(self, url):
        requests.packages.urllib3.disable_warnings(InsecureRequestWarning)
        response = self.session.get(self.url_prefix + url, timeout=120, verify=False)
        return response

    def delete(self, url):
        requests.packages.urllib3.disable_warnings(InsecureRequestWarning)
        response = self.session.delete(self.url_prefix + url, timeout=120, verify=False)
        return response
    
orch = Orch()

orch.login()
orchRresponse = orch.get
print("Value:\n{0}".format(orchRresponse.text))
orch.logout()
