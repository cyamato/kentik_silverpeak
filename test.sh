#!/bin/bash
echo
data='{"user":"kentik","password":"Kronos@78"}'
echo "$data"
echo
echo Testing Silver Peak Auth
curl -i -k -L -X POST -H "Content-Type: application/json" -d "$data" https://msp-us-orch.core.kronos.com/8.1.4.9-65644/rest/json/authentication/login

echo
echo Testing Silver Peak Auth Type
curl -i -k -L -X POST -H "Content-Type: application/json" -d "$data" https://msp-us-orch.core.kronos.com/8.1.4.9-65644/rest/json/authentication/userAuthType

echo
echo Testing Silvver Peak Login Status
curl -i -k -L -X GET https://msp-us-orch.core.kronos.com/8.1.4.9-65644/rest/json/authentication/loginStatus