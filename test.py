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
print("/tunnels2/physical")
orchResponse = orch.get('/tunnels2/physical?limit=30000')
# orchResponse = orch.get('/tunnels2/physical/{nePk}/{tunnelId}')

# print("\nValue:\n{0}\n".format(json.dumps(orchResponse.json(), indent=4, sort_keys=True)))
headers = {'Content-Type': 'text/plain'}
r = orchResponse.json()
for node, nValue in r.items():
    for tunnel, tValue in nValue.items():
        tData = {
            "node": node,
            "tunnel": tunnel,
            "id": tValue["id"],
            "dhgroup": tValue["dhgroup"],
            "tag": tValue["tag"],
            "alias": tValue["alias"],
            "sourceIpAddress": tValue["sourceIpAddress"],
            "destTunnelId": tValue["destTunnelId"],
            "udpDestinationPort": tValue["udpDestinationPort"],
            "dscp": tValue["dscp"],
            "destNePk": tValue["destNePk"],
            "srcNePk": tValue["srcNePk"],
            "operStatus": tValue["operStatus"],
            "adminStatus": tValue["adminStatus"],
            "destIpAddress": tValue["destIpAddress"],
            "destTunnelAlias": tValue["destTunnelAlias"]
        }
        requests.post('https://html-rx-server-cyamato.c9users.io/', data=tData)

print('/cache/interfaceEndpoints')
orchResponse = orch.get('/cache/interfaceEndpoints')
requests.post('https://html-rx-server-cyamato.c9users.io/interfaceEndpoints.json', data=orchResponse)

print('/cache/builtinApps')
orchResponse = orch.get('/cache/builtinApps')
requests.post('https://html-rx-server-cyamato.c9users.io/builtinApps.json', data=orchResponse)

print('/cache/builtinApps')
orchResponse = orch.get('/cache/userApps')
requests.post('https://html-rx-server-cyamato.c9users.io/userApps.json', data=orchResponse)

print('/tunnels2/passThrough')
orchResponse = orch.get('/tunnels2/passThrough')
requests.post('https://html-rx-server-cyamato.c9users.io/passThrough.json', data=orchResponse)

print('/tunnelsConfiguration/overlayInfo')
orchResponse = orch.get('/tunnelsConfiguration/overlayInfo')
requests.post('https://html-rx-server-cyamato.c9users.io/overlayInfo.json', data=orchResponse)

print('/tunnelsConfiguration/passThroughTunnelsInfo')
orchResponse = orch.get('/tunnelsConfiguration/passThroughTunnelsInfo')
requests.post('https://html-rx-server-cyamato.c9users.io/passThroughTunnelsInfo.json', data=orchResponse)

print('/gms/overlays/config')
orchResponse = orch.get('/gms/overlays/config')
requests.post('https://html-rx-server-cyamato.c9users.io/overlayConfig.json', data=orchResponse)

orch.logout()