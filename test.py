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

# #orchResponse = orch.get('/gms/overlays/config/7') #Get Overlays For ID 7
# orchResponse = orch.get('/tunnelsConfiguration/overlayInfo')
orchResponse = orch.get('/tunnels2/physical?limit=1')
# orchResponse = orch.get('/tunnels2/physical/{nePk}/{tunnelId}')

# print("\nValue:\n{0}\n".format(json.dumps(orchResponse.json(), indent=4, sort_keys=True)))
r = orchResponse.json()
tData = "node" + ','
tData = tData + "tunnel" + ','
tData = tData + "id" + ','
tData = tData + "dhgroup" + ','
tData = tData + "tag" + ','
tData = tData + "alias" + ','
tData = tData + "sourceIpAddress" + ','
tData = tData + "destTunnelId" + ','
tData = tData + "udpDestinationPort" + ','
tData = tData + "dscp" + ','
tData = tData + "destNePk" + ','
tData = tData + "srcNePk" + ','
tData = tData + "operStatus" + ','
tData = tData + "adminStatus" + ','
tData = tData + "destIpAddress" + ','
tData = tData + "destTunnelAlias"
tData = tData + "\n"
requests.post('https://html-rx-server-cyamato.c9users.io/', data=tData)
for node, nValue in r.items():
    for tunnel, tValue in nValue.items():
        tData = node + ','
        tData = tData + tunnel + ','
        try: 
            tData = tData + tValue["id"] + ','
            tData = tData + tValue["dhgroup"] + ','
            tData = tData + tValue["tag"] + ','
            tData = tData + tValue["alias"] + ','
            tData = tData + tValue["sourceIpAddress"] + ','
            tData = tData + tValue["destTunnelId"] + ','
            tData = tData + tValue["udpDestinationPort"] + ','
            tData = tData + tValue["dscp"] + ','
            tData = tData + tValue["destNePk"] + ','
            tData = tData + tValue["srcNePk"] + ','
            tData = tData + tValue["operStatus"] + ','
            tData = tData + tValue["adminStatus"] + ','
            tData = tData + tValue["destIpAddress"] + ','
            tData = tData + tValue["destTunnelAlias"]
        except:
            print("Error")
        tData = tData + "\n"
        requests.post('https://html-rx-server-cyamato.c9users.io/', data=tData)

orch.logout()