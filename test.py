import requests
import json

host = "https://msp-us-orch.core.kronos.com:443/gms/rest"
session = requests.Session
try:
    response = session.post(host + "/authentication/login", 
                        {"user": "Kentik", "password": "Kronos@78"})
    if response.status_code == 200:
        print("Orchestrator login success")
        requests.packages.urllib3.disable_warnings()
        response = session.get(host + '/stats/aggregate/tunnel', timeout=120, verify=False)
        print(response.json())
    else:
        print("Orchestrator login failed: {1}".format(response.text))
except:
    print("Unable to connect to Orchestrator")